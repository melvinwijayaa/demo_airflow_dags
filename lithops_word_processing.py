from __future__ import print_function
from builtins import range
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG
from datetime import datetime, timedelta

import time
from pprint import pprint

from lithops_function import my_map_function
from lithops_function import my_reduce_function
from lithops_function import lithops_func



seven_days_ago = datetime.combine(
        datetime.today() - timedelta(7), datetime.min.time())

args = {
    'owner': 'airflow',
    'start_date': seven_days_ago,
}


dag = DAG(
    dag_id='lithops_word_processing', default_args=args,
    schedule_interval=None)



run_this = PythonOperator(
    task_id='word_processing',
    python_callable=lithops_func,
    op_args=['World'],
    dag=dag)

run_this