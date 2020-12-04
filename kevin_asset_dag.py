# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from ASSET import ASSET_function
from ASSETINVENT import ASSETINVENT_function
from PERSONAL import PERSONAL_function
from SUPERIOR import SUPERIOR_function
from JOBACTUAL import JOBACTUAL_function
from JOBACTUALCOMP import ASSETINVENT_function
from STAGING_DONE import STAGING_DONE



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
 
