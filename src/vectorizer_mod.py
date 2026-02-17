# vectorizer
# option to remove stop words in CountVectorizer instead of spacy if necessary

# imports
from sklearn.feature_extraction.text import CountVectorizer
import text_clean

def vectorizer_func(text):
    print("vectorizer function")
    cv = CountVectorizer()
    cv.fit_transform(text)