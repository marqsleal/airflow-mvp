from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import requests
import csv
import os

def extract_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data

def transform_data(ti):
    data = ti.xcom_pull(task_ids='extract_data')
    transformed_data = {'bitcoin': data['bitcoin']['usd'] * 5.2}  # Exemplo de transformação
    return transformed_data

def load_data(ti):
    transformed_data = ti.xcom_pull(task_ids='transform_data')
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, 'airflow_bitcoin')
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    file_path = os.path.join(target_dir, 'bitcoin_price.csv')
    
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['currency', 'price_in_brl'])
        writer.writerow(['bitcoin', transformed_data['bitcoin']])

default_args = {
    'start_date': datetime(2023, 9, 1),
}

with DAG('simple_etl', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    extract >> transform >> load
