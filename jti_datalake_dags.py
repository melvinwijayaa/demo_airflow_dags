# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from asset_inventory import asset_inventory_function
from asset_inventory_deployment import asset_inventory_deployment_function
from personal import personal_function
from superior import superior_function
from jobactual import jobactual_function
from jobactualcomposite import jobactualcomposite_function

# import lithops function
#from jti_lithops_function import jti_lithops_function 

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 12, 1),
}

dag = DAG("asset_dag", default_args=default_args, schedule_interval=None)

asset_inventory = PythonOperator(
    task_id='asset_inventory',
    python_callable=asset_inventory_function,
    op_args=['asset_inventory'],
    dag=dag)

asset_inventory_deployment = PythonOperator(
    task_id='asset_inventory_deployment',
    python_callable=asset_inventory_deployment_function,
    op_args=['asset_inventory_deployment'],
    dag=dag)

personal = PythonOperator(
    task_id='personal',
    python_callable=personal_function,
    op_args=['personal'],
    dag=dag)

superior = PythonOperator(
    task_id='superior',
    python_callable=superior_function,
    op_args=['superior'],
    dag=dag)

jobactual = PythonOperator(
    task_id='jobactual',
    python_callable=jobactual_function,
    op_args=['jobactual'],
    dag=dag)

jobactualcomposite = PythonOperator(
    task_id='jobactualcomposite',
    python_callable=jobactualcomposite_function,
    op_args=['jobactualcomposite'],
    dag=dag)

#DummyOperator DAGS her
staging_done = DummyOperator('Staging_Done', dag= dag)

asset_inventory >> asset_inventory_deployment >> staging_done
personal >> staging_done
superior >> staging_done
jobactual >> jobactualcomposite >> staging_done
