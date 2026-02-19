# text_file.py

# import statements
import text_clean

# extract text file contents
def txt_extract(path):
    # print("txt_file function")

    # open text file to extract contents
    try:
        with open(path, "r") as f:
            text = f.read()
        print("text file content:\n", text)
    except FileNotFoundError:
        print("File not found")
        pass

    # convert list to string
    text = text_clean.list_to_str(text)
    # print("string from list:\n", text)

    # clean the text
    text = text_clean.clean_text(text)
    # print("cleaned text:\n", text)

    # convert string to dframe
    txt_dframe = text_clean.str_to_df(text, path)
    # print("txt dframe:\n", txt_dframe)

    # convert all characters to lowercase
    txt_dframe = text_clean.lower_dframe(txt_dframe)
    # print("lowercase dframe:\n", txt_dframe)

    # tokenize dataframe
    txt_dframe = text_clean.tokenize_dframe(txt_dframe)
    # print("tokenized dframe:\n", txt_dframe)

    # remove stop words from tokenized dataframe
    txt_dframe["no_stop"] = txt_dframe["tokens"].apply(text_clean.remove_stop_words_df)
    # print("no stop words dframe:\n", txt_dframe)

    # lemmatize and tokenize dframe contents
    txt_dframe["lemmas"] = txt_dframe["no_stop"].apply(text_clean.lemmatize_dframe)
    print("lemmatized dframe:\n", txt_dframe)

    # tag parts of speech
    txt_dframe["pos_tags"] = txt_dframe["no_stop"].apply(text_clean.pos_tags)
    # print("pos tags:\n", txt_dframe)