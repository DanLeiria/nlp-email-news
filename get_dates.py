import datetime


def get_news_time_range():
    # Get today’s date
    today = datetime.datetime.today()
    # print(today)

    # Create datetime objects for today and yesterday date and time
    yesterday = today - datetime.timedelta(days=1)

    # Convert to strings in ISO format (YYYY-MM-DD)
    news_time_from = yesterday.strftime("%Y-%m-%d")
    news_time_to = today.strftime("%Y-%m-%d")

    return news_time_from, news_time_to


if __name__ == "__main__":
    print(get_news_time_range())
