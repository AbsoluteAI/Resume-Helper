# word_file.py

# import statements
import text_clean
import vectorizer_mod
from docx import Document

# capture the unprocessed docx text
text = ""

# extract word file contents
def docx_extract(path):
    global text
    # print("docx_file function")
    document = Document(path)

    # Use for loop to parse through docx file by paragraph, then by line, and finally by word
    for para in document.paragraphs:
        lines_in_paragraph = para.text.splitlines()
        for line in lines_in_paragraph:
            text += line

    # check for delimiters to more effectively split text

    return text