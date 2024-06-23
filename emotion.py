'''
import nltk
from textblob import TextBlob


# Download 'punkt' from NLTK
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')

def analyze_emotion(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0.2:
        emotion1 = 'joy'
    elif sentiment < -0.2:
        emotion1 = 'sadness'
    else:
        emotion1 = 'neutral'
    return emotion1, sentiment

'''

import nlpcloud

client = nlpcloud.Client("distilbert-base-uncased-emotion", "be1d79c282a3f9dcede2cc35f66a15452ebe3d9e", gpu=False)
