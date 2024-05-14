from datetime import datetime, timedelta
import random
import logging
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "sinta",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

def generate_random_numbers(ti):
    random_numbers = [random.randint(1, 50) for _ in range(25)]
    ti.xcom_push(key='random_numbers', value=random_numbers)
    logging.info(f"Generated numbers: {random_numbers}")

def calculate_sum(ti):
    random_numbers = ti.xcom_pull(key='random_numbers', task_ids='generate_random_numbers')
    total_sum = sum(random_numbers)
    ti.xcom_push(key='total_sum', value=total_sum)
    logging.info(f"Sum of numbers: {total_sum}")

def check_even_or_odd(ti):
    total_sum = ti.xcom_pull(key='total_sum', task_ids='calculate_sum')
    if total_sum % 2 == 0:
        logging.info("Even Sum")
    else:
        logging.info("Odd Sum")

with DAG(
    dag_id="random_numbers_workflow",
    default_args=default_args,
    description="A DAG to generate random numbers, sum them, and check if the sum is even or odd",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    
    generate_random_numbers_task = PythonOperator(
        task_id="generate_random_numbers",
        python_callable=generate_random_numbers,
    )

    calculate_sum_task = PythonOperator(
        task_id="calculate_sum",
        python_callable=calculate_sum,
    )

    check_even_or_odd_task = PythonOperator(
        task_id="check_even_or_odd",
        python_callable=check_even_or_odd,
    )

    generate_random_numbers_task >> calculate_sum_task >> check_even_or_odd_task