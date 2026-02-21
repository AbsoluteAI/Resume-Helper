# Resume Suggestions
# prompts.py

# Import statements
import file_selector
import word_file
import pdf_file
import text_file
import text_clean
import vectorizer_mod
import sentiment_analysis
import nlp_ml_mod
import text_classification

file_extension = ""
raw_text = ""
text_dataframe = None

# Function to determine file type
def file_type(path):
    global file_extension
    global raw_text
    # Determine file type
    if path.endswith(".docx"):
        print("docx file extension recognized\nLoading contents...")
        file_extension = "docx"
        raw_text = word_file.docx_extract(path)
    elif path.endswith(".pdf"):
        print("pdf file extension recognized\nLoading contents...")
        file_extension = "pdf"
        raw_text = pdf_file.pdf_extract(path)
    elif path.endswith(".txt"):
        print("txt file extension recognized\nLoading contents...")
        file_extension = "txt"
        raw_text = text_file.txt_extract(path)
    else:
        print("File type not recognized")
        pass

# Function to welcome user and provide options
def main_menu():
    global raw_text
    global text_dataframe
    print("Welcome to Resume Helper!\n")

    while True:
        print("\n--- Main Menu ---\n")
        print("1. Upload resume")
        print("2. View resume stats")
        print("3. Sentiment analysis")
        print("4. Text classification")
        print("5. Exit")
        choice = input("\nEnter your choice: ")

        match choice:
            case "1":
                file_path = file_selector.select_file()
                file_type(file_path)
                print("File contents:\n", raw_text)
                print("Cleaning file contents...")
                text_dataframe = text_clean.process_text(raw_text)
                print("Text processing complete...\n", text_dataframe)
            case "2":
                if text_dataframe is None:
                    print("No resume loaded...")
                else:
                    print("Processing resume statistics...")
                    vectorizer_mod.vectorizer_dtm(text_dataframe["lemmas"])
                    vectorizer_mod.vectorizer_tfidf(text_dataframe["lemmas"])
                    vectorizer_mod.top_stats()
                    vectorizer_mod.double_bar_plot()
            case "3":
                if text_dataframe is None:
                    print("No resume loaded...")
                else:
                    print("Initiating sentiment analysis...")
                    text_dataframe["sentiment"] = text_dataframe.text.apply(sentiment_analysis.sentiment_analysis)
                    print("Sentiment analysis complete...\n", text_dataframe[["text", "sentiment"]])
                    sentiment_analysis.sentiment_sort(text_dataframe)
            case "4":
                if text_dataframe is None:
                    print("No resume loaded...")
                else:
                    text_classification.resume_sample_process()
            case "5":
                break
            case _:
                print("Invalid choice")