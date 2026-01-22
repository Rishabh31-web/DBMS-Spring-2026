SWARM-BASED AGENTIC AI – FLOWCHART STYLE (TASK 2)

SYSTEM OVERVIEW
---------------
User Query
   ↓
"Calculate patient readmission rates and department-wise contribution"
   ↓
Swarm-Based Agentic AI System
   ↓
Final Insights (Patients + Departments)


SWARM ARCHITECTURE OVERVIEW
---------------------------
Orchestrator Agent
        ↓
-------------------------------------------------
|        |            |             |            |
Data Agent   Readmission Agent   Department Agent   Insight Agent
-------------------------------------------------


AGENT FLOW (STEP-BY-STEP)
-------------------------

START
  ↓
User submits analytical query
  ↓
Orchestrator Agent activated
  ↓
Orchestrator triggers Data Retrieval Agent
  ↓
Data Retrieval Agent
  ├─ Connects to Hospital Database
  ├─ Fetches Patient, Appointment, Doctor, Department data
  └─ Returns structured records
        ↓
Orchestrator passes data to analysis agents
        ↓


AGENT ROLES AND RESPONSIBILITIES
--------------------------------

Orchestrator Agent {
  Role:
  - Controls execution order of agents
  - Manages data flow between agents
  - Ensures complete task execution

  Input:
  - User query

  Output:
  - Final coordinated results
}

Data Retrieval Agent {
  Role:
  - Connects to MySQL database
  - Executes JOIN queries across tables
  - Converts relational data into usable records

  Tables Used:
  - Patient
  - Appointment
  - Doctor
  - Department

  Output:
  - PatientID, AppointmentID, DepartmentName
}

Readmission Analysis Agent {
  Role:
  - Counts number of visits per patient
  - Identifies repeat visits
  - Calculates readmission count

  Logic:
  - Readmissions = Total Visits − 1

  Output:
  - PatientID → Readmission Count
}

Department Attribution Agent {
  Role:
  - Maps appointments to departments
  - Aggregates visit and readmission counts
  - Identifies high-load departments

  Output:
  - DepartmentName → Total Visits / Readmissions
}

Insight Generation Agent {
  Role:
  - Interprets numerical outputs
  - Ranks high-risk patients
  - Identifies departments with maximum readmissions
  - Produces human-readable insights

  Output:
  - Top readmitted patients
  - Department with highest readmission load
}


DATA FLOW BETWEEN AGENTS
------------------------
Database
   ↓
Data Retrieval Agent
   ↓
Structured Visit Records
   ↓
---------------------------------
|                               |
Readmission Analysis Agent   Department Attribution Agent
|                               |
---------------------------------
           ↓
      Insight Agent
           ↓
      Final Output


FINAL OUTPUT
------------
- List of patients with highest readmission counts
- Department contributing most to readmissions
- Actionable insights for hospital management


WHY THIS IS AGENTIC & SWARM-BASED
--------------------------------
- Each agent is autonomous and task-specific
- Agents collaborate via shared data
- No single monolithic algorithm
- Orchestrator coordinates swarm behavior
- System can be extended with new agents easily


DESIGN CHARACTERISTICS
----------------------
- Modular agent design
- Scalable and extensible
- Clear separation of responsibilities
- Database-driven intelligence
- Supports real-time analytical queries
