from nltk.sentiment import SentimentIntensityAnalyzer
# from pysentimiento import create_analyzer


def vibe_score_en(news_title: str, news_description: str):
    # NLP sentiment analysis
    analyser_en = SentimentIntensityAnalyzer()

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
