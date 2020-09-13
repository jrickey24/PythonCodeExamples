import pyodbc
import pandas
from _ast import In

db_connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=JR_DB_v1;'
                      'Trusted_Connection=yes;')

cursor = db_connection.cursor()
sql_query = pandas.read_sql_query("""
SELECT * FROM wgu_packages_v1 where DeliverBy <> 'EOD'
""", db_connection)


In[sql_query]: sql_query.to_csv('foo.csv')

