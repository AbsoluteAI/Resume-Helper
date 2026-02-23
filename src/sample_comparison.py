# sample_comparison.py
# smaller dataset: naive bayes
# use tfidvectorizer for most significant words

# import statements
from pathlib import Path
import pandas as pd
import text_file
import text_clean
import vectorizer_mod

# prep the text of each resume and turn it into a tf-idf dataframe for classification
def resume_sample_conversion(file_path):
    extracted_text = text_file.txt_extract(file_path)
    sample_df = text_clean.process_text(extracted_text)
    sample_count_df = vectorizer_mod.vectorizer_dtm(sample_df["lemmas"])
    sample_tfidf_df = vectorizer_mod.vectorizer_tfidf(sample_df["lemmas"])

    # print("Sample count:\n", sample_count_df)
    # print(f"Sample Text:\nFilepath {file_path}\n{sample_tfidf_df}")

    return sample_count_df, sample_tfidf_df

# goes through each resume in /docs one at a time
def resume_sample_process():
    directory_path = Path("../docs")
    sample_count_list = []
    sample_tfidf_list = []

    for file_path in directory_path.iterdir():
        if file_path.is_file():
            # print("Resume:", file_path.name)
            sample_count_df, sample_tfidf_df = resume_sample_conversion(file_path)
            sample_count_list.append(sample_count_df)
            sample_tfidf_list.append(sample_tfidf_df)

    combined_sample_count = pd.concat(sample_count_list, ignore_index=True)
    combined_sample_count = combined_sample_count.dropna(how='all')
    # print("Combined sample count:\n", combined_sample_count)

    combined_sample_sig = pd.concat(sample_tfidf_list, ignore_index=True)
    combined_sample_sig = combined_sample_sig.dropna(how='all')
    # print("Combined sample significance:\n", combined_sample_sig)

    top10_count = combined_sample_count.sum().sort_values(ascending=False).head(10)
    # print("Top 10 most frequent words:\n", top10_count)

    top10_sig_words = combined_sample_sig.sum().sort_values(ascending=False).head(10)
    # print("Top 10 most significant words:\n", top10_sig_words)

    vectorizer_mod.sample_comparison(top10_count, top10_sig_words)

    # print(combined_sample_sig.shape)