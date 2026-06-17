# Weather Intelligence & Predictive Analytics Platform
## Live Project Structure

This project consists of 3 integrated modules:

1. Weather Dashboard (API + Visualization)
2. NLP Weather Chatbot
3. Machine Learning Rainfall Prediction Engine

## Overview

A comprehensive weather analytics platform that combines real-time weather data collection, automated reporting, natural language interaction, and machine learning-based rainfall prediction.

## Live Demo

Streamlit Deployment:
https://weather-intelligence-platform-5vvluappnpddpbp3wwrnb2y.streamlit.app

## Features

### Weather Analytics Dashboard

* Real-time weather data collection using Open-Meteo API
* Weather data preprocessing and storage
* Temperature, humidity, rainfall, pressure, and wind analysis
* Automated visualization dashboards

### PDF Reporting System

* Automated weather report generation
* Embedded analytics and visual charts
* Professional PDF export

### NLP Weather Chatbot

* Natural language weather queries
* Intent detection using NLTK
* Weather summaries, alerts, and recommendations


![alt text](image.png)
![alt text](image-1.png)

### Rainfall Prediction Engine

* Dataset Size: 145,460 records  
* Logistic Regression, Decision Tree, Random Forest, and XGBoost models
* Best Performing Model: XGBoost Classifier
* Accuracy: 85.85%
* ROC-AUC Score: 0.889

## Technologies Used

* Python
* Pandas
* Matplotlib
* NLTK
* Scikit-Learn
* XGBoost
* ReportLab
* Open-Meteo API

## Results

* Automated Weather Dashboard
* NLP-Based Weather Assistant
* Machine Learning Rainfall Prediction
* Weather Analytics PDF Reports

## Installation & Setup

* Clone the repository
* Install dependencies:
   pip install -r requirements.txt
* Run modules individually:
   - Weather Dashboard → weather_dashboard.py
   - Chatbot → chatbot.py
   - ML Notebook → weather_ml.ipynb

## Future Enhancements

* Streamlit Web Application
* Deep Learning Forecasting Models
* Real-Time Weather Monitoring
* Cloud Deployment
