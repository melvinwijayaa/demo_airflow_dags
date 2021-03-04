# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from glo_payrolllock2 import glo_payrolllock2_function
from glo_pperiod import glo_pperiod_function
from glo_reward import glo_reward_function
from global_ptkp import global_ptkp_function
from global_taxpersen import global_taxpersen_function
from kurangpajak import kurangpajak_function
from kurs import kurs_function
from personalloan import personalloan_function
from personalmedical import personalmedical_function


# import lithops function
#from jti_lithops_function import jti_lithops_function 

default_args = {
    "owner": "airflow",
    "start_date": datetime(2021, 1, 19),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("livejtiipayroll2_dag", default_args=default_args, schedule_interval=None)

glo_payrolllock2 = PythonOperator(
    task_id='glo_payrolllock2',
    python_callable=glo_payrolllock2_function,
    op_args=['glo_payrolllock2'],
    dag=dag)

glo_pperiod = PythonOperator(
    task_id='glo_pperiod',
    python_callable=glo_pperiod_function,
    op_args=['glo_pperiod'],
    dag=dag)

glo_reward = PythonOperator(
    task_id='glo_reward',
    python_callable=glo_reward_function,
    op_args=['glo_reward'],
    dag=dag)

global_ptkp = PythonOperator(
    task_id='global_ptkp',
    python_callable=global_ptkp_function,
    op_args=['global_ptkp'],
    dag=dag)

global_taxpersen = PythonOperator(
    task_id='global_taxpersen',
    python_callable=global_taxpersen_function,
    op_args=['global_taxpersen'],
    dag=dag)

kurangpajak = PythonOperator(
    task_id='kurangpajak',
    python_callable=kurangpajak_function,
    op_args=['kurangpajak'],
    dag=dag)

kurs = PythonOperator(
    task_id='kurs',
    python_callable=kurs_function,
    op_args=['kurs'],
    dag=dag)

personalloan = PythonOperator(
    task_id='personalloan',
    python_callable=personalloan_function,
    op_args=['personalloan'],
    dag=dag)

personalmedical = PythonOperator(
    task_id='personalmedical',
    python_callable=personalmedical_function,
    op_args=['personalmedical'],
    dag=dag)

#DAG Sequences
glo_payrolllock2 >> glo_pperiod >> glo_reward >> global_ptkp >> global_taxpersen >> kurangpajak >> kurs >> personalloan >> personalmedical
