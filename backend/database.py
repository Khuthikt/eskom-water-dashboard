# database.py
import sqlite3
from data_simulation import simulate_weather_data, simulate_water_usage, simulate_cooling_tower, simulate_leaks, simulate_predictive, simulate_reports

DB_PATH = "db/dashboard.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        temperature INTEGER,
        humidity INTEGER
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS water (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tower TEXT,
        usage REAL
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS cooling (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tower TEXT,
        temperature INTEGER,
        water_level INTEGER
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS leaks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tower TEXT,
        leaks INTEGER,
        water_lost REAL,
        pressure INTEGER
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS predictive (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        predicted_usage REAL,
        rain INTEGER,
        load_shedding TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        month TEXT,
        count INTEGER
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level TEXT,
        tower TEXT,
        description TEXT,
        action TEXT,
        estimated_loss TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS pending_maintenance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tower TEXT,
        task TEXT,
        status TEXT,
        assigned TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS technicians (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        tasks TEXT,
        status TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS system_status (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        component TEXT,
        status TEXT,
        notes TEXT
    )''')

    conn.commit()
    conn.close()

def populate_tables():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Weather
    for row in simulate_weather_data(7).to_dict(orient="records"):
        c.execute("INSERT INTO weather (date, temperature, humidity) VALUES (?,?,?)",
                  (row["date"], row["temperature"], row["humidity"]))

    # Water
    for row in simulate_water_usage().to_dict(orient="records"):
        c.execute("INSERT INTO water (tower, usage) VALUES (?,?)",
                  (row["tower"], row["usage"]))

    # Cooling
    for row in simulate_cooling_tower().to_dict(orient="records"):
        c.execute("INSERT INTO cooling (tower, temperature, water_level) VALUES (?,?,?)",
                  (row["tower"], row["temperature"], row["water_level"]))

    # Leaks
    for row in simulate_leaks().to_dict(orient="records"):
        c.execute("INSERT INTO leaks (tower, leaks, water_lost, pressure) VALUES (?,?,?,?)",
                  (row["tower"], row["leaks"], row["water_lost"], row["pressure"]))

    # Predictive
    for row in simulate_predictive(7).to_dict(orient="records"):
        c.execute("INSERT INTO predictive (date, predicted_usage, rain, load_shedding) VALUES (?,?,?,?)",
                  (row["date"], row["predicted_usage"], row["rain"], row["load_shedding"]))

    # Reports
    for row in simulate_reports().to_dict(orient="records"):
        c.execute("INSERT INTO reports (month, count) VALUES (?,?)",
                  (row["month"], row["count"]))

    # Alerts
    alerts = [
        ("CRITICAL","Tower 1","Leak Detected","Check immediately","500 L/minute"),
        ("WARNING","Tower 2","Pressure Drop","Maintenance in 2-3 days","-"),
        ("INFO","Tower 3","Scheduled Maintenance","Assigned: Khuthadzo","Tomorrow 10:00 AM")
    ]
    c.executemany("INSERT INTO alerts (level,tower,description,action,estimated_loss) VALUES (?,?,?,?,?)", alerts)

    # Pending maintenance
    pending = [
        ("Tower 1","Stop Leak","New","Unassigned"),
        ("Tower 2","Filter Cleaning","Assigned","Tshepang"),
        ("Tower 3","Maintenance Check","In Progress","Ahmed Hassan")
    ]
    c.executemany("INSERT INTO pending_maintenance (tower,task,status,assigned) VALUES (?,?,?,?)", pending)

    # Technicians
    technicians = [
        ("Khuthadzo","1 Task","Available"),
        ("Oratile","2 Tasks (Busy)","On Duty"),
        ("Khorombi","1 Task (Away)","Off Duty")
    ]
    c.executemany("INSERT INTO technicians (name,tasks,status) VALUES (?,?,?)", technicians)

    # System Status
    system_status = [
        ("Database","✓ Connected","All OK"),
        ("Weather API","✓ Connected","All OK"),
        ("ML Model","✓ Running","All OK"),
        ("Sensor Network","⚠ 1 Offline","Check sensor 3")
    ]
    c.executemany("INSERT INTO system_status (component,status,notes) VALUES (?,?,?)", system_status)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    populate_tables()
    print("Database created and populated successfully!")
