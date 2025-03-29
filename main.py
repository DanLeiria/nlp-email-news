###################################################################################
### -----                             LIBRARY                             ----- ###
###################################################################################
"""Load library and settings"""

import os  # Used for handling file and directory paths in a cross-platform way

# Set working directory
""" Uncomment the 2 lines below if using PythonAnywhere """
# project_folder = os.path.expanduser("~/nlp-email-news")
# os.chdir(project_folder)

import requests  # Import APIs
from dotenv import load_dotenv  # Import secret crendentials from .env
import yaml  # # Load project settings from a .yaml configuration file

from email_sender import send_email  # Load function in the script
from news_loop import news_loop  # Load function in the script
from nasa_apod_request import get_nasa_apod  # Load function in the script
from get_dates import get_news_time_range  # Load function in the script

# Load variables from .env (secret credentials)
""" Uncomment the line below if using PythonAnywhere """
# load_dotenv(os.path.join(project_folder, ".env"))
""" Comment the line below if using PythonAnywhere """
load_dotenv()

# Load config file (public credentials)
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

if not config:
    raise ValueError("Couldn't load config file.")  # Logs


###################################################################################
### -----                      GET NEWS FROM API                          ----- ###
###################################################################################
"""
Retrieves news through their API.
"""

# Get settings for the retrieving the news
NEWS_TIME_FROM, NEWS_TIME_TO = get_news_time_range()

NEWS_SORT = config["NEWS_SORT"]
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

NEWS_QUERY_1 = config["NEWS_QUERY_1"]  # News regarding Portugal
NEWS_LANG_1 = config["NEWS_LANG_1"]  # Language

NEWS_QUERY_2 = config["NEWS_QUERY_2"]  # News regarding Danfoss
NEWS_LANG_2 = config["NEWS_LANG_2"]  # Language

if not all(
    [NEWS_SORT, NEWS_API_KEY, NEWS_QUERY_1, NEWS_LANG_1, NEWS_QUERY_2, NEWS_LANG_2]
):
    raise ValueError("News (API) - Credentials missing.")  # Logs

NEWS_URL_1 = (
    f"https://newsapi.org/v2/everything?q={NEWS_QUERY_1}"
    f"&from={NEWS_TIME_FROM}"
    f"&to={NEWS_TIME_TO}"
    f"&language={NEWS_LANG_1}"
    f"&sortBy={NEWS_SORT}"
    f"&apiKey={NEWS_API_KEY}"
)

NEWS_URL_2 = (
    f"https://newsapi.org/v2/everything?q={NEWS_QUERY_2}"
    f"&from={NEWS_TIME_FROM}"
    f"&to={NEWS_TIME_TO}"
    f"&language={NEWS_LANG_2}"
    f"&sortBy={NEWS_SORT}"
    f"&apiKey={NEWS_API_KEY}"
)

NEWS_URL_3 = f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={NEWS_API_KEY}"

# Make a request
api_request_1 = requests.get(NEWS_URL_1)
api_request_2 = requests.get(NEWS_URL_2)
api_request_3 = requests.get(NEWS_URL_3)

# Check responses (logs)
if api_request_1.status_code != 200:
    print("[INFO] News API request 1 failed.")

if api_request_2.status_code != 200:
    print("[INFO] News API request 2 failed.")

if api_request_3.status_code != 200:
    print("[INFO] News API request 3 failed.")

# Get data as dictionary
content_country = api_request_1.json()
content_job = api_request_2.json()
content_headlines = api_request_3.json()

# News: Country
news_country_total = news_loop(
    content=content_country, lang="pt", news_limit=config["NEWS_LIMIT_1"]
)

# News: Job
news_job_total = news_loop(
    content=content_job, lang="en", news_limit=config["NEWS_LIMIT_2"]
)

# News: Headlines
news_headline_total = news_loop(
    content=content_headlines, lang="en", news_limit=config["NEWS_LIMIT_3"]
)


###################################################################################
### -----                   GET NASA APOD FROM API                        ----- ###
###################################################################################
"""
Extracted NASA APOD using NASA API and the script nasa_apod_request.py
"""

NASA_API_KEY = os.getenv("NASA_API_KEY")

apod_text, apod = get_nasa_apod(api_key=NASA_API_KEY)


###################################################################################
### -----                         SEND EMAIL                              ----- ###
###################################################################################
"""
Combine all news and NASA picture into one final message.
Send the email using the script email_sender.py
"""

# Final message for the email
final_message = (
    "Headlines: \n"
    + news_headline_total
    + "\n NASA - APOD:"
    + apod_text
    + "\n Country news: \n"
    + news_country_total
    + "\n Company news: \n"
    + news_job_total
)

# Get the personal email credentials
EMAIL_HOST = os.getenv("HOST")
EMAIL_USERNAME = os.getenv("USERNAME_EMAIL")
EMAIL_RECEIVER = os.getenv("RECEIVER")
EMAIL_PASSWORD = os.getenv("PASSWORD")

if not all([EMAIL_HOST, EMAIL_USERNAME, EMAIL_RECEIVER, EMAIL_PASSWORD]):
    raise ValueError("EMAIL - Credentials missing.")  # Logs

# Send email
send_email(
    message=final_message,
    subject=config["EMAIL_SUBJECT"],
    host=EMAIL_HOST,
    username=EMAIL_USERNAME,
    password=EMAIL_PASSWORD,
    receiver=EMAIL_RECEIVER,
    nasa_apod=apod,
)
