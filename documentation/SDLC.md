SDLC PLAN – ESKOM WATER ANALYTICS & PREDICTIVE MAINTENANCE PLATFORM

Project Overview
Name: Eskom Water Analytics & Predictive Maintenance
Duration: 5 days (Feb 11–16, 2026)
Status: Complete & Operational
Version: 1.0

SDLC Phases
Phase 1: Requirements & Planning (Day 1: Feb 11)
Duration: 1 day
Status: ✓ COMPLETE

Activities:
Define system requirements
Document problem statement and business case
Plan folder structure and features
Identify stakeholders
Deliverables:
Requirements document (REQUIREMENTS.md)
Folder structure finalized
Project timeline create

Key Decisions:
SQLite for database (db/dashboard.db)
Python/Flask backend (backend/app.py)
HTML/CSS/JS frontend (templates/dashboard.html)
Sidebar features: active alerts, technicians, system status, pending maintenance


Phase 2: Analysis & Design (Day 2: Feb 12)
Duration: 1 day
Status: ✓ COMPLETE

Activities:
Design system architecture
Create database schema and table relationships
Design dashboard layout and sidebar features
Document data flows and update mechanisms

Deliverables:
Database schema with 8 tables
Dashboard and sidebar mockups
Data flow documentation

Design Decisions:
Modular design: backend, frontend, database separated
Real-time simulation for testing
Normalized database to prevent redundancy



Phase 3: Development (Days 3–4: Feb 13-14)

Duration: 2 days
Status: ✓ COMPLETE

Activities:
Develop database.py for DB operations
Code data_simulation.py to generate realistic readings
Implement app.py backend logic
Build dashboard.html with sidebar features
Style using style.css


Deliverables:
Operational database (dashboard.db)
Backend scripts (app.py, data_simulation.py, database.py)
Dashboard with sidebar for alerts, maintenance, technicians, system status
Fully functional data simulation

Development Approach:
Iterative and modular
Test-driven: database, backend, frontend verified separately
Code documented with comments

Phase 4: Testing (Day 5: Feb 15-16)
Duration: 1 day
Status: ✓ COMPLETE

Activities:
Unit testing for database and backend scripts
Integration testing of dashboard + sidebar updates
Simulated alerts and maintenance workflow testing
Performance testing (<2s load, <60s alert generation)

Test Cases:

| Component | Test                  | Expected                       | Actual              | Status |
| --------- | --------------------- | ------------------------------ | ------------------- | ------ |
| Database  | Create tables         | 8 tables                       | 8 tables            | ✓      |
| Database  | Insert simulated data | 1,620+ readings                | 1,620+ readings     | ✓      |
| Backend   | Data simulation       | Readings generated             | Readings generated  | ✓      |
| Backend   | Alerts triggered      | Alerts appear in sidebar       | Alerts appear       | ✓      |
| Dashboard | Load time             | <2s                            | ~1s                 | ✓      |
| Dashboard | Sidebar updates       | Alerts/technicians/maintenance | Correctly displayed | ✓      |

Test Coverage: 100% critical functions; positive & edge cases tested


Phase 5: Deployment (Feb 17)
Duration: Presentation day
Status: ✓ READY

Activities:
Final verification of all components
Dashboard demo with active alerts and maintenance simulation
Present folder structure, database, backend, and frontend
Answer stakeholder questions

Deliverables:
Fully operational system
Complete documentation (README.md, REQUIREMENTS.md, SDLC.md)
Live demo ready


















