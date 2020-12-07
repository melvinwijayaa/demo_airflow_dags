
# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator


# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from asset_inventory import asset_inventory_function
from asset_inventory_deployment import asset_inventory_deployment_function
from license import license_function
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

dag = DAG("license_dag", default_args=default_args, schedule_interval=None)

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

license = PythonOperator(
    task_id='license',
    python_callable=license_function,
    op_args=['license_deployment'],
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

#DAG Sequences
staging_start >> asset_inventory >> asset_inventory_deployment >> [personal, superior] >> jobactual >> jobactualcomposite >> staging_done
license_deployment
