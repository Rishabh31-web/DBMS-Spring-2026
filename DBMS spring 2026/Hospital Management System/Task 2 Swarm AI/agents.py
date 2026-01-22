from collections import defaultdict
from db import get_connection

# ---------------- ORCHESTRATOR ----------------
class OrchestratorAgent:
    def run(self):
        print("\n🧠 Orchestrator: Starting Swarm...\n")

        data_agent = DataAgent()
        raw_data = data_agent.fetch_data()

        readmission_agent = ReadmissionAgent()
        patient_stats = readmission_agent.calculate(raw_data)

        dept_agent = DepartmentAgent()
        dept_stats = dept_agent.analyze(raw_data)

        insight_agent = InsightAgent()
        insight_agent.report(patient_stats, dept_stats)


# ---------------- DATA AGENT ----------------
class DataAgent:
    def fetch_data(self):
        print("📊 DataAgent: Fetching data from DB...")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            p.PatientID,
            a.AppointmentID,
            d.DepartmentName
        FROM Patient p
        JOIN Appointment a ON p.PatientID = a.PatientID
        JOIN Doctor doc ON a.DoctorID = doc.DoctorID
        JOIN Department d ON doc.DepartmentID = d.DepartmentID
        """

        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        print(f"📊 DataAgent: Retrieved {len(data)} records\n")
        return data


# ---------------- READMISSION AGENT ----------------
class ReadmissionAgent:
    def calculate(self, data):
        print("🔁 ReadmissionAgent: Calculating readmissions...")

        visits = defaultdict(int)

        for row in data:
            visits[row["PatientID"]] += 1

        readmissions = {
            pid: count - 1
            for pid, count in visits.items()
            if count > 1
        }

        print("🔁 ReadmissionAgent: Done\n")
        return readmissions


# ---------------- DEPARTMENT AGENT ----------------
class DepartmentAgent:
    def analyze(self, data):
        print("🏥 DepartmentAgent: Analyzing department load...")

        dept_counts = defaultdict(int)

        for row in data:
            dept_counts[row["DepartmentName"]] += 1

        print("🏥 DepartmentAgent: Done\n")
        return dept_counts


# ---------------- INSIGHT AGENT ----------------
class InsightAgent:
    def report(self, patient_stats, dept_stats):
        print("📈 InsightAgent: Generating insights...\n")

        print("🔴 Top Patients by Readmissions:")
        for pid, count in sorted(patient_stats.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"PatientID {pid} → {count} readmissions")

        print("\n🏥 Department with Highest Readmissions:")
        top_dept = max(dept_stats, key=dept_stats.get)
        print(f"{top_dept} → {dept_stats[top_dept]} total visits")

        print("\n✅ Swarm Analysis Complete")
