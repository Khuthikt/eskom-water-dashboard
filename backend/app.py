# app.py
from flask import Flask, jsonify, render_template
import sqlite3

# ===== NEW IMPORTS (WEATHER ONLY) =====
import openmeteo_requests
import requests_cache
from retry_requests import retry
from datetime import datetime

DB_PATH = "db/dashboard.db"

app = Flask(__name__)

# =====================================
# DATABASE HELPER
# =====================================
def query_db(query, args=()):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(query, args)
    results = [dict(row) for row in c.fetchall()]
    conn.commit()
    conn.close()
    return results

# =====================================
# WEATHER API SETUP (OPEN-METEO)
# =====================================
cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

def update_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": -26.2023,
        "longitude": 28.0436,
        "current": "temperature_2m"
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    current = response.Current()
    temperature = round(current.Variables(0).Value(), 1)

    today = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # prevent duplicates
    c.execute("DELETE FROM weather WHERE date = ?", (today,))
    c.execute(
        "INSERT INTO weather (date, temperature) VALUES (?, ?)",
        (today, temperature)
    )

    conn.commit()
    conn.close()

# =====================================
# ROUTES (UNCHANGED)
# =====================================
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/weather")
def get_weather():
    update_weather()  # 🔥 ONLY ADDITION
    return jsonify(query_db("SELECT * FROM weather ORDER BY date ASC"))

@app.route("/api/water")
def get_water():
    return jsonify(query_db("SELECT * FROM water"))

@app.route("/api/cooling")
def get_cooling():
    return jsonify(query_db("SELECT * FROM cooling"))

@app.route("/api/leaks")
def get_leaks():
    return jsonify(query_db("SELECT * FROM leaks"))

@app.route("/api/predictive")
def get_predictive():
    return jsonify(query_db("SELECT * FROM predictive ORDER BY date ASC"))

@app.route("/api/reports")
def get_reports():
    return jsonify(query_db("SELECT * FROM reports"))

@app.route("/api/alerts")
def get_alerts():
    return jsonify(query_db("SELECT * FROM alerts ORDER BY level DESC"))

@app.route("/api/pending_maintenance")
def get_pending_maintenance():
    return jsonify(query_db("SELECT * FROM pending_maintenance"))

@app.route("/api/technicians")
def get_technicians():
    return jsonify(query_db("SELECT * FROM technicians"))

@app.route("/api/system_status")
def get_system_status():
    return jsonify(query_db("SELECT * FROM system_status"))

# =====================================
if __name__ == "__main__":
    print("Dashboard running at http://127.0.0.1:5000/")
    app.run(debug=True)
