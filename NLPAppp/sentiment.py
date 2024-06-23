import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon if not already downloaded
#nltk.download('vader_lexicon')


def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)

    # Determine sentiment
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, sentiment_scores

