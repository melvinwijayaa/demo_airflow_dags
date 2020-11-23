from __future__ import print_function
from builtins import range
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG
from datetime import datetime, timedelta
from lithops_video_transcoding import run

import time
from pprint import pprint

from lithops_function import lithops_func

yesterday = datetime.combine(
        datetime.today() - timedelta(1), datetime.min.time())

args = {
    'owner': 'airflow',
    'start_date': yesterday,
}


dag = DAG(
    dag_id='video_dag', default_args=args,
    schedule_interval=None)



run_this = PythonOperator(
    task_id='video_dag',
    python_callable=run,
    op_args=['http://techslides.com/demos/sample-videos/small.mp4'],
    dag=dag)

run_this