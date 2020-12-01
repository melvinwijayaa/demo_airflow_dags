# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from asset_inventory import connect
from asset_inventory_deployment import connect

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 12, 1),
}

dag = DAG("asset_dag", default_args=default_args, schedule_interval=None)

asset_inventory = PythonOperator(
    task_id='asset_inventory',
    python_callable=connect(),
    tablename='asset_inventory',
    dag=dag)

asset_inventory_deployment = PythonOperator(
    task_id='asset_inventory_deployment',
    python_callable=connect(),
    tablename='asset_inventory_deployment',
    dag=dag)

asset_inventory >> asset_inventory_deployment
