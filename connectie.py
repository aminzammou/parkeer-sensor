from sshtunnel import SSHTunnelForwarder
import mysql.connector
from mysql.connector import Error

# function for updating data in the database
def update():
    import update as up1
    plekje = str(up1.plek)
    with SSHTunnelForwarder(
        ('remote.ghaut.nl', 22),
        ssh_password="W817tjes",
        ssh_username="niek",
        remote_bind_address=('0.0.0.0', 3306)) as server:
        
        # sql query 
        connection = mysql.connector.connect(host='remote.ghaut.nl',
                                             port=3306,
                                             user='niek',
                                             passwd='W817tjes',
                                             db='prutrecht')

        cur = connection.cursor()
        sql = "UPDATE parkeerplekken SET bezet = " + plekje + " WHERE parkeerplekID = 1 "

        cur.execute(sql)

        connection.commit()

        print(cur.rowcount, "record(s) affected")
    
        cur.close()
        connection.close()

