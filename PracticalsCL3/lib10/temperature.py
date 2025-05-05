import pandas as pd
from collections import defaultdict
from datetime import datetime

# Load dataset
df = pd.read_csv("synthetic_weather_data_full.csv")

# Print columns to debug
print(df.columns)

# Ensure no leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# --- MAP STEP: Extract (year, temperature) pairs ---
year_temp = defaultdict(list)
for _, row in df.iterrows():
    date_time = datetime.strptime(row['Date_Time'], "%d-%m-%Y %H:%M")
    year = date_time.year
    year_temp[year].append(row['Temperature_C'])

# --- REDUCE STEP: Calculate average temperature for each year ---
avg_temp_by_year = {}
for year, temps in year_temp.items():
    avg_temp_by_year[year] = sum(temps) / len(temps)

# --- Determine coolest and hottest year ---
coolest_year = min(avg_temp_by_year, key=avg_temp_by_year.get)
hottest_year = max(avg_temp_by_year, key=avg_temp_by_year.get)

print("Average Temperature by Year:")
for year, avg in avg_temp_by_year.items():
    print(f"{year}: {avg:.2f}°C")

print(f"\nCoolest Year: {coolest_year} ({avg_temp_by_year[coolest_year]:.2f}°C)")
print(f"Hottest Year: {hottest_year} ({avg_temp_by_year[hottest_year]:.2f}°C)")
