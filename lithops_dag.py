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
from airflow.operators.lithops_airflow_plugin import (
    LithopsCallAsyncOperator,
    LithopsMapOperator,
    LithopsMapReduceOperator
)
from func_map import add
from datetime import datetime, timedelta

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

my_task = LithopsCallAsyncOperator(
    task_id='add_task',
    func=add,
    data={'x' : 1, 'y' : 3},
    dag=dag,
    lithops_config=config,
)

basic_task = LithopsCallAsyncOperator(
    task_id='add_task_2',
    func=add,
    data={'x' : 4},
    data_from_task={'y' : 'add_task_1'},
    dag=dag,
    lithops_config=config,
)


my_task >> basic_task