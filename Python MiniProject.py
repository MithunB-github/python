from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

Sentences=["You are a loser but you play a good game"]

analyzer=SentimentIntensityAnalyzer()

for sentence in Sentences:
    a=analyzer.polarity_scores(sentence)
    
    print("{:-<65} {}".format(sentence,str(a)))