from __future__ import print_function
from builtins import range
from airflow.operators import PythonOperator
from airflow.models import DAG
from datetime import datetime, timedelta
import lithops

import time
from pprint import pprint

seven_days_ago = datetime.combine(
        datetime.today() - timedelta(7), datetime.min.time())

args = {
    'owner': 'airflow',
    'start_date': seven_days_ago,
}

dag = DAG(
    dag_id='lithops_python_operator', default_args=args,
    schedule_interval=None)

def hello_world(name):
    return 'Hello {}!'.format(name)

def lithops_func(*op_args):
    fexec = lithops.FunctionExecutor()
    fexec.call_async(hello_world, op_args[0])
    print(fexec.get_result())

run_this = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=lithops_func,
    op_args=['World', 'Earth', 'Forest'],
    dag=dag)

run_that = PythonOperator(
    task_id='print_the_second_context',
    provide_context=True,
    python_callable=lithops_func,
    op_args=['Earth', 'World', 'Forest'],
    dag=dag)

run_this >> run_that