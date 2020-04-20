from textblob import TextBlob
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

class TextAnalyzer:

  trainClassifier = [
    # negatives
    ('bears increase', 'neg'),
    ('is bearish', 'neg'),
    ('negative perspective', 'neg'),
    ('billions loss', 'neg'),
    ('millions loss', 'neg'),
    ('stocks lower at close of trade', 'neg'),
    ('stock falls', 'neg'),

    # positives
    ('bulls increase', 'pos'),
    ('is bullish', 'pos'),
    ('positive perspective', 'pos'),
    ('billions gain', 'pos'),
    ('millions gain', 'pos'),
    ('stocks higher at close of trade', 'pos'),
    ('stock gains', 'pos'),
    ('stock rises', 'pos')

  ]

  textClassifier = NaiveBayesClassifier(trainClassifier)

  def getTextAnalysis(content):
    return TextBlob(content, classifier=TextAnalyzer.textClassifier).classify()