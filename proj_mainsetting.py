import pyodbc
import psycopg2
import lithops

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
    'iam_api_key': 'HXllbHC68TncpWEzjurOOKEidQf9bTk5K7kMsNDjfyFN'
    },
'ibm_cf':{
    'endpoint'     : 'https://jp-tok.functions.cloud.ibm.com',
    'namespace'    : 'JTI_Dev',
    'namespace_id' : 'eab04365-3267-4b09-b33c-bf83e04ecacc'
    },
'ibm_cos':{
    'endpoint'    : 'https://s3.au-syd.cloud-object-storage.appdomain.cloud',
    'private_endpoint': 'https://s3.private.au-syd.cloud-object-storage.appdomain.cloud',
    'api_key '    : 'oPCxFqLR0OX593ImB5pebiHDaqQUhkuCkbcNlIJp__1u'
    #'access_key' : <ACCESS_KEY>  # Optional
    #'secret_key' : <SECRET_KEY>  # Optional
    },
}
def proj_mainsetting_function(tablename):
    fexec = lithops.FunctionExecutor()
    fexec.call_async(proj_mainsetting,tablename)
    print(fexec.get_result())    
    
def proj_mainsetting(tablename):

    #Fixed conexion string for connecting sqlserver -- no need to change 
    conn1 = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=cap-au-sg-prd-04.securegateway.appdomain.cloud,15275;'
        'DATABASE=jtiiproms;'
        'UID=sa;'
        'PWD=Pas5word')

    #Fixed conexion string for connecting postgresql -- no need to change     
    conn2 = psycopg2.connect(
        database = 'ibmclouddb' ,
        user = 'ibm_cloud_f261f536_a6f2_4fec_b8e9_55016c16b459' ,
        password = 'a4285df0d0f18926f9c84591c78f91d402ab3d037e8ef6023f0fb4ff41e45043',
        host = 'c0ca2771-62ed-4c2a-862e-743fda10b364.bqfh4fpt0vhjh7rs4ot0.databases.appdomain.cloud',
        port = '32645')
        
    #Retrieve data -- change here
    cur1 = conn1.cursor()
    cur1.execute("SELECT id, stat, createdby, createddate, createdip, updatedby, updateddate, updatedip, \
                idproject, noregpm, noregadm1, noregadm2, headcount, ibmprojectmanager FROM "+ tablename)
    records = cur1.fetchall()
    #conn1.commit() -- no need to commit

    #Delete data --change here
    cur2 = conn2.cursor()
    cur2.execute("DELETE FROM jtiiproms." +tablename)
    conn2.commit()

    print(cur2.rowcount, "Records deleted successfully from " +tablename)

    #Insert data -- change here
    cur2 = conn2.cursor()
    cur2.executemany("INSERT INTO jtiiproms." +tablename+ "(id, stat, createdby, createddate, \
                createdip, updatedby, updateddate, updatedip, idproject, noregpm, noregadm1, \
                noregadm2, headcount, ibmprojectmanager) \
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",records)
    conn2.commit()

    print(cur2.rowcount, "Record inserted successfully into " +tablename)
    
if __name__ == '__main__':
    fexec = lithops.FunctionExecutor()
    fexec.call_async(proj_mainsetting,'proj_mainsetting')
    print(fexec.get_result())
