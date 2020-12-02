# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file

# import lithops function
from jti_lithops_function import jti_lithops_function

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 12, 1),
}

dag = DAG("test_dag", default_args=default_args, schedule_interval=None)

asset = PythonOperator(
    task_id='test_dag',
    python_callable=jti_lithops_function,
    op_args=['test_dag'],
    dag=dag)

asset 
