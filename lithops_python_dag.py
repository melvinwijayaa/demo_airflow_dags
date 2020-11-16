from __future__ import print_function
from builtins import range
from airflow.operators.python_operator import PythonOperator
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

config = {'lithops' : {'storage_bucket' : 'lithops-bucket-habib01',
                        'storage':'ibm_cos',
                        'mode':'serverless'},
          'serverless':{'backend':'ibm_cf'},
          'ibm':{'iam_api_key':'cLQhHWR28nlJaGOqo7j87L5akzoCizqQPvH_XooHHo3h'},

          'ibm_cf':  {'endpoint': 'https://us-south.functions.cloud.ibm.com',
                      'namespace': 'Namespace-H5L',
                      'namespace_id': '7fd17f8c-4a89-4d08-9529-f9aa7737c52d'},

          'ibm_cos': {'endpoint': 'https://s3.jp-tok.cloud-object-storage.appdomain.cloud',
                      'private_endpoint': 'https://s3.private.jp-tok.cloud-object-storage.appdomain.cloud',
                      'api_key': 'jlFa8a1ERFLryXzLhVT4Z0HbYaUdwW_UsGCLDPlaCnm2'}}

dag = DAG(
    dag_id='lithops_python_operator', default_args=args,
    schedule_interval=None)

def hello_world(name):
    return 'Hello {}!'.format(name)

def lithops_func():
    fexec = lithops.FunctionExecutor(config=config)
    fexec.call_async(hello_world, 'World')
    print(fexec.get_result())

run_this = PythonOperator(
    task_id='print_the_context',
    python_callable=lithops_func,
    dag=dag)

run_that = PythonOperator(
    task_id='print_the_second_context',
    python_callable=lithops_func,
    dag=dag)

run_this >> run_that