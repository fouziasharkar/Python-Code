from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def text_summarization(text):

    # Initialize the parser and tokenizer
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Initialize LSA (Latent Semantic Analysis) summarizer
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=3)  # Specify the number of sentences in the summary

    # Print the summarized sentences
    l=[]
    for sentence in summary:
        l.append(sentence)

    return l









