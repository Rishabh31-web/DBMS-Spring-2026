import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="rishabh31",
        database="hospital_management_system"
    )
