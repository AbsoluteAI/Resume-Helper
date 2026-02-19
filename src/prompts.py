# Resume Suggestions
# prompts.py

# Import statements
import file_selector
import word_file
import pdf_file
import text_file

file_extension = ""

# Function to determine file type
def file_type(path):
    global file_extension
    # Determine file type
    if path.endswith(".docx"):
        print("docx file extension recognized\nLoading contents...")
        file_extension = "docx"
        word_file.docx_extract(path)
    elif path.endswith(".pdf"):
        print("pdf file extension recognized\nLoading contents...")
        file_extension = "pdf"
        pdf_file.pdf_extract(path)
    elif path.endswith(".txt"):
        print("txt file extension recognized\nLoading contents...")
        file_extension = "txt"
        text_file.txt_extract(path)
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
        # print("file_path: ", file_path)
    elif start_upload.lower() == "n":
        pass