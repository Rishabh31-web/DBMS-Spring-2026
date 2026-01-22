import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rishabh31",
    database="hospital_management_system"
)

cursor = conn.cursor()

departments = [
    ("General Medicine", "Block A"),
    ("Pediatrics", "Block B"),
    ("Gynecology", "Block C"),
    ("Orthopedics", "Block D"),
    ("Cardiology", "Block E"),
    ("Dermatology", "Block F")
]

sql = "INSERT INTO Department (DepartmentName, Location) VALUES (%s, %s)"

cursor.executemany(sql, departments)
conn.commit()

print("✅ Departments inserted successfully")

cursor.close()
conn.close()



