# vectorizer

# imports
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd
import matplotlib.pyplot as plt

dtm_df = None
tfidf_df = None
top_count = None
top_sig = None

# double bar chart plot
def double_bar_plot():
    global top_count
    global top_sig

    print("Top count:\n", top_count)
    print("Top significant terms:\n", top_sig)

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))

    top_count.plot(kind="barh", ax=axes[0], color="skyblue")
    axes[0].set_title("DTM")
    axes[0].invert_yaxis()

    top_sig.plot(kind="barh", ax=axes[1], color="limegreen")
    axes[1].set_title("TF-IDF")
    axes[1].invert_yaxis()

    plt.tight_layout()
    plt.show()

# get the top 5 for count and significance
def top_stats():
    global dtm_df
    global tfidf_df
    global top_count
    global top_sig

    top_count = dtm_df.sum().sort_values(ascending=False).head(5)
    top_sig = tfidf_df.sum().sort_values(ascending=False).head(5)

# perform a term frequency-inverse document frequency calculation
def vectorizer_tfidf(df):
    global tfidf_df
    tv = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=.04)
    tfidf = tv.fit_transform(df)
    tfidf_df = pd.DataFrame(tfidf.toarray(), columns=tv.get_feature_names_out())

    # print("TF-IDF Vectorizer:\n", tfidf_df)

    return tfidf_df

# convert cleaned text from dataframe to document-term matrix
def vectorizer_dtm(df):
    global dtm_df
    print("vectorizer function")

    # create countvectorizer object
    cv = CountVectorizer(stop_words='english', ngram_range=(1, 2), min_df=.1, max_df=.8)
    dtm = cv.fit_transform(df)
    dtm_df = pd.DataFrame(dtm.toarray(), columns=cv.get_feature_names_out())

    print("DTM Vectorizer:\n", dtm_df)