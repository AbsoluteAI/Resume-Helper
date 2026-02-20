# sentiment_analysis.py

# import statements
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_sort(df):
    print("\nMost positive:\n", df[["text", "sentiment"]].sort_values(by="sentiment", ascending=False).head(10))
    print("\nMost negative:\n", df[["text", "sentiment"]].sort_values(by="sentiment").head(10))

# function for sentiment analysis
def sentiment_analysis(df):
    analyzer = SentimentIntensityAnalyzer()
    analyzer.polarity_scores(df)

    composite_sentiment = analyzer.polarity_scores(df)["compound"]

    return composite_sentiment