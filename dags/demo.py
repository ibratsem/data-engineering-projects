from datetime import datetime
import logging
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# Set up logging format
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Define the DAG
with DAG(
    dag_id="demo",
    start_date=datetime(2022, 1, 1),  # The start date for the DAG
    schedule="40 * * * *",  # Run at the 40th minute of every hour
    catchup=False  # Prevent backfilling
) as dag:
    
    # Define the BashOperator task
    hello = BashOperator(
        task_id="hello", 
        bash_command="echo hello", 
        do_xcom_push=True  # Enable XCom to push the result of the bash command
    )

    # Define a Python task using the @task decorator
    @task()
    def airflow(hello_output):
        logging.info(f"Hello output: {hello_output}")
        return "airflow"

    # Set the task dependencies
    hello_output = hello.output  # Capture the output of the `hello` task
    hello >> airflow(hello_output=hello_output)

