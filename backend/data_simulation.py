import random
import pandas as pd
from datetime import datetime, timedelta

def simulate_weather_data(days=7):
    base_temp = 25
    data = []
    for i in range(days):
        date = datetime.now() - timedelta(days=i)
        temp = base_temp + random.randint(-5,5)
        humidity = random.randint(40,80)
        data.append({"date": date.strftime("%Y-%m-%d"), "temperature": temp, "humidity": humidity})
    return pd.DataFrame(data)

def simulate_water_usage(days=7):
    towers = ["Tower 1", "Tower 2", "Tower 3"]
    data = []
    for t in towers:
        usage = random.uniform(10,25)
        data.append({"tower": t, "usage": round(usage,2)})
    return pd.DataFrame(data)

def simulate_cooling_tower():
    towers = ["Tower 1", "Tower 2", "Tower 3"]
    data = []
    for t in towers:
        temp = random.randint(25,40)
        level = random.randint(50,100)
        data.append({"tower": t, "temperature": temp, "water_level": level})
    return pd.DataFrame(data)

def simulate_leaks():
    towers = ["Tower 1", "Tower 2", "Tower 3"]
    data = []
    for t in towers:
        leaks = random.randint(0,3)
        water_lost = round(random.uniform(0,5),2)
        pressure = random.randint(80,120)
        data.append({"tower": t, "leaks": leaks, "water_lost": water_lost, "pressure": pressure})
    return pd.DataFrame(data)

def simulate_predictive(days=7):
    data = []
    for i in range(days):
        date = datetime.now() + timedelta(days=i)
        predicted_usage = round(random.uniform(10,25),2)
        rain = random.randint(0,50)
        load_shedding = random.choice(["None","Stage 1","Stage 2"])
        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "predicted_usage": predicted_usage,
            "rain": rain,
            "load_shedding": load_shedding
        })
    return pd.DataFrame(data)

def simulate_reports():
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    data = []
    for m in months:
        count = random.randint(5,20)
        data.append({"month": m, "count": count})
    return pd.DataFrame(data)
