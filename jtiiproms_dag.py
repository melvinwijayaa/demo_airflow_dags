# airflow related
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

# other packages
from datetime import datetime, timedelta

# import operators from the 'operators' file
from contract_termination_request import contract_termination_request_function
from glo_approvalrecord import glo_approvalrecord_function
from glo_customer import glo_customer_function
from glo_location_proms import glo_location_proms_function
from num_department import num_department_function
from proj_contractreg import proj_contractreg_function
from proj_mainsetting import proj_mainsetting_function
from proj_sowcategory import proj_sowcategory_function
from proj_sowlayout import proj_sowlayout_function
from proj_warmbodyreg import proj_warmbodyreg_function
from proj_departmentlist import proj_departmentlist_function


# import lithops function
#from jti_lithops_function import jti_lithops_function 

default_args = {
    "owner": "airflow",
    "start_date": datetime(2021, 1, 19),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("jtiiproms_dag", default_args=default_args, schedule_interval=None)

contract_termination_request = PythonOperator(
    task_id='contract_termination_request',
    python_callable=contract_termination_request_function,
    op_args=['contract_termination_request'],
    dag=dag)

glo_approvalrecord = PythonOperator(
    task_id='glo_approvalrecord',
    python_callable=glo_approvalrecord_function,
    op_args=['glo_approvalrecord'],
    dag=dag)

glo_customer = PythonOperator(
    task_id='glo_customer',
    python_callable=glo_customer_function,
    op_args=['glo_customer'],
    dag=dag)

glo_location_proms = PythonOperator(
    task_id='glo_location_proms',
    python_callable=glo_location_proms_function,
    op_args=['glo_location_proms'],
    dag=dag)

num_department = PythonOperator(
    task_id='num_department',
    python_callable=num_department_function,
    op_args=['num_department'],
    dag=dag)

proj_contractreg = PythonOperator(
    task_id='proj_contractreg',
    python_callable=proj_contractreg_function,
    op_args=['proj_contractreg'],
    dag=dag)

proj_mainsetting = PythonOperator(
    task_id='proj_mainsetting',
    python_callable=proj_mainsetting_function,
    op_args=['proj_mainsetting'],
    dag=dag)

proj_sowcategory = PythonOperator(
    task_id='proj_sowcategory',
    python_callable=proj_sowcategory_function,
    op_args=['proj_sowcategory'],
    dag=dag)

proj_sowlayout = PythonOperator(
    task_id='proj_sowlayout',
    python_callable=proj_sowlayout_function,
    op_args=['proj_sowlayout'],
    dag=dag)

proj_warmbodyreg = PythonOperator(
    task_id='proj_warmbodyreg',
    python_callable=proj_warmbodyreg_function,
    op_args=['proj_warmbodyreg'],
    dag=dag)

proj_departmentlist = PythonOperator(
    task_id='proj_departmentlist',
    python_callable=proj_departmentlist_function,
    op_args=['departmentlist'],
    dag=dag)
#DAG Sequences
contract_termination_request >> glo_approvalrecord >> glo_customer >> glo_location_proms >> num_department >> proj_contractreg >> proj_mainsetting >> proj_sowcategory >> proj_sowlayout >> proj_warmbodyreg >> proj_departmentlist
