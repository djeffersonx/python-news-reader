import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

nltk.download('vader_lexicon')
nltk.download('stopwords')

text_classifications = [
  ('I love this sandwich.', 'pos'),
  ('this is an amazing place!', 'pos'),
  ('I feel very good about these beers.', 'pos'),
  ('this is my best work.', 'pos'),
  ("what an awesome view", 'pos'),
  ('I do not like this restaurant', 'neg'),
  ('I am tired of this stuff.', 'neg'),
  ("I can't deal with this", 'neg'),
  ('he is my sworn enemy!', 'neg'),
  ('my boss is horrible.', 'neg')
]

text_classifier = NaiveBayesClassifier(text_classifications)

def getTextAnalysis(text):
  tb_classification = TextBlob(text, classifier=text_classifier).classify()
  sia = SentimentIntensityAnalyzer()
  compound = sia.polarity_scores(text)['compound']

  print('Compound '+str(compound))
  print('Class '+str(tb_classification))
  
  if tb_classification =='pos' and compound > 60:
    return 'pos'
  elif tb_classification =='neg' and compound < -60:
    return 'neg'
  else:
    return 'ntr'

a = """
demission
"""

print(getTextAnalysis(a))