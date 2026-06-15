from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent / "Weather_Dashboard"
csv_path = BASE_DIR / "data" / "weather_data.csv"


df = pd.read_csv(csv_path)

print("CSV loaded successfully!")

max_temp = df["Temperature"].max()
min_temp = df["Temperature"].min()
avg_temp = round(df["Temperature"].mean(), 2)

max_humidity = df["Humidity"].max()
max_rain = df["Rain_Probability"].max()
max_wind = df["Wind_Speed"].max()


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


def preprocess(text):

    tokens = word_tokenize(text.lower())

    filtered = [
        word
        for word in tokens
        if word.isalnum() and word not in stop_words
    ]

    stemmed = [
        stemmer.stem(word)
        for word in filtered
    ]

    return stemmed
intents = {
    "greeting": [
        "hello", "hi", "hey"
    ],

    "temperature": [
        "temperature",
        "temp",
        "hot",
        "heat"
    ],

    "humidity": [
        "humidity",
        "moisture"
    ],

    "rain": [
        "rain",
        "umbrella",
        "precipitation"
    ],

    "wind": [
        "wind",
        "breeze"
    ],

    "alerts": [
        "alert",
        "alerts",
        "warning"
    ],

    "summary": [
        "summary",
        "forecast",
        "weather",
        "summarize",
        "overview",
        "report"

    ],
    "advice": [
        "advice",
        "recommend",
        "suggest"
    ],
    "thanks": [
        "thanks",
        "thank",
        "thanku",
        "thankyou"
    ]
    
}

def detect_intents(words):

    found = set()

    for intent, keywords in intents.items():

        for keyword in keywords:

            keyword = stemmer.stem(keyword)

            if any(keyword in w for w in words):
                found.add(intent)
                break

    return list(found)

def get_response(user_input):

    words = preprocess(user_input)

    found_intents = detect_intents(words)

    if not found_intents:
        return (
    "Sorry, I could not understand your question..\n"
    "Try asking about:\n"
    "- temperature\n"
    "- humidity\n"
    "- rain\n"
    "- wind\n"
    "- alerts\n"
    "- summary\n"
    "- weather advice"
    )
        

    response_parts = []

    if "greeting" in found_intents:
        response_parts.append(
            "Hello! I am your Weather Intelligence Assistant."
        )

    if "temperature" in found_intents:
        response_parts.append(
            f"Maximum Temperature: {max_temp}°C\n"
            f"Minimum Temperature: {min_temp}°C\n"
            f"Average Temperature: {avg_temp}°C"
        )

    if "humidity" in found_intents:
        response_parts.append(
            f"Maximum Humidity: {max_humidity}%"
        )

    if "rain" in found_intents:
        response_parts.append(
            f"Highest Rain Probability: {max_rain}%\n"
            f"Recommendation: Carry an umbrella if travelling."
        )

    if "wind" in found_intents:
        response_parts.append(
            f"Maximum Wind Speed: {max_wind} km/h"
        )

    if "alerts" in found_intents:

        alerts = []

        if max_temp > 40:
            alerts.append("🔥 Heat Alert")

        if max_rain > 30:
            alerts.append("🌧 Rain Alert")

        if max_wind > 12:
            alerts.append("💨 Wind Alert")
        if alerts:
            response_parts.append("\n".join(alerts))
        else:
            response_parts.append("No weather alerts at the moment.")
        

    if "summary" in found_intents:

        summary = (
            f"Weather Summary\n"
            f"Average Temperature: {avg_temp}°C\n"
            f"Maximum Humidity: {max_humidity}%\n"
            f"Rain Probability: {max_rain}%\n"
            f"Wind Speed: {max_wind} km/h\n"
        )

        if avg_temp > 35:
            summary += "\n🔥 Very hot weather expected."

        if max_rain > 30:
            summary += "\n🌧 Carry an umbrella."

        if max_wind > 12:
            summary += "\n💨 Strong winds may occur."

        response_parts.append(summary)

    if "advice" in found_intents:

        advice = []

        if max_temp > 38:
            advice.append("Stay hydrated and avoid direct sunlight.")

        if max_rain > 30:
            advice.append("Carry an umbrella.")

        if max_wind > 12:
            advice.append("Secure loose outdoor objects.")

        response_parts.append(
            "Weather Advice:\n" + "\n".join(advice)
        )
    if "thanks" in found_intents:
        response_parts.append(
            "You're welcome! Stay weather aware."
            )

    return "\n\n".join(response_parts)


print("=" * 50)
print("WEATHER INTELLIGENCE CHATBOT")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "bye":
        print("\nBot: Goodbye! Stay weather aware.")
        break

    response = get_response(user_input)

    print("\nBot:", response)