# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from glo_avrist import glo_avrist_function
from glo_bumida import glo_bumida_function
from glo_dailyperiod import glo_dailyperiod_function
from glo_deduction import glo_deduction_function
from glo_expensesrule import glo_expensesrule_function
from glo_jamsosmin import glo_jamsosmin_function
from glo_jamsosplus import glo_jamsosplus_function
from glo_medical import glo_medical_function
from glo_papproval import glo_papproval_function


# import lithops function
#from jti_lithops_function import jti_lithops_function 

default_args = {
    "owner": "airflow",
    "start_date": datetime(2021, 1, 19),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("livejtiipayroll1_dag", default_args=default_args, schedule_interval=None)

glo_avrist = PythonOperator(
    task_id='glo_avrist',
    python_callable=glo_avrist_function,
    op_args=['glo_avrist'],
    dag=dag)

glo_bumida = PythonOperator(
    task_id='glo_bumida',
    python_callable=glo_bumida_function,
    op_args=['glo_bumida'],
    dag=dag)

glo_dailyperiod = PythonOperator(
    task_id='glo_dailyperiod',
    python_callable=glo_dailyperiod_function,
    op_args=['glo_dailyperiod'],
    dag=dag)

glo_deduction = PythonOperator(
    task_id='glo_deduction',
    python_callable=glo_deduction_function,
    op_args=['glo_deduction'],
    dag=dag)

glo_expensesrule = PythonOperator(
    task_id='glo_expensesrule',
    python_callable=glo_expensesrule_function,
    op_args=['glo_expensesrule'],
    dag=dag)

glo_jamsosmin = PythonOperator(
    task_id='glo_jamsosmin',
    python_callable=glo_jamsosmin_function,
    op_args=['glo_jamsosmin'],
    dag=dag)

glo_jamsosplus = PythonOperator(
    task_id='glo_jamsosplus',
    python_callable=glo_jamsosplus_function,
    op_args=['glo_jamsosplus'],
    dag=dag)

glo_medical = PythonOperator(
    task_id='glo_medical',
    python_callable=glo_medical_function,
    op_args=['glo_medical'],
    dag=dag)

glo_papproval = PythonOperator(
    task_id='glo_papproval',
    python_callable=glo_papproval_function,
    op_args=['glo_papproval'],
    dag=dag)

#DAG Sequences
glo_avrist >> glo_bumida >> glo_dailyperiod >> glo_deduction >> glo_expensesrule >> glo_jamsosmin >> glo_jamsosplus >> glo_medical >> glo_papproval
