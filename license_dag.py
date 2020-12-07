# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from license import license_function
from license_deployment import license_deployment_function

# import lithops function
#from jti_lithops_function import jti_lithops_function 

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 12, 1),
}

dag = DAG("license_dag", default_args=default_args, schedule_interval=None)

license = PythonOperator(
    task_id='license',
    python_callable=asset_inventory_function,
    op_args=['license'],
    dag=dag)

license_deployment = PythonOperator(
    task_id='license_deployment',
    python_callable=asset_inventory_deployment_function,
    op_args=['license_deployment'],
    dag=dag)

license >> license_deployment