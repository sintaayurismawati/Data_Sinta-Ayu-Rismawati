import pandas as pd
import os

sentiment_csv = None
classified_data = None

# metodh load_data()
def load_data():
    global sentiment_csv
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data_source', 'file.csv')
    sentiment_csv = pd.read_csv(file_path,  index_col=0)

# method classify_sentiment()
def classify_sentiment():
    global sentiment_csv
    global classified_data
    classified_data = sentiment_csv.groupby('labels')

# method save_to_csv() ----> sentiment_good.csv, sentiment_bad.csv, sentiment_neutral.csv
def save_to_csv():
    global sentiment_csv
    global classified_data
    for label, group in classified_data:
        file_name = f"sentiment_{label}.csv"
        group.to_csv(file_name, index=False)

# method summarize_counts()---> sentiment_counts.csv
def summarize_counts():
    global sentiment_csv
    counts = sentiment_csv['labels'].value_counts().reset_index()
    counts.columns = ['label', 'count']
    counts.to_csv("sentiment_counts.csv", index=False)
    print("sentiment_counts.csv saved successfully.")

if __name__ == "__main__":
    load_data()
    classify_sentiment()
    save_to_csv()
    summarize_counts()