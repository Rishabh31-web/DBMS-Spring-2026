import mysql.connector
from faker import Faker
import random
from datetime import date

fake = Faker('en_IN')  # Indian locale

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rishabh31",
    database="hospital_management_system"
)

cursor = conn.cursor()

def random_dob(min_age=1, max_age=80):
    today = date.today()
    age = random.randint(min_age, max_age)
    year = today.year - age
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return date(year, month, day)

patients = []

for _ in range(100):
    name = fake.name()
    dob = random_dob()
    gender = random.choice(["Male", "Female"])
    address = fake.address().replace("\n", ", ")
    phone = str(random.randint(6000000000, 9999999999))  # Indian mobile
    email = fake.email()

    patients.append((name, dob, gender, address, phone, email))

sql = """
INSERT INTO Patient (Name, DateOfBirth, Gender, Address, PhoneNumber, Email)
VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(sql, patients)
conn.commit()

print("✅ 100 Indian patients inserted successfully")

cursor.close()
conn.close()
