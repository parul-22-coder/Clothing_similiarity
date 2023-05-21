# import required packages
# Create constructor object
# Creating routing
# Running web app
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify

 
# Step 1: Collect and preprocess data
def scrape_clothing_descriptions():
    # Use web scraping to gather clothing item descriptions from a website
    # Return a list of clothing descriptions
    # You can modify this function to scrape multiple websites or use an existing dataset
 
    # Sample implementation: scraping clothing descriptions from a website
     url = "https://www.amazon.com/s?k=womens+dresses"
     response = requests.get(url)
     soup = BeautifulSoup(response.content, "html.parser")
     descriptions = [item.text for item in soup.find_all("div", class_="description")]
     return descriptions


 
# Step 2: Measure similarity
def compute_similarity(input_text, descriptions):
    # Use TF-IDF to extract features from the text descriptions
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(descriptions + [input_text])
    input_vector = vectors[-1]
 
    # Calculate cosine similarity between the input text and descriptions
    similarities = cosine_similarity(input_vector, vectors[:-1])
    return similarities
 
# Step 3: Return ranked results
def get_top_similar_items(input_text, descriptions, urls, n=5):
    similarities = compute_similarity(input_text, descriptions)
    sorted_indices = similarities.argsort()[0][::-1][:n]
    top_similar_items = [{"url": urls[idx], "similarity": similarities[0][idx]} for idx in sorted_indices]
    return top_similar_items
 
# Step 4: Deploy the function using Flask

from flask import Flask,render_template

app = Flask(__name__)


@app.route("/similar-items", methods=["POST"])
def find_similar_items():
    input_text = request.json["text"]
    descriptions = scrape_clothing_descriptions()  # Modify this function for your specific data collection method
    urls = "https://www.amazon.com/s?k=womens+dresses" # Modify this function to get the URLs corresponding to the descriptions
    top_similar_items = get_top_similar_items(input_text, descriptions, urls)
    return jsonify(top_similar_items)
 


@app.route("/css")  
def css():
    return render_template("css.html")

if __name__ == "__main__":
    app.run(port=8080)



