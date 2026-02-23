# naive_bayes_mod.py

# import statements
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import random
from collections import defaultdict
from pathlib import Path
import pandas as pd
import vectorizer_mod
import text_file

# xtrain will be tfidfvectorizer object
# ytrain will be corresponding data labels

def multinomial_nb():
    # sample data is in the df dataframe
    # choice_list = ["resume", "not a resume"]

    nb_dict = defaultdict(list)

    directory_path = Path("../docs")
    for file_path in directory_path.iterdir():
        if file_path.is_file():
            extracted_text = text_file.txt_extract(file_path)
            # random_choice = random.choice(choice_list)
            nb_dict["text"].append(extracted_text)
            # nb_dict["label"].append(random_choice)
            if "cover letter" in str(file_path):
                nb_dict["label"].append("cover letter")
            elif "resume" in str(file_path):
                nb_dict["label"].append("resume")

    df = pd.DataFrame(nb_dict)
    print("Initial Dataframe:\n", df)

    X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.1, random_state=42)

    cv = CountVectorizer()
    X_train_counts = cv.fit_transform(X_train)
    X_test_counts = cv.transform(X_test)

    mnb_classifier = MultinomialNB(alpha=0.1)
    mnb_classifier.fit(X_train_counts, y_train)
    predictions = mnb_classifier.predict(X_test_counts)

    print("Accuracy:\t", accuracy_score(y_test, predictions))
    print("Report:\n", classification_report(y_test, predictions, zero_division=0))