import MySQLdb
import csv

dbUser = 'root'
dbServer = 'localhost'
dbPass = ''
dbSchema = 'cadastro'


db = MySQLdb.connect(host=dbServer, user=dbUser, passwd=dbPass, db=dbSchema)
cursor = db.cursor()
dbQuery = 'SELECT * FROM cadastro.occupation;'
cursor.execute(dbQuery)
with open('occupation.csv', 'w') as f:
    writer = csv.writer(f)
    for row in cursor.fetchall():
        writer.writerow(row)
