from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

# Sample text
#text1 = ""

# Create a TextBlob object
#blob = TextBlob(text1, np_extractor=ConllExtractor())

# Extract noun phrases (which can include named entities)
#noun_phrases = blob.noun_phrases

#print("Noun phrases (potential named entities) in the text:")
#for np in noun_phrases:
    #print(np)


def ner_analysis(text1):
    # Create a TextBlob object
    blob = TextBlob(text1, np_extractor=ConllExtractor())

    # Extract noun phrases (which can include named entities)
    noun_phrases = blob.noun_phrases

    l = []
    for np in noun_phrases:
        l.append(np)

    return l


