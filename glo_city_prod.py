
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
def glo_city_prod_function(tablename):
    fexec = lithops.FunctionExecutor()
    fexec.call_async(glo_city,tablename)
    print(fexec.get_result())    
    
def glo_city_prod(tablename):

    #Fixed conexion string for connecting sqlserver -- no need to change 
    conn1 = pyodbc.connect(
        'DRIVER={PostgreSQL Unicode};'
        'Server=c0ca2771-62ed-4c2a-862e-743fda10b364.bqfh4fpt0vhjh7rs4ot0.databases.appdomain.cloud;'
        'Port=32645;'
        'Database=ibmclouddb;'
        'User ID=ibm_cloud_f261f536_a6f2_4fec_b8e9_55016c16b459;'
        'Password=a4285df0d0f18926f9c84591c78f91d402ab3d037e8ef6023f0fb4ff41e45043;'
        'String Types=Unicode')

    #Fixed conexion string for connecting postgresql -- no need to change     
    conn2 = psycopg2.connect(
        database = 'ibmclouddb' ,
        user = 'ibm_cloud_09847fd3_051e_4a89_b3d4_5ad2834bd12a' ,
        password = 'b3031a57615d6aa121981db35ea33d0e07e21bfb34af76e255b1e5236ae14f13',
        host = '0541b373-b134-406f-9687-f94b85d5cb94.bqfh4fpt0vhjh7rs4ot0.databases.appdomain.cloud',
        port = '30280')
        
    #Retrieve data -- change here
    cur1 = conn1.cursor()
    cur1.execute("SELECT id, stat, createdby, createddate, createdip, updatedby, updateddate, updatedip, name FROM "+ tablename)
    records = cur1.fetchall()
    #conn1.commit() -- no need to commit

    #Delete data --change here
    cur2 = conn2.cursor()
    cur2.execute("DELETE FROM dimension." +tablename)
    conn2.commit()

    print(cur2.rowcount, "Records deleted successfully from " +tablename)

    #Insert data -- change here
    cur2 = conn2.cursor()
    cur2.executemany("INSERT INTO dimension." +tablename+ "(id, stat, createdby, createddate, createdip, updatedby, updateddate, updatedip, name) \
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",records)
    conn2.commit()

    print(cur2.rowcount, "Record inserted successfully into " +tablename)
    
if __name__ == '__main__':
    fexec = lithops.FunctionExecutor()
    fexec.call_async(glo_city_prod,'glo_city_prod')
    print(fexec.get_result())