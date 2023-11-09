import sqlite3
import os
import pyodbc
from datetime import datetime
class CTDataBase():
    status = False
    details= {}
    def __init__(self,details):
        #self.conn = sqlite3.connect(FILEPATH+ "\\CTDATA.db")
        try:
            self.conn = pyodbc.connect(details["connection_string"])
            self.details = details
            self.c = self.conn.cursor()
            #print("Connection Established")
            self.status = True
        except:
            pass

    def insert_execution_record(self,session_details,report_options):
        session_details = {k: str(v) for k, v in session_details.items()}
        query="INSERT INTO app_execution(owner,test_execution_name,app_name,app_version,platform,add_info,report_options,start_time,end_time,duration,active,deactivate_reason) VALUES(N'"\
              + session_details["owner"]+"',N'" \
              + session_details["test_execution_name"] + "',N'" \
              + session_details["application_name"] + "',N'" \
              + session_details["application_version"] + "',N'" \
              + session_details["platform"] + "',N'" \
              + session_details["additional_information"] + "',N'" \
              +str(report_options).replace('\'','"')+"',?,?,?,1,''"+")"
        #print(query)
        self.c.execute(query, datetime.strptime(session_details["start_time"], '%d-%m-%y %H:%M:%S'),
                        datetime.strptime(session_details["end_time"], '%d-%m-%y %H:%M:%S'),
                        datetime.strptime(session_details["duration"], '%H:%M:%S'))
        self.conn.commit()

    def insert_test_record(self,name,id,desc,start_time,end_time,duration,result,priority,log):
        sel_query = "SELECT MAX(id)  FROM app_execution"
        self.c.execute(sel_query)
        data = self.c.fetchall()
        #print(data)
        query = 'INSERT INTO app_test(Execution_ID,name,test_id,description,start_time,end_time,duration,result,priority,logs) ' \
                'VALUES(\'' +str(data[0][0])+'\',N\'' + name.replace("'","\"") + '\',N\'' + id + '\',N\'' + desc.replace("'","\"") + '\',?,?,?,\'' + result + '\',N\''+priority+'\',N\''+log.replace("'","\"")+'\')'
        #print(query)
        self.c.execute(query, datetime.strptime(start_time, '%d-%m-%y %H:%M:%S'),
                             datetime.strptime(end_time, '%d-%m-%y %H:%M:%S'),
                             datetime.strptime(duration, '%H:%M:%S'))
        self.conn.commit()

