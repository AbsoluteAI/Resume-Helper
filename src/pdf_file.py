# pdf_file.py
from sklearn.feature_extraction.text import CountVectorizer

# import statements
import text_clean
import vectorizer_mod
import pymupdf

# capture the unprocessed pdf text
text = ""

# extract pdf file contents
def pdf_extract(path):
    global text
    # print("pdf_file function")
    # print("file path: ", path)
    doc = pymupdf.open(path)

    # for loop to parse pdf contents
    for page in doc:
        text += page.get_text()
    doc.close()

    return text