# Daily debrief

A Python project that fetches the latest news, performs sentiment analysis, retrieves NASA’s Astronomy Picture of the Day, and emails a concise daily summary right to your inbox.

## Features

### 1. Daily News Retrieval
- US headlines (in English)
- Portugal news (in Portuguese)
- Company-specific (job) news (in English)
Date Range: Pulls news from yesterday to today at 7:30 AM.

### 2. Sentiment Analysis (NLP)

Assesses each piece of news as negative, neutral, or positive.
The result is a color-coded representation:
- 🔴 Red → Negative
- 🟡 Yellow → Neutral
- 🟢 Green → Positive

### 3. NASA Astronomy Picture of the Day

Fetches the latest APOD image or video (with a brief explanation).

### 4. Automated Email Report

Sends a daily email at 8:00 AM containing:
- All gathered news with sentiment analysis
- NASA’s APOD (embedded or linked)
Scheduled via [PythonAnywhere](https://www.pythonanywhere.com/) (or your preferred hosting/scheduling solution).

## Project Overview

**APIs Used:**
- News API (for headlines and custom queries).
- NASA API (for Astronomy Picture of the Day - APOD).

**Sentiment Analysis:** Basic NLP approach on both English and Portuguese sources to determine sentiment polarity.

**Automation:** Cron-like scheduling on PythonAnywhere triggers the script every day at 8:00 AM.

**Reporting:** A single email summarizes top news stories, color-coded sentiment, and includes the NASA APOD.

## Directory Tree
This project has the following directory structure and the next sections attempt to explain them.

```
nlp-email_sender
|   .env
|   .gitignore
|   config.yaml
|   email_sender.py
|   get_dates.py
|   main.py
|   nasa_apod_request.py
|   news_loop.py
|   README.md
|   requirements.txt
|   sentiment_analysis.py
|   
+---venv
\---__pycache__
```

## Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/DanLeiria/<REPO_NAME>.git
cd <REPO_NAME>
```

### 2. Create a Virtual Environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Configure Environment Variables
You’ll need API keys for the News API and NASA. Create environment variables (``.env``) and a config file (``config.yaml``) to store:

In the ``.env`` add the following variables: NEWS_API_KEY, NASA_API_KEY, SMTP_HOST, SMTP_PASSWORD, RECIPIENT_EMAIL, USERNAME_EMAIL

In the ``config.yaml`` add the following variables: EMAIL_SUBJECT, NEWS_SORT, NEWS_QUERY, NEWS_LANG_1, NEWS_LIMIT.

### 5. Schedule the Script

In PythonAnywhere, go to the “Tasks” or “Schedule” section.
Set the script to run daily at 8:00 AM local time.
Adjust your time zone or scheduling preferences as needed.

## License
This project is licensed under the MIT License - feel free to modify and distribute as you see fit.

