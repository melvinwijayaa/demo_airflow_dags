#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import json
from datetime import timedelta

from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.sensors import HttpSensor
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('function_dag', default_args=default_args, tags=['example'], start_date=datetime(2020, 9, 16))

dag.doc_md = __doc__

# task_post_op, task_get_op and task_put_op are examples of tasks created by instantiating operators
# [START howto_operator_http_task_post_op]
task_post_op = SimpleHttpOperator(
    task_id='post_op',
    method='POST',
    endpoint='',
    http_conn_id='http_ibm_function',
    data=json.dumps({"name": "habib"}),
    headers={"Content-Type": "application/json"},
    # response_check=lambda response: response.json()['result']['body'] == "Hello habib!",
    response_check=lambda response: "habib" in response.text,
    log_response='true',
    dag=dag,
)
# [END howto_operator_http_task_post_op]

# [START howto_operator_http_task_post_op]
task_post_op2 = SimpleHttpOperator(
    task_id='post_op2',
    method='POST',
    endpoint='',
    http_conn_id='http_ibm_function',
    data=json.dumps({"name": "khairul"}),
    headers={"Content-Type": "application/json"},
    # response_check=lambda response: response.json()['result']['body'] == "Hello khairul!",
    response_check=lambda response: "khairul" in response.text,
    log_response='true',
    dag=dag,
)
# [END howto_operator_http_task_post_op]


task_post_op >> task_post_op2