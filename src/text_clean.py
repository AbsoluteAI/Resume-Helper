# Resume Helper
# text_clean.py
from nltk import WhitespaceTokenizer

# Imports
import prompts
import re
import pandas as pd
import spacy
from nltk.corpus import stopwords

# global spacy load
nlp = spacy.load('en_core_web_sm', disable=["parser", "ner"])

# converts all string text to lowercase
def lower_text(text):
    # print("Lower text function")
    return text.lower()

# join comma separated values
def remove_separators(text):
    # print("remove_separators function")
    text = "".join(text)
    return text

# converts string to list
def str_to_list(text):
    # print("Text to list function")
    return text.split()

# converts list to string
def list_to_str(list_of_text):
    # print("List to text function")
    return " ".join(list_of_text)

def create_newline(text):
    print("create new line")
    text = text.replace(" ", "\n")
    return text

def dframe_lists_to_strings(dframe):
    dframe = " ".join(dframe)
    return dframe

# show max dframe columns
def max_columns():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)

# tag parts of speech
def pos_tags(pos_text):
    pos_text = dframe_lists_to_strings(pos_text)
    doc = nlp(pos_text)
    return [(token.text, token.pos_) for token in doc]

# lemmatize dataframe
def lemmatize_dframe(lemma_text):
    lemma_text = dframe_lists_to_strings(lemma_text)
    doc = nlp(lemma_text)
    lemmatized_text = [token.lemma_ for token in doc]
    # print("lemmatized text: ", lemmatized_text)
    return lemmatized_text

# remove stop words from dataframe with nltk
def remove_stop_words_df(text):
    stop_words = set(stopwords.words('english'))
    return [w for w in text if w.lower() not in stop_words]

# tokenize dataframe
def tokenize_dframe(df):
    df["tokens"] = df["text"].str.split()
    return df

# converts all dframe text to lowercase
def lower_dframe(dframe):
    dframe["text"] = dframe["text"].str.lower()
    return dframe

# converts string contents to dataframes
def str_to_df(text, path):
    # print("string to df")
    if path.endswith(".docx"):
        df = pd.DataFrame(text.split(","))
        max_columns()
        df.columns = ["text"]
        # print("docx dframe:\n", df)
        return df
    elif path.endswith(".pdf"):
        df = pd.DataFrame(text.split("\n"))
        max_columns()
        df.columns = ["text"]
        # print("pdf dframe:\n", df)
        return df
    elif path.endswith(".txt"):
        df = pd.DataFrame(text.split("\n"))
        max_columns()
        df.columns = ["text"]
        # print("text dframe:\n", df)
        return df

# remove misc characters from string text
def clean_text(text):
    # print("clean_text function")
    pattern = r'[^a-zA-Z0-9\n]'
    text = re.sub(pattern, ' ', text)
    text = re.sub(" {2,}", " ", text)
    return text

# def pkl_save(doc):
#     file_extension = prompts.file_extension
#     df = pd.DataFrame(doc)
#     df_other = df.pivot(index="word", columns="words", values="value")
#     print(df_other)
#     # print(df)
#     # df.to_pickle(f"{file_extension} resume.pkl")