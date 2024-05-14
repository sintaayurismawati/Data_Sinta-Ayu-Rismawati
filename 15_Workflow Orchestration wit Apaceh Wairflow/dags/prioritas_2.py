from datetime import datetime, timedelta
import requests
import csv
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "sinta",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

def fetch_data_from_api():
    api_url = "https://fakestoreapi.com/products"
    response = requests.get(api_url)
    return response.json()

def write_to_csv(**kwargs):
    products = kwargs["ti"].xcom_pull(task_ids="fetch_data_from_api")
    with open("/tmp/products.csv", "w", newline="") as csvfile:
        fieldnames = products[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def write_to_txt(**kwargs):
    products = kwargs["ti"].xcom_pull(task_ids="fetch_data_from_api")
    with open("/tmp/products.txt", "w") as txtfile:
        for product in products:
            txtfile.write(str(product) + "\n")

with DAG(
    "fetch_api_data_and_write_to_files",
    default_args=default_args,
    description="A DAG to fetch data from API and write to CSV and TXT files",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    fetch_data_from_api_task = PythonOperator(
        task_id="fetch_data_from_api",
        python_callable=fetch_data_from_api
    )

    write_to_csv_task = PythonOperator(
        task_id="write_to_csv",
        python_callable=write_to_csv
    )

    write_to_txt_task = PythonOperator(
        task_id="write_to_txt",
        python_callable=write_to_txt
    )

    done_message_task = BashOperator(
        task_id="done_message",
        bash_command='echo "done!"'
    )

    fetch_data_from_api_task >> [write_to_csv_task, write_to_txt_task] >> done_message_task
