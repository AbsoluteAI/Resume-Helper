# word_file.py

# import statements
import text_clean
import vectorizer_mod
from docx import Document
import docx2txt
import re

# capture the unprocessed docx text
text = ""

# extract word file contents
def docx_extract(path):
    global text

    init_path = path

    word_file = path
    text = docx2txt.process(word_file)

    txt_file = path.replace(".docx", ".txt")

    with open(txt_file, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"{init_path} to {txt_file}:\n", text)

    return text