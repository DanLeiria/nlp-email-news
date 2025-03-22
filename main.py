###################################################################################
### IMPORT ###
###################################################################################

import requests
from email_sender import send_email
from news_loop import news_loop
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

###################################################################################
### NEWS API ###
###################################################################################

# Add limit number of titles per news subject
NEWS_TIME = "2025-03-10"
NEWS_SORT = "relevancy"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

NEWS_QUERY_1 = "Portugal"  # News regarding Portugal
NEWS_LANG_1 = "pt"  # Language

NEWS_QUERY_2 = "Danfoss"  # News regarding Danfoss
NEWS_LANG_2 = "en"  # Language

NEWS_QUERY_3 = "Danfoss"  # News regarding Danfoss
NEWS_LANG_3 = "en"  # Language

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

# NEWS_URL_3 = (
#     f"https://newsapi.org/v2/everything?q={NEWS_QUERY_2}"
#     f"&from={NEWS_TIME}"
#     f"&language={NEWS_LANG_2}"
#     f"&sortBy={NEWS_SORT}"
#     f"&apiKey={NEWS_API_KEY}"
# )

# Make a request
api_request_1 = requests.get(NEWS_URL_1)
api_request_2 = requests.get(NEWS_URL_2)

# Get data as dictionary
content_country = api_request_1.json()
content_job = api_request_2.json()

print(content_country)
print(content_job)

# News: Country
news_country_total = news_loop(
    content=content_country, content_type="country", news_limit=25
)

print(news_country_total)

# News: Job
news_job_total = news_loop(content=content_job, content_type="job", news_limit=15)

print(news_job_total)


###################################################################################
### NASA API ###
###################################################################################


###################################################################################
### SEND EMAIL ###
###################################################################################

# Final message for the email
final_message = (
    "Headlines: \n"
    + "Country news: \n"
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
    host=EMAIL_HOST,
    username=EMAIL_USERNAME,
    password=EMAIL_PASSWORD,
    receiver=EMAIL_RECEIVER,
)
