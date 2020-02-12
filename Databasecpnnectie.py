from sshtunnel import SSHTunnelForwarder
import mysql.connector
from mysql.connector import Error

with SSHTunnelForwarder(
    ('remote.ghaut.nl', 22),
    ssh_password="",
    ssh_username="",
    remote_bind_address=('0.0.0.0', 3306)) as server:

    connection = mysql.connector.connect(host='remote.ghaut.nl',
                                         port=3306,
                                         user='',
                                         passwd='',
                                         db='prutrecht')

    cur = connection.cursor()
    cur.execute("SELECT * FROM parkeerplekken")

    myresult = cur.fetchall()

    for x in myresult:
        print(x)

    cur.close()
    connection.close()
