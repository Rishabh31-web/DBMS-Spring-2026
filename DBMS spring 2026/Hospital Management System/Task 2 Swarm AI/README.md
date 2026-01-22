START
  ↓
User Query:
"Calculate patient readmission rates"
  ↓
Orchestrator Agent
  ↓
Data Retrieval Agent
  ├─ Fetch Patient + Appointment data
  └─ Return structured timelines
  ↓
Readmission Analysis Agent
  ├─ Count admissions per patient
  ├─ Detect readmissions
  └─ Compute readmission rates
  ↓
Department Attribution Agent
  ├─ Map appointments → doctors
  └─ Map doctors → departments
  ↓
Department Aggregation Agent
  ├─ Count readmissions per department
  └─ Rank departments
  ↓
Insight Agent
  ├─ Identify high-risk patients
  ├─ Identify top readmission departments
  └─ Generate explanations
  ↓
FINAL REPORT / DASHBOARD OUTPUT
  ↓
END
