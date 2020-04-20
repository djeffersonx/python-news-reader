import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('wordnet')

def getTextAnalysis(text):
  sia = SentimentIntensityAnalyzer()
  return sia.polarity_scores(text)