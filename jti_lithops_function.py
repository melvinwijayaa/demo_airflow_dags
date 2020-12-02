import  lithops

config = {
'lithops': {
    'storage': 'ibm_cos',
    'storage_bucket': 'bucket-jti',
    'mode': 'serverless'
    },
'serverless':{
    'backend': 'ibm_cf',
    'runtime': 'khairulhabib/lithops-runtime-datalake:1.0.1'
    },
'ibm':{
    'iam_api_key': 'L8cWWexAcTm8K-XtlthzkwtNxZjxQwtnCcwr4Gj0qhkg'
    },
'ibm_cf':{
    'endpoint'     : 'https://jp-tok.functions.cloud.ibm.com',
    'namespace'    : 'JTI Dev',
    'namespace_id' : 'f02917fc-e645-4850-9dea-5f27b541b933'
    },
'ibm_cos':{
    'endpoint'    : 'https://s3.au-syd.cloud-object-storage.appdomain.cloud',
    'private_endpoint': 'https://s3.private.au-syd.cloud-object-storage.appdomain.cloud',
    'api_key '    : 'p6D4IagLwAXetJCWAzlsyzPnWezeIPicE-2j2LggG7HO'
    #'access_key' : <ACCESS_KEY>  # Optional
    #'secret_key' : <SECRET_KEY>  # Optional
    },
}

def start_task(tablename):
    #return 'Start DAG {}!'.format(name)
    print("Start DAG" +tablename)

def jti_lithops_function(tablename):
    fexec = lithops.FunctionExecutor(config=config)
    fexec.call_async(start_task,tablename)
    print(fexec.get_result())
