import mysql.connector
import random
from datetime import date, timedelta

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

payment_methods = [
    "Cash",
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]

billings = []

for appointment_id in appointments:
    amount = random.randint(200, 2000)  # realistic OPD range
    payment_date = date.today() - timedelta(days=random.randint(0, 30))
    payment_method = random.choice(payment_methods)

    billings.append(
        (amount, payment_date, payment_method, appointment_id)
    )

sql = """
INSERT INTO Billing (Amount, PaymentDate, PaymentMethod, AppointmentID)
VALUES (%s, %s, %s, %s)
"""

cursor.executemany(sql, billings)
conn.commit()

print("✅ Billing records inserted successfully")

cursor.close()
conn.close()
