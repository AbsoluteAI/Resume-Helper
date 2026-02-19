# pdf_file.py

# import statements
import text_clean
import pymupdf

# extract pdf file contents
def pdf_extract(path):
    # print("pdf_file function")
    # print("file path: ", path)
    doc = pymupdf.open(path)
    text = ""

    # for loop to parse pdf contents
    for page in doc:
        text += page.get_text()
    doc.close()
    # print("pdf contents:\n", text)

    # clean the text
    text = text_clean.clean_text(text)
    # print("cleaned text:\n", text)

    # convert string to dframe
    pdf_dframe = text_clean.str_to_df(text, path)
    # print("pdf dframe:\n", pdf_dframe)

    # convert all characters to lowercase
    pdf_dframe = text_clean.lower_dframe(pdf_dframe)
    # print("lowercase dframe:\n", pdf_dframe)

    # tokenize dataframe
    pdf_dframe = text_clean.tokenize_dframe(pdf_dframe)
    # print("tokenized dframe:\n", pdf_dframe)

    # remove stop words from tokenized dataframe
    pdf_dframe["no_stop"] = pdf_dframe["tokens"].apply(text_clean.remove_stop_words_df)
    # print("no stop words dframe:\n", pdf_dframe)

    # lemmatize and tokenize dframe contents
    pdf_dframe["lemmas"] = pdf_dframe["no_stop"].apply(text_clean.lemmatize_dframe)
    print("lemmatized dframe:\n", pdf_dframe)

    # tag parts of speech
    pdf_dframe["pos_tags"] = pdf_dframe["no_stop"].apply(text_clean.pos_tags)
    # print("pos tags:\n", pdf_dframe)