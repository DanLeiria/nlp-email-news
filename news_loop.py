from sentiment_analysis import vibe_score_en
# Removed the portuguese analyser because of the server
# , vibe_score_pt


def news_loop(content: dict, lang: str, news_limit: int):
    """
    Loop through the news extracted.
    In the loop:
        - Add news title and link source to send by email.
        - Portugal has a condition of rejecting brazilian news.
        - Filter number of news according to given limit.
        - Sentiment analysis of the title and description.
        - Sentiment score is added to email text as color emoji.

    Parameters:
        - content: API news (dict)
        - lang: only 'en' or 'pt' (string)
        - news_limit: maximum number of news output (int)
    Output:
        - News list as a string.
    """
    # Starting point
    news_total = ""
    i = 0

    try:
        # Loop
        for article in content["articles"]:
            # Extract the value
            news_title = article["title"]
            news_description = article["description"]
            news_source = article["url"]

            if lang == "pt":
                # Condition not brazilian
                if (
                    news_title is not None
                    and ".br" not in news_source
                    and i <= news_limit
                ):
                    # News displayed in the email
                    news_total_i = f"{i}. {news_title} ({news_source})" + "\n"

                    # Sentiment analysis
                    # vibe = vibe_score_pt(news_title, news_description)
                    vibe = "⚪"

                    # Final outcome
                    news_total += f"{vibe} {news_total_i}"
                    i += 1
            elif lang == "en":
                # Condition of job
                if news_title is not None and i <= news_limit:
                    # News displayed in the email
                    news_total_i = f"{i}. {news_title} ({news_source})" + "\n"

                    # Sentiment analysis
                    vibe = vibe_score_en(news_title, news_description)

                    # Final outcome
                    news_total += f"{vibe} {news_total_i}"
                    i += 1
            else:
                break
        return news_total
    except Exception as e:
        print("The error is: ", e)
