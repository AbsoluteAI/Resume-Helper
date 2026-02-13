# Resume Helper
# text_preprocessing.py

# Import statements
from docx import Document
from pypdf import PdfReader as pr
import re
import pandas as pd

# Function to clean text
def clean_text(text):
    pattern = r'[^a-zA-Z0-9,.-]'
    text = "".join(text)
    text = text.lower()
    text = re.sub(pattern, ' ', text)
    return text

# Function to transfer extracted list text to pd dataframe
def list_to_dframe(data):
    prep_data = data.split(", ")
    text_dframe = pd.DataFrame(prep_data)
    copy_dframe = text_dframe.copy()
    print(text_dframe)

# Function to parse word document
def docx_file(path):
    # Extract docx contents
    print("docx_file function")
    document = Document(path)
    extracted_text = ""

    # Use for loop to parse through docx file by paragraph, then by line, and finally by word
    for para in document.paragraphs:
        lines_in_paragraph = para.text.splitlines()
        for line in lines_in_paragraph:
            for word in line.split():
                extracted_text+=word
    # print(extracted_text)
    list_to_dframe(extracted_text)

def pdf_file(path):
    # Extract pdf file contents
    print("pdf_file function")
    reader = pr(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    # print(text)
    list_to_dframe(text)

def txt_file(path):
    # Extract txt file contents
    print("txt_file function")
    try:
        with open(path, "r") as f:
            content = f.read()
        # print(content)
        list_to_dframe(content)
    except FileNotFoundError:
        print("File not found")
        pass