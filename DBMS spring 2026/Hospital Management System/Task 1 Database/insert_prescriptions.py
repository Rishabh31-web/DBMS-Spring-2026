import mysql.connector
import random

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rishabh31",
    database="hospital_management_system"
)

cursor = conn.cursor()

# Fetch all appointment IDs
cursor.execute("SELECT AppointmentID FROM Appointment")
appointments = [row[0] for row in cursor.fetchall()]

medications = [
    "Paracetamol",
    "Amoxicillin",
    "Ibuprofen",
    "Azithromycin",
    "Cetirizine",
    "Metformin",
    "Pantoprazole",
    "Vitamin D3",
    "Calcium Tablets",
    "Cough Syrup"
]

dosages = [
    "Once a day",
    "Twice a day",
    "Thrice a day",
    "After meals",
    "Before meals"
]

durations = [
    "3 days",
    "5 days",
    "7 days",
    "10 days",
    "14 days"
]

prescriptions = []

for appointment_id in appointments:
    medicine = random.choice(medications)
    dosage = random.choice(dosages)
    duration = random.choice(durations)

    prescriptions.append(
        (medicine, dosage, duration, appointment_id)
    )

sql = """
INSERT INTO Prescription (Medication, Dosage, Duration, AppointmentID)
VALUES (%s, %s, %s, %s)
"""

cursor.executemany(sql, prescriptions)
conn.commit()

print("✅ Prescriptions inserted successfully")

cursor.close()
conn.close()
