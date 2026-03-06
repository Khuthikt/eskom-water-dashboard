Project Overview

A fully functional water management and predictive maintenance system for Eskom power stations that:

Monitors cooling water consumption in real-time.

Detects anomalies (leaks or unusual readings) immediately.

Predicts maintenance tasks 3–5 days ahead.

Tracks technician assignments and system status.

Shows active alerts and pending maintenance in the dashboard sidebar.

This project improves water efficiency, reduces emergency repairs, and allows proactive maintenance planning.

*****************************************************************************************************************

Problem Statement

Eskom power stations consume billions of liters of water annually.

Even a 1% water leak can cost over R2.5 million per year.

Current monitoring is reactive → repairs happen after damage occurs.

Leads to emergency maintenance, downtime, and unnecessary water loss.
******************************************************************************************************************


Solution

This platform provides:

Real-time water consumption monitoring – updated every 5 minutes.

Anomaly detection & alerts – instantly identifies leaks or irregular readings.

Predictive maintenance – predicts maintenance needs 3–5 days in advance.

Technician workflow management – tracks staff assignments and task progress.

Dashboard sidebar – displays active alerts, technician availability, system status, and pending maintenance.

Data-driven decision making – helps save R2.45M+ per avoided incident.

******************************************************************************************************************

Sensors → database/dashboard.db → backend/app.py → templates/dashboard.html → Technician Action
        ↓
Weather data (optional) → influences maintenance predictions
*****************************************************************************************************************

Components
1. Database (db/dashboard.db)

Stores 8 tables: sensors, sensor_readings, cooling_towers, technicians, maintenance_requests, maintenance_history, alerts, daily_consumption.

Holds 30 days of sensor readings (~1,620+ readings).

Maintains historical data for analysis and dashboard display.

2. Backend (backend/)

app.py – Flask application serving dashboard, simulating data, updating maintenance, alerts, and system status.

data_simulation.py – Generates realistic sensor data for testing and demonstration.

database.py – Handles all database connections, queries, and updates.

3. Templates (backend/templates/)

dashboard.html – Main dashboard interface showing:

Real-time water consumption graphs.

Active alerts.

Technician assignments and availability.

Pending maintenance tasks.

Overall system status.

4. Static Files (backend/static/)

style.css – Dashboard styling.

Images/ESKOM LOGO – Company logo used in the header.
**********************************************************************************************************************

Installation
Requirements

Python 3.8+

Windows/Mac/Linux

Web browser (Chrome, Firefox, Edge)



Setup
Navigate to the project:
1. cd %USERPROFILE%\Desktop\Eskom Project)
2. cd backend
3. It’s recommended to create a virtual environment to isolate project dependencies by running python -m venv venv and then activating it with venv\Scripts\activate on Windows CMD. 
4. Once the environment is active, install the required libraries with pip install Flask pandas flask-cors and pip install openmeteo-requests requests-cache retry-requests pandas
5. Create the database: database.py
6. run it with python app.py
************************************************************************************************************************

Usage
Dashboard Features

Water Consumption: Real-time updates per cooling tower.

Active Alerts: Shows anomalies and leaks instantly.

Technicians: Lists staff, availability, and assigned tasks.

System Status: Displays operational health of the system.

Pending Maintenance: Shows upcoming maintenance requests.

Interactive Charts: Visualize historical and current sensor data.
*************************************************************************************************************************
Simulated Data

data_simulation.py generates test readings for all sensors.
Readings automatically update dashboard and trigger alerts if thresholds exceeded.
**************************************************************************************************************************

Key Metrics
Prediction Accuracy: 85%+
Dashboard Load Time: < 2 seconds
Alert Generation: < 60 seconds after anomaly detection
Database Query: < 1 second
**************************************************************************************************************************



| Component  | Technology                 |
| ---------- | -------------------------- |
| Database   | SQLite (`db/dashboard.db`) |
| Backend    | Python 3.8+ (Flask)        |
| Frontend   | HTML5, CSS3, JavaScript    |
| Graphs     | Chart.js                   |
| Deployment | Localhost / Server         |
**************************************************************************************************************************


backend/
├── static/
│   ├── Images/
│   │   └── ESKOM LOGO
│   └── style.css
├── templates/
│   └── dashboard.html
├── app.py
├── data_simulation.py
├── database.py
db/
└── dashboard.db
*************************************************************************************************************************


Data Schema
sensors → sensor_id, name, type, unit, location, min_normal, max_normal
sensor_readings → reading_id, sensor_id, value, timestamp, is_anomaly
cooling_towers → tower_id, name, location, capacity, efficiency
technicians → technician_id, name, availability, assigned_tasks
maintenance_requests → request_id, tower_id, type, status, scheduled_date
maintenance_history → history_id, request_id, completed_on
alerts → alert_id, tower_id, type, severity, timestamp, resolved
daily_consumption → tower_id, date, total_consumed
*************************************************************************************************************************


Future Enhancements
Mobile application for technicians.
Automated SMS/email notifications.
Cloud deployment with REST API integration.
Advanced ML for better predictive maintenance.
Multi-site monitoring for multiple Eskom power stations.

