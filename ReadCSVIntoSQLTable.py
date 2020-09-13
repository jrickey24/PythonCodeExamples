import pyodbc
import pandas

data = pandas.read_csv(r'WGUPSPackageFile.csv')
df = pandas.DataFrame(data, columns=['PackageID', 'AddressStreet', 'AddressCity', 'AddressState',
                                     'AddressZip', 'DeliverBy', 'PackageWeight', 'PackageNotes'])


db_connection = pyodbc.connect('Driver={SQL Server};'
                               'Server=server_name;'
                               'Database=JR_DB_v1;'
                               'Trusted_Connection=yes;')
cursor = db_connection.cursor()


for row in df.itertuples():

    cursor.execute('''
                   INSERT INTO JR_DB_v1.dbo.wgu_packages_v1 (PackageID, AddressStreet, AddressCity, AddressState,
                   AddressZip, DeliverBy, PackageWeight, PackageNotes)
                   VALUES (?,?,?,?,?,?,?,?)
                   ''',
                   row.PackageID,
                   row.AddressStreet,
                   row.AddressCity,
                   row.AddressState,
                   row.AddressZip,
                   row.DeliverBy,
                   row.PackageWeight,
                   row.PackageNotes
                   )
db_connection.commit()
