from __future__ import print_function
from builtins import range
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG
from datetime import datetime, timedelta
import lithops

import time
from pprint import pprint

# Dataset from: https://archive.ics.uci.edu/ml/datasets/bag+of+words
iterdata = ['https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.enron.txt',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.kos.txt',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.nips.txt',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.nytimes.txt',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.pubmed.txt']

seven_days_ago = datetime.combine(
        datetime.today() - timedelta(7), datetime.min.time())

args = {
    'owner': 'airflow',
    'start_date': seven_days_ago,
}

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

dag = DAG(
    dag_id='lithops_word_processing', default_args=args,
    schedule_interval=None)

def my_map_function(url):
    print('I am processing the object from {}'.format(url.path))
    counter = {}

    data = url.data_stream.read()

    for line in data.splitlines():
        for word in line.decode('utf-8').split():
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1

    return counter


def my_reduce_function(results):
    final_result = {}
    for count in results:
        for word in count:
            if word not in final_result:
                final_result[word] = count[word]
            else:
                final_result[word] += count[word]

    return final_result

def lithops_func(*op_args):
    fexec = lithops.FunctionExecutor()
    fexec.map_reduce(my_map_function, iterdata, my_reduce_function)

run_this = PythonOperator(
    task_id='word_processing',
    python_callable=lithops_func,
    op_args=['World'],
    dag=dag)

run_this