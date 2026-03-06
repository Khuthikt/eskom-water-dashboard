Functional Requirements
FR1: Real-Time Monitoring

System shall collect sensor readings every 5 minutes from each cooling tower sensor.

System shall display real-time water consumption on the dashboard.

System shall store sensor readings with timestamp in db/dashboard.db.

System shall show historical data for the last 30 days.
*************************************************************************

FR2: Anomaly Detection

System shall detect abnormal readings:

Flow spikes → possible leaks

Pressure drops → potential equipment failure

System shall generate alerts within 60 seconds of detecting anomalies.

System shall flag anomalies only after verifying at least 3 consecutive readings to prevent false positives.
**************************************************************************

FR3: Predictive Maintenance

System shall predict maintenance needs 3–5 days in advance for filters and pumps.

System shall indicate confidence levels (0–100%) for predictions.

System shall update pending maintenance tasks automatically in the dashboard sidebar.
**************************************************************************
FR4: Technician Workflow

System shall assign maintenance tasks to available technicians automatically.

System shall track task progress (New → In Progress → Complete).

System shall notify technicians of their assigned tasks (future enhancement: SMS/email).

System shall display technicians and their availability in the sidebar.
**************************************************************************

FR5: Alerts & System Status

System shall display active alerts with severity levels in the dashboard sidebar.

System shall show overall system status (operational, degraded, offline) in the sidebar.

System shall allow technicians to resolve alerts, updating the database accordingly.
***************************************************************************

FR6: Data Management

System shall store at least 30 days of sensor readings for analysis.

System shall allow export of data (JSON, CSV) for reporting.

System shall maintain data integrity and consistency across all tables.
****************************************************************************

FR7: Dashboard

System shall display real-time and historical data for all towers.

System shall show interactive graphs using Chart.js.

System shall be responsive for multiple screen sizes.

System shall provide sidebar navigation for alerts, technicians, system status, and maintenance.

**************************************************************************
**************************************************************************

Non-Functional Requirements
NFR1: Performance

Dashboard load time < 2 seconds.

Alert generation < 60 seconds.

Database queries < 1 second.

Predictions generated < 10 seconds.
**************************************************************************

NFR2: Availability

System uptime ≥ 99%.

Daily database backup at 2:00 AM.

Graceful degradation if data simulation or backend fails.
**************************************************************************

NFR3: Security

Local SQLite database for development.

Future production: user authentication, role-based access, HTTPS, and POPIA compliance.
**************************************************************************

NFR4: Scalability

Support 1–100 cooling towers.

Support 10–100 sensors per tower.

Handle millions of readings without performance loss.
**************************************************************************

NFR5: Reliability

Zero data loss tolerated.

Graceful error handling with clear user feedback.
**************************************************************************

NFR6: Usability

Dashboard intuitive; no training required.

Error messages clear and actionable.

Sidebar navigation easy to understand.
**************************************************************************

NFR7: Maintainability

Code documented and modular.

Follows SDLC best practices.

Easy to extend with new sensors, towers, or features.
***************************************************************************

NFR8: Compatibility

Python 3.8+

Windows, Mac, Linux

Modern browsers: Chrome, Firefox, Edge
**************************************************************************
**************************************************************************

Hardware Requirements
Server (Backend)

CPU: 2+ cores

RAM: 4 GB minimum

Storage: 50+ GB for historical data

OS: Windows, Mac, Linux
**************************

Client (Dashboard User)

Modern computer

Web browser

Internet connection optional (for simulated data)
***************************

Sensors

Eskom-compatible IoT sensors

Data sent every 5 minutes via HTTP/REST
*****************************************************************************
*****************************************************************************
Software Requirements
Development Environment

Python 3.8+

VS Code or other text editor

SQLite3

Git (for version control)
**************************

Production Environment

Python 3.8+ runtime

SQLite database

Flask web server (optional)
***************************
Libraries/Dependencies
Flask==2.3.2          # Backend web framework
sqlite3 (built-in)     # Database
json (built-in)        # Data handling
datetime (built-in)    # Timestamping
Chart.js 3.9.1         # Frontend graphs
**************************
**************************
User Stories
US1: Monitor Water Consumption

As a power station operator
I want to see real-time water consumption
So that I can track usage and detect anomalies
Acceptance Criteria:
Dashboard shows flow rate per tower
Updates every 5 minutes
Historical data for 24 hours visible
Comparisons to baseline averages
****************************

US2: Receive Alerts
As a maintenance technician
I want to receive immediate alerts for anomalies
So that I can prevent water loss or equipment damage
Acceptance Criteria:
Alerts appear within 60 seconds
Show tower and sensor affected
Display estimated severity
Recommended actions included
*****************************

US3: Predict Maintenance
As a maintenance supervisor
I want to know predicted maintenance tasks 3–5 days ahead
So that I can schedule work efficiently
Acceptance Criteria:
Tasks appear in dashboard sidebar
Confidence levels shown
Technicians notified of assignments
*****************************

US4: Track Technicians
As a supervisor
I want to see technician availability and assignments
So that I can manage workforce effectively
Acceptance Criteria:
Sidebar lists all technicians
Tasks assigned and status visible
Can reassign tasks manually
****************************

US5: Monitor System Status
As a operator
I want to see overall system health
So that I know whether the system is operational
Acceptance Criteria:
Sidebar shows status: Operational / Degraded / Offline
Updates automatically with data simulation























