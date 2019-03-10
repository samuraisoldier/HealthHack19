from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

text = input("How are you feeling? ")

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print(sentence, "\n", score)

print(sentiment_analyzer_scores(text))
