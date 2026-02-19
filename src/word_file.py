# word_file.py

# import statements
import text_clean
from docx import Document

# extract word file contents
def docx_extract(path):
    # print("docx_file function")
    document = Document(path)
    text = ""

    # Use for loop to parse through docx file by paragraph, then by line, and finally by word
    for para in document.paragraphs:
        lines_in_paragraph = para.text.splitlines()
        for line in lines_in_paragraph:
            # for word in line.split():
            text += line

    text = text.replace(". ", "\n")
    # print("text:\n", text)

    result = text_clean.process_text(text)
    print("Result:\n", result)

    # # clean the text
    # text = text_clean.clean_text(text)
    # # print("cleaned text:\n", text)
    #
    # # convert string to dframe
    # doc_dframe = text_clean.str_to_df(text, path)
    # # print("doc dframe:\n", doc_dframe)
    #
    # # convert all characters to lowercase
    # doc_dframe = text_clean.lower_dframe(doc_dframe)
    # # print("lowercase dframe:\n", doc_dframe)
    #
    # # tokenize dataframe
    # doc_dframe = text_clean.tokenize_dframe(doc_dframe)
    # # print("tokenized dframe:\n", doc_dframe)
    #
    # # remove stop words from tokenized dataframe
    # doc_dframe["no_stop"] = doc_dframe["tokens"].apply(text_clean.remove_stop_words_df)
    # # print("no stop words dframe:\n", doc_dframe)
    #
    # # lemmatize and tokenize dframe contents
    # doc_dframe["lemmas"] = doc_dframe["no_stop"].apply(text_clean.lemmatize_dframe)
    # print("lemmatized dframe:\n", doc_dframe)
    #
    # # tag parts of speech
    # doc_dframe["pos_tags"] = doc_dframe["no_stop"].apply(text_clean.pos_tags)
    # # print("pos tags:\n", doc_dframe)