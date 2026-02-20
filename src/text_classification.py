# text_classification.py
# smaller dataset: naive bayes
# use tfidvectorizer for most significant words

# import statements
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from pathlib import Path
import pandas as pd
import text_file
import text_clean
import vectorizer_mod

# xtrain will be tfidfvectorizer object
# ytrain will be corresponding data labels
def multinomial_nb(df):
    nb_model = MultinomialNB()
    nb_model.fit(X_train, y_train)
    nb_pred = nb_model.predict(X_test)

# prep the text of each resume and turn it into a tf-idf dataframe for classification
def resume_sample_conversion(file_path):
    extracted_text = text_file.txt_extract(file_path)
    sample_df = text_clean.process_text(extracted_text)
    sample_tfidf_df = vectorizer_mod.vectorizer_tfidf(sample_df["lemmas"])

    print(f"Sample Text:\nFilepath {file_path}\n{sample_tfidf_df}")

    return sample_tfidf_df

# goes through each resume in /docs one at a time
def resume_sample_process():
    directory_path = Path("../docs")
    sample_df_list = []

    for file_path in directory_path.iterdir():
        if file_path.is_file():
            # print("Resume:", file_path.name)
            sample_df = resume_sample_conversion(file_path)
            sample_df_list.append(sample_df)

    combined_sample_df = pd.concat(sample_df_list, ignore_index=True)
    combined_sample_df = combined_sample_df.dropna(how='all')
    print("Full sample df:\n", combined_sample_df)

    top50_sig_words = combined_sample_df.sum().sort_values(ascending=False).head(50)
    print("Top 50 most significant words:\n", top50_sig_words)

    print(combined_sample_df.shape)