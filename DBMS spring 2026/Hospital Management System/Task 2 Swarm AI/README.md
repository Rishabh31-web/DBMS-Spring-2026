# Task 2: Swarm-Based Agentic AI for Patient Readmission Analysis

## Objective
To build a working swarm-based agentic AI system that analyzes patient readmission rates and identifies departments responsible for repeated admissions.

## System Design
The system is composed of multiple autonomous agents working collaboratively:

- **Orchestrator Agent:** Controls execution flow
- **Data Agent:** Fetches data from the hospital database
- **Readmission Agent:** Calculates patient readmission counts
- **Department Agent:** Aggregates department-wise statistics
- **Insight Agent:** Generates human-readable insights

## How to Run
```bash
python main.py
