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

    # # print("docx_file function")
    # document = Document(path)
    #
    # # Use for loop to parse through docx file by paragraph, then by line, and finally by word
    # for para in document.paragraphs:
    #     lines_in_paragraph = para.text.splitlines()
    #     for line in lines_in_paragraph:
    #         text += line
    #
    # # check for delimiters to more effectively split text
    #
    # text = re.sub(" {2,}", "\n", text)
    # text = text.replace(". ", "\n")
    # text = text.replace(", ", "\n")
    # # text = re.sub(", ", "\n", text)
    # print("Initial modifications:\n", text)