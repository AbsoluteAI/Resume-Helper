# Resume Suggestions
# prompts.py

# Import statements
import file_selector
import text_preprocessing

file_extension = ""

# Function to determine file type
def file_type(path):
    global file_extension
    # Determine file type
    if path.endswith(".docx"):
        print("docx file extension recognized")
        file_extension = "docx"
        text_preprocessing.docx_file(path)
    elif path.endswith(".pdf"):
        print("pdf file extension recognized")
        file_extension = "pdf"
        text_preprocessing.pdf_file(path)
    elif path.endswith(".txt"):
        print("txt file extension recognized")
        file_extension = "txt"
        text_preprocessing.txt_file(path)
    else:
        print("File type not recognized")
        pass

# Function to welcome user and provide options
def main_menu():
    print("Welcome to Resume Helper!\n")
    start_upload = input("Would you like to start upload? (y/n): ")
    if start_upload.lower() == "y":
        file_path = file_selector.select_file()
        file_type(file_path)
        print("file_path: ", file_path)
    elif start_upload.lower() == "n":
        pass