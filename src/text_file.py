# text_file.py

# import statements
import text_clean
import vectorizer_mod

# capture the unprocessed txt text
text = ""

# extract text file contents
def txt_extract(path):
    global text
    # print("txt_file function")

    # open text file to extract contents
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found")
        pass

    return text