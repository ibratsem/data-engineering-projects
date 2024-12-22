from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

def print_hello():
    logging.info("Hello, Airflow!")

with DAG('simple_dag', start_date=datetime(2024, 12, 21), schedule_interval=None) as dag:
    PythonOperator(task_id='print_hello_task', python_callable=print_hello)