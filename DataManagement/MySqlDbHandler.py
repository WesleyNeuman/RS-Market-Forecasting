import mysql.connector
import logging

class MySqlDbHandler(object):
    """Handles logging data, retrieving data, and performing ETL math on the retrieved data"""

    def log_mysql():
        mydb = mysql.connector.connect(
          host="localhost",
          user="yourusername",
          password="yourpassword",
          database="mydatabase"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        mycursor.execute(sql, val)

        mydb.commit()


    def get_mysql():
        mydb = mysql.connector.connect(
          host="localhost",
          user="yourusername",
          password="yourpassword",
          database="mydatabase"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM customers")

        myresult = mycursor.fetchall()
