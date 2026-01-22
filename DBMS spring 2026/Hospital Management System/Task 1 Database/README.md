Task 1: Hospital Database Design (README Version)
Overview

This task involves designing a relational database for a hospital management system. The database is structured to manage patients, doctors, departments, appointments, prescriptions, and billing records. The design follows standard DBMS principles such as normalization, primary keys, foreign keys, and referential integrity.

The database acts as the foundational layer for analytical and AI-based tasks implemented later.

Database Tables and Structure
1. Department

Stores information about hospital departments.

Key Fields

DepartmentID – Primary Key

DepartmentName

Description

Represents different medical departments in the hospital.

One department can have multiple doctors.

2. Doctor

Stores information about doctors working in the hospital.

Key Fields

DoctorID – Primary Key

DepartmentID – Foreign Key (references Department)

Other Fields

Name

Specialization

PhoneNumber

Email

Description

Each doctor belongs to exactly one department.

A doctor can attend multiple appointments.

3. Patient

Stores demographic and contact details of patients.

Key Fields

PatientID – Primary Key

Other Fields

Name

DateOfBirth

Gender

Address

PhoneNumber

Email

Description

Each patient can have multiple appointments over time.

4. Appointment

Represents each visit of a patient to the hospital.
This is the central table in the database.

Key Fields

AppointmentID – Primary Key

PatientID – Foreign Key (references Patient)

DoctorID – Foreign Key (references Doctor)

Other Fields

AppointmentDate

Reason

Description

Connects patients with doctors.

Acts as the base for prescriptions and billing.

5. Prescription

Stores medication details prescribed during an appointment.

Key Fields

PrescriptionID – Primary Key

AppointmentID – Foreign Key (references Appointment)

Other Fields

Medication

Dosage

Duration

Description

Each appointment generates one prescription record.

6. Billing

Stores payment details related to an appointment.

Key Fields

BillingID – Primary Key

AppointmentID – Foreign Key (references Appointment)

Other Fields

Amount

PaymentDate

PaymentMethod

Description

Each appointment has one billing record associated with it.

Design Characteristics

All tables use primary keys for unique identification.

Foreign keys enforce referential integrity between tables.

The schema avoids data redundancy through normalization.

The design supports analytical queries and AI-driven analysis.

Appointment acts as the central linking entity across the system.

Outcome

The result is a clean, scalable hospital database design that supports both operational storage and higher-level analytics, including patient readmission analysis.
