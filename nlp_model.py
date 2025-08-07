# nlp_model.py

from textblob import TextBlob

def analyze_sentiment(message):
    blob = TextBlob(message)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"
