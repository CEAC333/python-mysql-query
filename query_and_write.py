import os
import MySQLdb # This is the forked 'mysqlclient' for Python 3.4
from config import DB_HOST, DB_USER, DB_PASS, DATABASE_NAME, sql


db = MySQLdb.connect(DB_HOST,
                     DB_USER,
                     DB_PASS,
                     DATABASE_NAME)

cursor = db.cursor()
query = cursor.execute(sql)
results = cursor.fetchall()

f = open('emails-all-active.csv', 'w')
for r in results:
    f.writelines('{}\n'.format(r[0]))
f.close()
