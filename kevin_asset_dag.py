# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

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

dag = DAG("kevin_asset_dag", default_args=default_args, schedule_interval=None)

ASSET = PythonOperator(
    task_id='asset_inventory',
    python_callable=asset_inventory_function,
    op_args=['asset_inventory'],
    dag=dag)

ASSETINVENT = PythonOperator(
    task_id='asset_inventory_deployment',
    python_callable=asset_inventory_deployment_function,
    op_args=['asset_inventory_deployment'],
    dag=dag)

PERSONAL = PythonOperator(
    task_id='asset_inventory_deployment',
    python_callable=asset_inventory_deployment_function,
    op_args=['asset_inventory_deployment'],
    dag=dag)

SUPERIOR = PythonOperator(
    task_id='asset_inventory_deployment',
    python_callable=asset_inventory_deployment_function,
    op_args=['asset_inventory_deployment'],
    dag=dag)

JOBACTUAL = PythonOperator(
    task_id='asset_inventory_deployment',
    python_callable=asset_inventory_deployment_function,
    op_args=['asset_inventory_deployment'],
    dag=dag)

JOBACTUALCOMP = PythonOperator(
    task_id='asset_inventory_deployment',
    python_callable=asset_inventory_deployment_function,
    op_args=['asset_inventory_deployment'],
    dag=dag)

STAGING_DONE = PythonOperator(
    task_id='asset_inventory_deployment',
    python_callable=asset_inventory_deployment_function,
    op_args=['asset_inventory_deployment'],
    dag=dag)

ASSET >> ASSETINVENT >> [PERSONAL, SUPERIOR] >> JOBACTUAL >> JOBACTUALCOMP >> STAGING_DONE
 
