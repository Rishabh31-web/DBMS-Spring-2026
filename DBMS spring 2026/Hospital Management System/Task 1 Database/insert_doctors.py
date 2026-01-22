import mysql.connector
from faker import Faker
import random

fake = Faker('en_IN')

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rishabh31",
    database="hospital_management_system"
)

cursor = conn.cursor()

specializations = {
    1: "General Physician",
    2: "Pediatrician",
    3: "Gynecologist",
    4: "Orthopedic Surgeon",
    5: "Cardiologist",
    6: "Dermatologist"
}

doctors = []

for dept_id, spec in specializations.items():
    for _ in range(2):  # 2 doctors per department → 12 doctors
        name = fake.name()
        phone = str(random.randint(6000000000, 9999999999))
        email = fake.email()

        doctors.append((name, spec, phone, email, dept_id))

sql = """
INSERT INTO Doctor (Name, Specialization, PhoneNumber, Email, DepartmentID)
VALUES (%s, %s, %s, %s, %s)
"""

cursor.executemany(sql, doctors)
conn.commit()

print("✅ Doctors inserted successfully")

cursor.close()
conn.close()
