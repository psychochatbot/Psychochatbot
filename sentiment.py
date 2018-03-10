import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
  
hotel_rev = ["I hate studies",
"I am in a really bad mood",
"Nobody supports me in what I want to do",
"I will never be successful"]
  
sid = SentimentIntensityAnalyzer()
for sentence in hotel_rev:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
     	print((k, ss[k]))
        print('{0}: {1}, '.format(k, ss[k]))
     print()
