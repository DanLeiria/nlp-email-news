###################################################################################
### IMPORT ###
###################################################################################

import requests
from email_sender import send_email
from news_loop import news_loop
from dotenv import load_dotenv
import os
import yaml


# Load variables from .env
load_dotenv()

# Load config file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

###################################################################################
### NEWS API ###
###################################################################################

# Add limit number of titles per news subject
NEWS_TIME = "2025-03-10"
NEWS_SORT = config["NEWS_SORT"]
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

NEWS_QUERY_1 = config["NEWS_QUERY_1"]  # News regarding Portugal
NEWS_LANG_1 = config["NEWS_LANG_1"]  # Language

NEWS_QUERY_2 = config["NEWS_LANG_2"]  # News regarding Danfoss
NEWS_LANG_2 = config["NEWS_LANG_2"]  # Language

NEWS_URL_1 = (
    f"https://newsapi.org/v2/everything?q={NEWS_QUERY_1}"
    f"&from={NEWS_TIME}"
    f"&language={NEWS_LANG_1}"
    f"&sortBy={NEWS_SORT}"
    f"&apiKey={NEWS_API_KEY}"
)

NEWS_URL_2 = (
    f"https://newsapi.org/v2/everything?q={NEWS_QUERY_2}"
    f"&from={NEWS_TIME}"
    f"&language={NEWS_LANG_2}"
    f"&sortBy={NEWS_SORT}"
    f"&apiKey={NEWS_API_KEY}"
)

NEWS_URL_3 = f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={NEWS_API_KEY}"

# Make a request
api_request_1 = requests.get(NEWS_URL_1)
api_request_2 = requests.get(NEWS_URL_2)
api_request_3 = requests.get(NEWS_URL_3)

# Get data as dictionary
content_country = api_request_1.json()
content_job = api_request_2.json()
content_headlines = api_request_3.json()

print(content_country)
print(content_job)
print(content_headlines)


# News: Country
news_country_total = news_loop(
    content=content_country, lang="pt", news_limit=config["NEWS_LIMIT_1"]
)

print(news_country_total)

# News: Job
news_job_total = news_loop(
    content=content_job, lang="en", news_limit=config["NEWS_LIMIT_2"]
)

print(news_job_total)

# News: Headlines
news_headline_total = news_loop(
    content=content_headlines, lang="en", news_limit=config["NEWS_LIMIT_3"]
)

print(news_headline_total)


###################################################################################
### NASA API ###
###################################################################################


###################################################################################
### SEND EMAIL ###
###################################################################################

# Final message for the email
final_message = (
    "Headlines: \n"
    + news_headline_total
    + "\n Country news: \n"
    + news_country_total
    + "\n Company news: \n"
    + news_job_total
)

# Get the personal email credentials
EMAIL_HOST = os.getenv("HOST")
EMAIL_USERNAME = os.getenv("USERNAME")
EMAIL_RECEIVER = os.getenv("RECEIVER")
EMAIL_PASSWORD = os.getenv("PASSWORD")

# Send email
send_email(
    message=final_message,
    subject=config["EMAIL_SUBJECT"],
    host=EMAIL_HOST,
    username=EMAIL_USERNAME,
    password=EMAIL_PASSWORD,
    receiver=EMAIL_RECEIVER,
)
