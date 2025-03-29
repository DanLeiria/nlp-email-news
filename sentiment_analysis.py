import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# from pysentimiento import create_analyzer

try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

# NLP sentiment analysis - Only call it once
analyser_en = SentimentIntensityAnalyzer()


def vibe_score_en(news_title: str, news_description: str):
    """
    Sentiment analysis the english text (both title and description) using
    the package nltk.

    Parameters:
        - news_title (str): Title news
        - news_description (str): Descriptive text of the news
    Output:
        - Sentiment score as an emojis
    """

    # Add text together
    news_text = f"{news_title}: {news_description}"

    # Calculate the polarity scores
    result = analyser_en.polarity_scores(news_text)

    # Define the news sentiment
    if result["compound"] > 0.05:
        vibe = "🟢"
    elif result["compound"] < -0.05:
        vibe = "🔴"
    else:
        vibe = "🟡"
    return vibe


### Removed because it is too heavy in the server
# def vibe_score_pt(news_title: str, news_description: str):
#     # NLP sentiment analysis
#     analyser_pt = create_analyzer(task="sentiment", lang="pt")

#     # Add text together
#     news_text = f"{news_title}: {news_description}"

#     # Calculate the polarity scores
#     result = analyser_pt.predict(news_text)

#     # Define the news sentiment
#     if result.output == "POS":
#         vibe = "🟢"
#     elif result.output == "NEG":
#         vibe = "🔴"
#     else:
#         vibe = "🟡"
#     return vibe
