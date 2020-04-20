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
(Reuters) - U.S. car rental company Hertz Global Holdings Inc (N:HTZ) said on Monday it plans to lay off 10,000 employees across its North America operations to cut costs amid the economic fallout of the COVID-19 pandemic.
Hertz had about 38,000 employees as of Dec. 31, 2019, of which 29,000 were at its U.S. operations.
The company, which counts billionaire investor Carl Icahn as its largest shareholder, will incur employee termination costs of about $30 million, it said in a regulatory filing. (https://
The terminations were effective April 14 for non-union employees and effective April 21 for union employees, the company said.
Late last month, Hertz said it was implementing furlough programs across its North America operations to cope with slowing demand for its services. (https://
"Like the rest of the global travel sector, COVID-19's impact on Hertz arrived swiftly, and the reversal in customer demand has been significant," Chief Executive Officer Kathryn Marinello said in March.
The company also said last month it hoped to bring back as many team members as possible once global travel rebounds.
"""

print(getTextAnalysis(a))