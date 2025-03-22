from nltk.sentiment import SentimentIntensityAnalyzer
from pysentimiento import create_analyzer


# Create a sentiment analyzer for Portuguese
analyser_pt = create_analyzer(task="sentiment", lang="pt")
# Analyze a sentence
result = analyser_pt.predict("Este produto é neutro!")
print(result.output)  # "POS" => Positive
print(result.probas)  # Probabilities for POS, NEG, NEU


def vibe_score(news_title: str, news_description: str):
    # NLP sentiment analysis
    analyser_en = SentimentIntensityAnalyzer()
    analyser_pt = create_analyzer(task="sentiment", lang="pt")

    # Add text together
    news_text = f"{news_title}: {news_description}" + "\n"

    # Calculate the polarity scores
    analysis_output = analyser_en.polarity_scores(news_text)

    # Define the news sentiment
    if analysis_output["compound"] > 0.05:
        vibe = "🟢"
    elif analysis_output["compound"] < -0.05:
        vibe = "🔴"
    else:
        vibe = "🟡"
    return vibe


def news_loop(content: dict, lang: str, news_limit: int):
    """
    INPUT:
        - content: API news (dict)
        - lang: only 'en' or 'pt' (string)
        - news_limit: maximum number of news output (int)
    OUTPUT:
        - News list as a string.
    DESCRIPTION:
    Loop through the news extracted.
    In the loop:
        - Add news title and link source to send by email.
        - Portugal has a condition of rejecting brazilian news.
        - Filter number of news according to given limit.
        - Sentiment analysis of the title and description.
        - Sentiment score is added to email text as color emoji.
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
                    news_total += f"{i}. {news_title} ({news_source})" + "\n"
                    i += 1
            elif lang == "en":
                # Condition of job
                if news_title is not None and i <= news_limit:
                    # News displayed in the email
                    news_total_i = f"{i}. {news_title} ({news_source})" + "\n"

                    # Sentiment analysis
                    vibe = vibe_score(news_title, news_description)

                    # Final outcome
                    news_total += f"{vibe} {news_total_i}"
                    i += 1
            else:
                break
        return news_total
    except Exception as e:
        print("The error is: ", e)
