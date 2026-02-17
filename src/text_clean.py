# Resume Helper
# text_clean.py

# Imports
import prompts
from docx import Document
import pymupdf
import re
import pandas as pd
from io import StringIO
import spacy
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import vectorizer_mod
# nltk.download('punkt_tab')
# nltk.download('wordnet')
# nltk.download('stopwords')

# Function to clean text
def lower_text(text):
    # print("Lower text function")
    return text.lower()

def remove_separators(text):
    # print("remove_separators function")
    text = ", ".join(text)
    return text

def text_to_list(text):
    # print("Text to list function")
    return text.split()

def list_to_text(list_of_text):
    # print("List to text function")
    return " ".join(list_of_text)

def str_to_df(text):
    df = pd.read_csv(StringIO(text), sep=" ")
    print(df)

# def pkl_save(doc):
#     file_extension = prompts.file_extension
#     df = pd.DataFrame(doc)
#     df_other = df.pivot(index="word", columns="words", values="value")
#     print(df_other)
#     # print(df)
#     # df.to_pickle(f"{file_extension} resume.pkl")

def clean_text(text):
    # print("clean_text function")
    text = list_to_text(text)
    text = lower_text(text)
    pattern = r'[^a-zA-Z0-9]'
    text = re.sub(pattern, ' ', text)
    return text

def filter_nouns(text):
    # print("Filter nouns function")
    nouns = [token.text for token in text if token.pos_ in ['NOUN', 'PROPN']]
    print("Nouns:\n", nouns)

def filter_verbs(text):
    # print("Filter verbs function")
    verbs = [token.text for token in text if token.pos_ in 'VERB']
    print("Verbs:\n", verbs)

def filter_adjectives(text):
    # print("Filter adjectives function")
    adjectives = [token.text for token in text if token.pos_ in 'ADJ']
    print("adjectives:\n", adjectives)

def filter_numbers(text):
    # print("Filter numbers function")
    numbers = [token.text for token in text if token.pos_ in 'NUMBER']
    print("numbers:\n", numbers)

def filter_misc(text):
    # print("Filter misc function")
    misc = [token.text for token in text if token.pos_ in 'X']
    print("misc:\n", misc)

def spacy_pos(text):
    # Create spacy doc for parts of speech
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    print(doc)

    str_to_df(doc.text)

    # vectorizer_mod.vectorizer_func(doc)

    # pkl_save(doc)

    # print("Tokens:\n", [(token.text, token.pos_) for token in doc])
    # filter_nouns(doc)
    # filter_verbs(doc)
    # filter_adjectives(doc)
    # filter_numbers(doc)
    # filter_misc(doc)

def remove_stopwords(text):
    # print("Remove stopwords function")
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [word for word in text if word.lower() not in stop_words]
    return filtered_sentence

# Process text with spacy
def text_preprocessing(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    # print(lemmatized_tokens)

    no_stop = remove_stopwords(lemmatized_tokens)
    no_stop = list_to_text(no_stop)
    # print("No stopwords:\n", no_stop)

    spacy_pos(no_stop)

# Extract word file contents
def docx_file(path):
    # print("docx_file function")
    document = Document(path)
    extracted_text = []

    # Use for loop to parse through docx file by paragraph, then by line, and finally by word
    for para in document.paragraphs:
        lines_in_paragraph = para.text.splitlines()
        for line in lines_in_paragraph:
            for word in line.split():
                extracted_text.append(word)
    # print(extracted_text)
    text_preprocessing(clean_text(extracted_text))

# Extract pdf file contents
def pdf_file(path):
    # print("pdf_file function")
    doc = pymupdf.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    text = text_to_list(text)
    text_preprocessing(clean_text(text))

# Extract text file contents
def txt_file(path):
    # print("txt_file function")
    try:
        with open(path, "r") as f:
            content = f.read()
        # print(content)
        content = text_to_list(content)
        text_preprocessing(clean_text(content))
    except FileNotFoundError:
        print("File not found")
        pass