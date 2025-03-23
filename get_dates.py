import datetime


def get_news_time_range():
    # Get today’s date
    today = datetime.date.today()

    # Create datetime objects at 8:00 AM for today and yesterday
    today_8am = datetime.datetime.combine(today, datetime.time(7, 30))
    yesterday_8am = today_8am - datetime.timedelta(days=1)

    # Convert to strings in ISO format (YYYY-MM-DDTHH:MM:SS)
    news_time_from = yesterday_8am.strftime("%Y-%m-%dT%H:%M:%S")
    news_time_to = today_8am.strftime("%Y-%m-%dT%H:%M:%S")

    return news_time_from, news_time_to
