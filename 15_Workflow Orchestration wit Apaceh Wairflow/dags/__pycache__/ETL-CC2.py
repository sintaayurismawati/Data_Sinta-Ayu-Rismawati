from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='ETL-CC2',
    default_args=default_args,
    description='A pipeline to run Jupyter notebooks sequentially using BashOperator',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 5, 20),
    catchup=False,
) as dag:

    run_data_ingestion = BashOperator(
        task_id='run_data_ingestion',
        bash_command='jupyter nbconvert --execute /path/to/data_ingestion.ipynb'
    )

    run_data_transformation = BashOperator(
        task_id='run_data_transformation',
        bash_command='jupyter nbconvert --execute /path/to/data_transformation.ipynb'
    )

    run_data_load = BashOperator(
        task_id='run_data_load',
        bash_command='jupyter nbconvert --execute /path/to/data_load.ipynb'
    )

    run_data_ingestion >> run_data_transformation >> run_data_load
