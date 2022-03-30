# import mysql.connector as mysql  # import from MySQL lib

# mysql.connect(host='localhost',  # connector
#               database='test_db',
#               user='Denis',
#               password='2016')
#
# cur = conn.cursor

import psycopg2  # import from PosgreSQL

conn = psycopg2.connect(host='localhost',  # connector
                        database='test_db',
                        user='Denis',
                        password='2016')

cur = conn.cursor

# cur.execute("..")