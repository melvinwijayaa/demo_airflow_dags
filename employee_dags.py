# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
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

dag = DAG("employee_dag", default_args=default_args, schedule_interval=timedelta(1))

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

personal >> superior
jobactual >> jobactualcomposite
