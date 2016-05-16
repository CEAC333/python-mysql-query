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

print('Starting...')
f = open('outfile.txt', 'w')
for r in results:
    current_datum = r[0]
    f.writelines('{}\n'.format(current_datum))
    print('Wrote: {}'.format(current_datum))
f.close()
print('Done.')
