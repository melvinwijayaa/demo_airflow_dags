# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from glo_city import glo_city_function
from glo_brand import glo_brand_function
from glo_location import glo_location_function
from asset_inventory import asset_inventory_function
from asset_inventory_deployment import asset_inventory_deployment_function
from license import license_function
from license_deployment import license_deployment_function
from control_input import control_input_function
from sec_logmdl import sec_logmdl_function
from sec_auditlog import sec_auditlog_function

# import lithops function
#from jti_lithops_function import jti_lithops_function 

default_args = {
    "owner": "airflow",
    "start_date": datetime(2021, 1, 1),
}

dag = DAG("jtiasset_test_dag", default_args=default_args, schedule_interval=None)

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
glo_city = PythonOperator(
    task_id='glo_city',
    python_callable=glo_city_function,
    op_args=['glo_city'],
    dag=dag)

glo_location = PythonOperator(
    task_id='glo_location',
    python_callable=glo_location_function,
    op_args=['glo_location'],
    dag=dag)


glo_brand = PythonOperator(
    task_id='glo_brand',
    python_callable=glo_brand_function,
    op_args=['glo_brand'],
    dag=dag)

control_input = PythonOperator(
    task_id='control_input',
    python_callable=control_input_function,
    op_args=['control_input'],
    dag=dag)

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
    op_args=['license'],
    dag=dag)

license_deployment = PythonOperator(
    task_id='license_deployment',
    python_callable=license_deployment_function,
    op_args=['license_deployment'],
    dag=dag)

sec_auditlog = PythonOperator(
    task_id='sec_auditlog',
    python_callable=sec_auditlog_function,
    op_args=['sec_auditlog'],
    dag=dag)

sec_logmdl = PythonOperator(
    task_id='sec_logmdl',
    python_callable=sec_logmdl_function,
    op_args=['sec_logmdl'],
    dag=dag)


#DAG Sequences
staging_start >> control_input >> [glo_city, glo_brand, glo_location] >> asset_inventory >> sec_auditlog >> sec_logmdl >> license_deployment >> license >> asset_inventory_deployment >> staging_done
