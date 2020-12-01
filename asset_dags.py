# airflow related
from airflow import models
from airflow import DAG

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from asset_inventory import run
from asset_inventory_deployment import run

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 8, 13),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "catchup": False,
}

dag = DAG("asset_dag", default_args=default_args, schedule_interval=timedelta(1))

asset_inventory = PythonOperator(
    task_id='asset_inventory',
    python_callable=run,
    op_args=['asset_inventory'],
    dag=dag)

asset_inventory_deployment = PythonOperator(
    task_id='asset_inventory_deployment',
    python_callable=run,
    op_args=['asset_inventory_deployment'],
    dag=dag)

asset_inventory >> asset_inventory_deployment