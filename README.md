# Cloathing-Similiarity

## follow the following steps:
# Step-1
  # Data Collection and Preprocessing:
Use web scraping tools like BeautifulSoup or Scrapy to gather a dataset of clothing item descriptions
from different websites. Extract the relevant text information for each item.
Preprocess the text data by cleaning it, which may include removing HTML tags, special characters,
and performing text normalization techniques like lowercase conversion and
stemming/lemmatization.
# Step-2
 # Similarity Measurement:
Develop a method to extract useful features from the text descriptions. This could involve techniques
like TF-IDF (Term Frequency-Inverse Document Frequency) or word embeddings like Word2Vec or
GloVe.
Compute the similarity between the input text and the descriptions in your database using techniques
like cosine similarity or Jaccard similarity.
#  Step-3
#  Ranking and Suggestions:
Design a function that accepts a text string, extracts its features using the same method as the previous
step, computes similarities with the items in the database, ranks them based on similarity, and returns
the URLs of the top-N most similar items.
You can use data structures like priority queues or sorting algorithms to efficiently rank the items
based on similarity.
# Step-4
#  Deployment:
Deploy your function as a web service on Google Cloud Functions or Google Cloud Run. You'll need
to create an API endpoint that accepts JSON requests containing the text description and returns
JSON responses with ranked suggestions.
Make sure to include the necessary dependencies and set up the deployment environment correctly.
Document the code by adding comments and create a ReadMe file that provides an overview of the
project, instructions for deployment, and any other relevant information.

##           Process to Deploy Flask app using cloud Run

# What is Web Framework?
Web Application Framework or simply Web Framework represents a collection of libraries
and modules that enables a web application developer to write applications without having to
bother about low-level details such as protocols, thread management etc.
# What is Flask?
Flask is a web application framework written in Python. It is developed by Armin Ronacher,
who leads an international group of Python enthusiasts named Pocco. Flask is based on the
Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects
# Jinja2
Jinja2 is a popular templating engine for Python. A web templating system combines a
template with a certain data source to render dynamic web pages.
Prerequisite
Python >= 2.6
# Flask
Steps to Install a Python: -
1. Go to https://www.python.org/
2. Click on download Menu
3. Scroll down to select a version you want to install and click on download link
4. Open an executable file downloaded to install it
5. Make sure the checkbox i.e., Add a path to environment variable is tick while
installing executable file
6. Click on Next …. And install it
Steps to Check Python is installed properly?
1. Open a terminal or CMD in your system
2. Type command: - python -V or python –version
3. If is show a version of python you installed, it means your python installation is
successful
# Steps to Install Flask: -
1. Open a terminal or CMD in your system
2. Write a command: -
a. pip install flask (for python version < 3)
b. pip3 install flask (for python version > 3)
3. If you want to install a specific version of flask:
a. pip install flask == flask_version_number (for python version < 3)
b. pip3 install flask == flask_version_number (for python version > 3)
# Steps to Check flask is installed properly or not?
1. Open a terminal or CMD in your system
2. Write a Command:
a. python or python3
b. import flask
3. Press ENTER key
4. If it runs without any error, it means flask is installed successfully

##  The Steps required for deploying flask app using google app engine are:-
1. main.py  contains flask app
2. requirements.txt  contains list of packages required for flask app to run
3. app.yaml  define a runtime which you are using ex. runtime: python38
After creation and test of flask app locally, Steps to deploy it
Main part is creating a project in your google cloud using link
https://console.cloud.google.com/
1. Download Google cloud SDK :-
https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe
2. command to Check Google cloud Is installed or not:- gcloud --version
3. Login using gcloud  gcloud auth login
4. Set your app into gcloud project  gcloud config set project <name of the project
you created in Google cloud console>
5. Deploy the app  gcloud app deploy
6. You can stream logs from the command line by running: - gcloud app logs tail -s
default
7. To view your application in the web browser run : gcloud app browse
Reference :- https://realpython.com/python-web-applications/
