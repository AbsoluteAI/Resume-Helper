# Resume Helper
# text_preprocessing.py

# Import statements
from docx import Document
from pypdf import PdfReader as pr
import re

# Function to clean text
def clean_text(text):
    pattern = r'[^a-zA-Z0-9,.-]'
    text = text.lower()
    text = re.sub(pattern, ' ', text)
    text = " ".join(text.split())
    return text

# Function to parse word document
def docx_file(path):
    # Extract docx contents
    print("docx_file function")
    document = Document(path)
    extracted_text = []

    # Use for loop to parse through docx file by paragraph, then by line, and finally by word
    for para in document.paragraphs:
        lines_in_paragraph = para.text.splitlines()
        for line in lines_in_paragraph:
            for word in line.split():
                word = clean_text(word)
                extracted_text.append(word)
    extracted_text = " ".join(extracted_text)
    print(extracted_text)
    # return extracted_text

def pdf_file(path):
    # Extract pdf file contents
    print("pdf_file function")
    reader = pr(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    text = clean_text(text)
    print(text)
    pass

def txt_file(path):
    # Extract txt file contents
    print("txt_file function")
    try:
        with open(path, "r") as f:
            content = f.read()
            content = clean_text(content)
        print(content)
    except FileNotFoundError:
        print("File not found")
        pass