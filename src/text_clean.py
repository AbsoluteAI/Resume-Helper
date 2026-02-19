# Resume Helper
# py
from nltk import WhitespaceTokenizer

# Imports
import prompts
import re
import pandas as pd
import spacy
from nltk.corpus import stopwords

# global spacy load
nlp = spacy.load('en_core_web_sm')
# , disable=["parser", "ner"]

def create_df(text):
    df = pd.DataFrame(text.split("\n"))
    return df

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
def str_to_df(text):
    # print("string to df")
    df = create_df(text)
    max_columns()
    df.columns = ["text"]
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

def process_text(text):
    # clean the text
    text = clean_text(text)
    # print("cleaned text:\n", text)

    # convert string to dframe
    text_dframe = str_to_df(text)
    # print("text dframe:\n", text_dframe)

    # convert all characters to lowercase
    text_dframe = lower_dframe(text_dframe)
    # print("lowercase dframe:\n", text_dframe)

    # tokenize dataframe
    text_dframe = tokenize_dframe(text_dframe)
    # print("tokenized dframe:\n", text_dframe)

    # remove stop words from tokenized dataframe
    text_dframe["no_stop"] = text_dframe["tokens"].apply(remove_stop_words_df)
    # print("no stop words dframe:\n", text_dframe)

    # lemmatize and tokenize dframe contents
    text_dframe["lemmas"] = text_dframe["no_stop"].apply(lemmatize_dframe)
    # print("lemmatized dframe:\n", text_dframe)

    return text_dframe