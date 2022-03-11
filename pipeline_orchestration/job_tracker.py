import datetime
import psycopg2
from configparser import ConfigParser

dbconfig = ConfigParser()
dbconfig.read('config.ini')


# Your job status table should contain these fields:
# - Job_id (primary and unique): naming convention can be jobname_yyyy-mm-dd
# - Status: success or failure state of the job
# - Updated_time: datetime of the entry

class Tracker(object):
    """
    job_id, status, updated_time
    """
    def __init__(self, jobname, dbconfig):
        self.jobname = jobname
        self.dbconfig = dbconfig
    
    def assign_job_id(self):
        today = str(datetime.date.today())
        job_id  = self.jobname + '_' + today
        return job_id

    def create_job_table(self,table_name):

        # table_name = 'spark_jobs_springcapital'
        connection = self.get_db_connection()
        curr = connection.cursor()

        try:
            #insert values
            sql = f""" 
            create table {table_name} as (job_id varchar(30) primary key,
            status varchar(30),update_time date)
            """
            curr.execute(sql)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("error executing db statement for job tracker.")
        return


    def update_job_status(self, status):
        job_id = self.assign_job_id()
        print("Job ID Assigned: {}".format(job_id))
        update_time = datetime.datetime.now()
        # table_name = self.dbconfig.get("postgres", "job_tracker_table_name")
        table_name = 'spark_jobs_springcapital'
        connection = self.get_db_connection()
        try:

            #insert values
            sql = f""" insert into {table_name} (job_id,status,update_time)
            values(%s,%s,%s)
            """
            recs = (job_id,status,update_time)
            curr = connection.cursor()
            curr.execute(sql,recs)
            connection.commit()
            # [Execute the SQL statement to insert to job status table]
        except (Exception, psycopg2.Error) as error:
            print("error executing db statement for job tracker.")
        finally:
            connection.cursor().close()
        return

    def get_job_status(self, job_id):
        # connect db and send sql query
        table_name = self.dbconfig.get('postgres', 'job_tracker_table_name')
        connection = self.get_db_connection()
        try:
            curr = connection.cursor()
            curr.execute(f"select status from {table_name} where job_id={job_id}")
            record = curr.fetchall()
            return record
        except (Exception, psycopg2.Error) as error:
            print("error executing db statement for job tracker.")
        return

    def get_db_connection(self):
        host = 'host'
        port = 'port'
        user = 'user'
        password = 'password'
        database = 'database'

        connection = None
        try:
            connection = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        return connection

