# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from glo_city_prod import glo_city_prod_function


# import lithops function
#from jti_lithops_function import jti_lithops_function 

default_args = {
    "owner": "airflow",
    "start_date": datetime(2021, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("jglo_city_prod", default_args=default_args, schedule_interval=None)

#DummyOperator DAGS here
staging_start = DummyOperator(
    task_id='Staging_Start',
    dag=dag)

staging_done = DummyOperator(
    task_id='Staging_Done',
    dag=dag)

datalake_start = DummyOperator(
    task_id='Datalake_Start',
    dag=dag)

datalake_done = DummyOperator(
    task_id='Datalake_Done',
    dag=dag)

dimension_start = DummyOperator(
    task_id='Dimension_Start',
    dag=dag)

dimension_done = DummyOperator(
    task_id='Dimension_Done',
    dag=dag)

fact_start = DummyOperator(
    task_id='Fact_Start',
    dag=dag)

fact_done = DummyOperator(
    task_id='Fact_Done',
    dag=dag)

datamart_start = DummyOperator(
    task_id='DataMart_Start',
    dag=dag)

datamart_done = DummyOperator(
    task_id='DataMart_Done',
    dag=dag)

olap_start = DummyOperator(
    task_id='OLAP_Start',
    dag=dag)

olap_done = DummyOperator(
    task_id='OLAP_Done',
    dag=dag)

#Add database staging here ...
jtiiasset = DummyOperator(
    task_id='jtiiasset',
    dag=dag)

livejtiipdbms = DummyOperator(
    task_id='livejtiipdbms',
    dag=dag)

jtiifinace = DummyOperator(
    task_id='jtiifinace',
    dag=dag)

livejtiipayroll = DummyOperator(
    task_id='livejtiipayroll',
    dag=dag)

#Add more database staging here ...


#PythonOperator extract staging tables
glo_city_prod = PythonOperator(
    task_id='glo_city_prod',
    python_callable=glo_city_prod_function,
    op_args=['glo_city_prod'],
    dag=dag)

#DAG Sequences
staging_start >> glo_city_prod >> staging_done
