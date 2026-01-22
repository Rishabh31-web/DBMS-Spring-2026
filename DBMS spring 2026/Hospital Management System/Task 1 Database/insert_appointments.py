import mysql.connector
import random
from datetime import datetime, timedelta

# MySQL connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rishabh31",
    database="hospital_management_system"
)

cursor = conn.cursor()

# Fetch Patient IDs
cursor.execute("SELECT PatientID FROM Patient")
patients = [row[0] for row in cursor.fetchall()]

# Fetch Doctor IDs
cursor.execute("SELECT DoctorID FROM Doctor")
doctors = [row[0] for row in cursor.fetchall()]

# Appointment reasons
reasons = [
    "Fever",
    "Routine Checkup",
    "Back Pain",
    "Pregnancy Consultation",
    "Chest Pain",
    "Skin Allergy",
    "Follow-up Visit",
    "Joint Pain",
    "Cough and Cold"
]

appointments = []

for _ in range(200):  # 200 appointments
    patient_id = random.choice(patients)
    doctor_id = random.choice(doctors)

    days_ago = random.randint(0, 60)
    appointment_date = datetime.now() - timedelta(days=days_ago)

    reason = random.choice(reasons)

    appointments.append(
        (appointment_date, reason, patient_id, doctor_id)
    )

# IMPORTANT: Backticks used for Appointment table
sql = """
INSERT INTO `Appointment` (AppointmentDate, Reason, PatientID, DoctorID)
VALUES (%s, %s, %s, %s)
"""

cursor.executemany(sql, appointments)
conn.commit()

print("✅ Appointments inserted successfully")

cursor.close()
conn.close()
