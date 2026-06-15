import pandas as pd
from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

BASE_DIR = Path(__file__).resolve().parent 

csv_path = BASE_DIR / "data" / "weather_data.csv"

df = pd.read_csv(csv_path)

data_folder = BASE_DIR / "data"
charts_folder = BASE_DIR / "charts"
# ---------------------------
# Load Weather Data
# ---------------------------

df = pd.read_csv(
    data_folder / "weather_data.csv"
)

# ---------------------------
# Analytics
# ---------------------------

max_temp = df["Temperature"].max()
min_temp = df["Temperature"].min()
avg_temp = round(df["Temperature"].mean(), 2)

max_humidity = df["Humidity"].max()
max_rain = df["Rain_Probability"].max()
max_wind = df["Wind_Speed"].max()

# ---------------------------
# Create PDF
# ---------------------------

reports_folder = Path(__file__).resolve().parent

pdf = SimpleDocTemplate(
    str(reports_folder / "Weather_Report.pdf")
)

styles = getSampleStyleSheet()

content = []

from datetime import datetime
today = datetime.now().strftime("%d-%m-%Y")
# Title

title = Paragraph(
    "Weather Intelligence Report",
    styles["Title"]
)

content.append(title)
content.append(Spacer(1, 20))
content.append(
    Paragraph(
        f"Generated on: {today}",
        styles["BodyText"]
    )
)

# Introduction

intro = Paragraph(
    "This report was generated automatically using weather forecast data obtained from the Open-Meteo API.",
    styles["BodyText"]
)

content.append(intro)
content.append(Spacer(1, 15))

# Statistics

stats = f"""
<b>Weather Statistics</b><br/><br/>
Maximum Temperature: {max_temp} °C<br/>
Minimum Temperature: {min_temp} °C<br/>
Average Temperature: {avg_temp} °C<br/>
Maximum Humidity: {max_humidity}%<br/>
Highest Rain Probability: {max_rain}%<br/>
Maximum Wind Speed: {max_wind} km/h
"""

content.append(
    Paragraph(stats, styles["BodyText"])
)

content.append(Spacer(1, 20))

# Alerts

alerts = []

if max_temp > 40:
    alerts.append("Heat Alert: Temperature may exceed 40°C")

if max_rain > 30:
    alerts.append("Rain Alert: Significant rainfall possible")

if max_wind > 12:
    alerts.append("Wind Alert: Strong winds expected")
    
alert_text = ""

for alert in alerts:
    alert_text += f"• {alert}<br/>"

# alert_text = "<br/>".join(alerts)

content.append(
    Paragraph(
        "<b>Weather Alerts</b><br/><br/>" + alert_text,
        styles["BodyText"]
    )
)

content.append(Spacer(1, 20))

from reportlab.platypus import PageBreak

content.append(PageBreak())

content.append(
    Paragraph(
        "Weather Dashboard",
        styles["Title"]
    )
)

content.append(Spacer(1, 20))
dashboard = Image(
    str(charts_folder / "weather_dashboard.png"),
    width= 500,
    height= 330
)

content.append(dashboard)

content.append(Spacer(1, 20))

# Conclusion

content.append(
    Paragraph(
        "This report provides weather insights and forecast trends based on Open-Meteo weather data.",
        styles["BodyText"]
    )
)

# Build PDF

pdf.build(content)

print("Weather_Report.pdf created successfully!")