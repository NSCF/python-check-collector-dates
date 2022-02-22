import mysql.connector as mysql
from mysql.connector import Error
from loginCredentials import *


def extractDatesFromDB():
    # Database query to extract collecting dates per collection object
    SQL = """SELECT co.CatalogNumber, year(ce.StartDate) FROM collectionobject co
            JOIN collection c ON co.collectionID = c.collectionID
            JOIN collectingevent ce ON co.collectingeventID = ce.collectingeventID
            WHERE c.CollectionName = 'Vertebrate Palaeontology Cenozoic';"""
    
    # connect to database
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        if db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute("select database();")
            dataBase = cursor.fetchone()
            print("You're connected to database: ", dataBase)
            print("Connected to:", db_connection.get_server_info())
            # Query database
            cursor.execute(SQL)
            print("Query has been executed")

    except Error as err:
        print("Error while connecting to MySQL: ", err)

    results = cursor.fetchall()
    
    db_connection.close()
    print("Database disconnected")
    return results
    

extractDatesFromDB()
