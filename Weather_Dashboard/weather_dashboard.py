import requests
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 28.6139,
    "longitude": 77.2090,
    "current": [
        "temperature_2m",
        "relative_humidity_2m",
        "pressure_msl",
        "wind_speed_10m"
    ],
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation_probability",
        "wind_speed_10m",
        "pressure_msl"
    ]
}

response = requests.get(url, params=params)

data = response.json()

hourly = data["hourly"]

weather_df = pd.DataFrame({
    "Time": hourly["time"],
    "Temperature": hourly["temperature_2m"],
    "Humidity": hourly["relative_humidity_2m"],
    "Rain_Probability": hourly["precipitation_probability"],
    "Wind_Speed": hourly["wind_speed_10m"],
    "Pressure": hourly["pressure_msl"]
})

data_folder = BASE_DIR / "data"
data_folder.mkdir(exist_ok=True)

weather_df.to_csv(
    data_folder / "weather_data.csv",
    index=False
)

print("CSV saved successfully!")

plt.figure(figsize=(12,6))

plt.plot(
    weather_df["Time"][:48],
    weather_df["Temperature"][:48]
)

plt.title("Temperature Trend")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")

plt.xticks(rotation=45)

plt.tight_layout()

charts_folder = BASE_DIR / "charts"
charts_folder.mkdir(exist_ok=True)

plt.savefig(
    charts_folder / "temperature.png"
)

plt.close()
plt.figure(figsize=(12,6))

plt.plot(
    weather_df["Time"][:48],
    weather_df["Humidity"][:48]
)

plt.title("Humidity Trend")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")

plt.xticks(rotation=45)

plt.tight_layout()


plt.savefig(
    charts_folder / "humidity.png"
)


plt.close()

plt.figure(figsize=(12,6))

plt.plot(
    weather_df["Time"][:48],
    weather_df["Rain_Probability"][:48]
)

plt.title("Rain Probability Trend")
plt.xlabel("Time")
plt.ylabel("Probability (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    charts_folder / "rain_probability.png"
)


plt.close()

plt.figure(figsize=(12,6))

plt.plot(
    weather_df["Time"][:48],
    weather_df["Wind_Speed"][:48]
)

plt.title("Wind Speed Trend")
plt.xlabel("Time")
plt.ylabel("Wind Speed (km/h)")

plt.xticks(rotation=45)

plt.tight_layout()


plt.savefig(
    charts_folder / "wind_speed.png"
)

plt.close()

max_temp = weather_df["Temperature"].max()
min_temp = weather_df["Temperature"].min()
avg_temp = weather_df["Temperature"].mean()

max_humidity = weather_df["Humidity"].max()
max_rain = weather_df["Rain_Probability"].max()


# Create dashboard layout
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Temperature
axs[0, 0].plot(
    weather_df["Time"][:48],
    weather_df["Temperature"][:48]
)
axs[0, 0].set_title("Temperature Trend")
axs[0, 0].tick_params(axis='x', rotation=45)

# Humidity
axs[0, 1].plot(
    weather_df["Time"][:48],
    weather_df["Humidity"][:48]
)
axs[0, 1].set_title("Humidity Trend")
axs[0, 1].tick_params(axis='x', rotation=45)

# Rain Probability
axs[1, 0].plot(
    weather_df["Time"][:48],
    weather_df["Rain_Probability"][:48]
)
axs[1, 0].set_title("Rain Probability")
axs[1, 0].tick_params(axis='x', rotation=45)

# Wind Speed
axs[1, 1].plot(
    weather_df["Time"][:48],
    weather_df["Wind_Speed"][:48]
)
axs[1, 1].set_title("Wind Speed Trend")
axs[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()

plt.savefig (
    charts_folder / "weather_dashboard.png",
    dpi=300
)


plt.close()

print("Dashboard created successfully!")

print("\nWEATHER ANALYTICS")
print("----------------------")
print(f"Maximum Temperature: {max_temp:.1f} °C")
print(f"Minimum Temperature: {min_temp:.1f} °C")
print(f"Average Temperature: {avg_temp:.1f} °C")
print(f"Maximum Humidity: {max_humidity}%")
print(f"Highest Rain Probability: {max_rain}%")

print("\nWEATHER ALERTS")
print("----------------------")

if weather_df["Temperature"].max() > 40:
    print("HEAT ALERT: Temperature may exceed 40°C")

if weather_df["Rain_Probability"].max() > 30:
    print("RAIN ALERT: High chance of rainfall expected")

if weather_df["Wind_Speed"].max() > 12:
    print("WIND ALERT: Strong winds expected")