from pymysql import connect
import pandas as pd
import os

connection = connect(
    host='localhost',
    db='sentiment_chatgpt',
    user='root',
    password='',
    port=3307
)

cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE sentiments (sentiment_id INT PRIMARY KEY, sentiment_label VARCHAR(10))')
    cursor.execute('INSERT INTO sentiments (sentiment_id, sentiment_label) values (1,"neutral"), (2,"good"), (3,"bad")')
    cursor.execute('CREATE TABLE tweets (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(100), sentiment_id INT, FOREIGN KEY(sentiment_id) REFERENCES sentiments(sentiment_id))')

def insert_from_csv():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data_source', 'file.csv')
    sentiment_csv = pd.read_csv(file_path,  index_col=0)

    for index, row in sentiment_csv.iterrows():
        if row.iloc[1]=='neutral':
            sentiment_id = 1
        elif row.iloc[1]=='good':
            sentiment_id = 2
        elif row.iloc[1]=='bad':
            sentiment_id = 3
        cursor.execute('INSERT INTO tweets (text, sentiment_id) VALUES (%s, %s)', (row['tweets'], sentiment_id))

create_table()
insert_from_csv()

connection.commit()
connection.close()