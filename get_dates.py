import datetime


def get_news_time_range():
    # Get today’s date
    today = datetime.datetime.today()
    # print(today)

    # Create datetime objects for today and yesterday date and time
    yesterday = today - datetime.timedelta(days=1)

    # Convert to strings in ISO format (YYYY-MM-DDTHH:MM:SS)
    news_time_from = yesterday.strftime("%Y-%m-%dT%H:%M:%S")
    news_time_to = today.strftime("%Y-%m-%dT%H:%M:%S")

    return news_time_from, news_time_to


if __name__ == "__main__":
    print(get_news_time_range())
