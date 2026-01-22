HOSPITAL DATABASE DESIGN – FLOWCHART STYLE (TASK 1)

DATABASE OVERVIEW
-----------------
Department ──▶ Doctor ──▶ Appointment ◀── Patient
                               │
                               ├──▶ Prescription
                               └──▶ Billing

Appointment is the CENTRAL TABLE connecting all entities.


TABLE STRUCTURE WITH PK / FK
----------------------------

Department {
  DepartmentID : INT (PRIMARY KEY)
  DepartmentName : VARCHAR

  Role:
  - Represents hospital departments
  - One Department → Many Doctors
}

Doctor {
  DoctorID : INT (PRIMARY KEY)
  Name : VARCHAR
  Specialization : VARCHAR
  PhoneNumber : VARCHAR
  Email : VARCHAR
  DepartmentID : INT (FOREIGN KEY → Department.DepartmentID)

  Role:
  - Represents doctors
  - Each Doctor belongs to ONE Department
  - One Doctor → Many Appointments
}

Patient {
  PatientID : INT (PRIMARY KEY)
  Name : VARCHAR
  DateOfBirth : DATE
  Gender : VARCHAR
  Address : VARCHAR
  PhoneNumber : VARCHAR
  Email : VARCHAR

  Role:
  - Represents patients
  - One Patient → Many Appointments
}

Appointment {
  AppointmentID : INT (PRIMARY KEY)
  AppointmentDate : DATETIME
  Reason : VARCHAR
  PatientID : INT (FOREIGN KEY → Patient.PatientID)
  DoctorID : INT (FOREIGN KEY → Doctor.DoctorID)

  Role:
  - Represents each hospital visit
  - Connects Patient ↔ Doctor
  - CENTRAL ENTITY of the database
}

Prescription {
  PrescriptionID : INT (PRIMARY KEY)
  Medication : VARCHAR
  Dosage : VARCHAR
  Duration : VARCHAR
  AppointmentID : INT (FOREIGN KEY → Appointment.AppointmentID)

  Role:
  - Stores medicines prescribed during an appointment
  - One Appointment → One Prescription
}

Billing {
  BillingID : INT (PRIMARY KEY)
  Amount : DECIMAL
  PaymentDate : DATE
  PaymentMethod : VARCHAR
  AppointmentID : INT (FOREIGN KEY → Appointment.AppointmentID)

  Role:
  - Stores payment details for an appointment
  - One Appointment → One Billing record
}


RELATIONSHIP FLOW SUMMARY
-------------------------
Department (PK)
   ↓
Doctor (PK, FK → Department)
   ↓
Appointment (PK, FK → Doctor, FK → Patient)
   ↑
Patient (PK)

Appointment
   ├──▶ Prescription (PK, FK → Appointment)
   └──▶ Billing (PK, FK → Appointment)


DESIGN CHARACTERISTICS
----------------------
- Primary Keys uniquely identify records
- Foreign Keys enforce referential integrity
- No redundant data
- Appointment acts as the core linkage table
- Supports analytics such as patient readmission analysis
- Suitable foundation for swarm-based agentic AI
