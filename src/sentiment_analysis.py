# sentiment_analysis.py
from matplotlib import pyplot as plt
# import statements
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import seaborn as sns
import numpy as np
import math

def prep_heatmap_data(arr):
    elements = arr.size

    sqrt_size = math.sqrt(elements)

    rows = int(math.ceil(sqrt_size))
    cols = int(elements / rows)

    while rows * cols != elements:
        rows -= 1
        cols = int(elements / rows)

    return np.reshape(arr, (rows, cols))


# create a heatmap for positive and negative sentiments
def heatmap_chart(df):
    # pos_array = positive_df[["sentiment"]].to_numpy()
    # neg_array = negative_df[["sentiment"]].to_numpy()

    # pos_matrix = prep_heatmap_data(pos_array)
    # neg_matrix = prep_heatmap_data(neg_array)

    df = df.sort_values(ascending=False)

    df = df.to_numpy()
    matrix = prep_heatmap_data(df)

    sns.heatmap(matrix, annot=False, cmap="plasma", center=0, vmin=-1, vmax=1)
    plt.title("Sentiment Analysis")
    plt.show()

    # sns.heatmap(neg_matrix, annot=True, cmap="coolwarm", center=0, vmin=-1, vmax=1)
    # plt.title("Sentiment Analysis")
    # plt.xlabel("Sentiment")
    # plt.ylabel("blank")
    # plt.show()

def sentiment_sort(df):
    positive_df = df[["text", "sentiment"]].sort_values(by="sentiment", ascending=False).head(25)
    negative_df = df[["text", "sentiment"]].sort_values(by="sentiment").head(25)

    print("\nMost positive:\n", positive_df)
    print("\nMost negative:\n", negative_df)

    # heatmap_chart(positive_df, negative_df)

# function for sentiment analysis
def sentiment_analysis(df):
    analyzer = SentimentIntensityAnalyzer()
    analyzer.polarity_scores(df)

    composite_sentiment = analyzer.polarity_scores(df)["compound"]

    return composite_sentiment