import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(
    page_title="Weather Intelligence Platform",
    page_icon="🌦",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

st.title("🌦 Weather Intelligence & Predictive Analytics Platform")

st.markdown("""
A complete end-to-end weather analytics system combining:

✅ Real-Time Weather Data Collection  
✅ Interactive Weather Dashboard  
✅ Automated PDF Reporting  
✅ NLP Weather Chatbot  
✅ Machine Learning Rainfall Prediction  

Built using Python, Scikit-Learn, XGBoost, NLTK, Pandas, and Streamlit.
""")

# ==========================
# PROJECT METRICS
# ==========================

st.header("📊 Project Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Dataset Size", "145,460")

with col2:
    st.metric("Best Model", "XGBoost")

with col3:
    st.metric("Accuracy", "85.85%")

with col4:
    st.metric("ROC-AUC", "0.889")

# ==========================
# WEATHER DASHBOARD
# ==========================

st.header("🌦 Weather Analytics Dashboard")

dashboard_path = BASE_DIR / "Weather_Dashboard" / "charts" / "weather_dashboard.png"

dashboard_img = Image.open(dashboard_path)

st.image(
    dashboard_img,
    use_container_width=True
)

st.markdown("""
The dashboard visualizes:

- Temperature Trends
- Humidity Trends
- Rainfall Probability
- Wind Speed Analysis
""")

# ==========================
# CHATBOT SECTION
# ==========================

st.header("🤖 NLP Weather Chatbot")

st.markdown("""
Features:

- Natural Language Processing using NLTK
- Intent Detection
- Weather Summaries
- Alerts & Recommendations
- Interactive Weather Queries

Example Queries:

- What's the weather summary?
- Any temperature differences?
- Weather advice
- Rain alerts
""")

# ==========================
# MACHINE LEARNING
# ==========================

st.header("🧠 Rainfall Prediction Engine")

st.markdown("""
Models Evaluated:

- Logistic Regression → 83.75%
- Decision Tree → 78.51%
- Random Forest → 85.62%
- XGBoost → 85.85% (Best)
""")

# ==========================
# FEATURE IMPORTANCE
# ==========================

st.subheader("📈 Feature Importance")

feature_path = (
    BASE_DIR
    / "Weather_Prediction_ML_Engine"
    / "outputs"
    / "feature_importance_xgboost.png"
)

st.image(
    Image.open(feature_path),
    use_container_width=True
)

# ==========================
# CONFUSION MATRIX
# ==========================

st.subheader("🔍 Confusion Matrix")

cm_path = (
    BASE_DIR
    / "Weather_Prediction_ML_Engine"
    / "outputs"
    / "confusion_matrix.png"
)

st.image(
    Image.open(cm_path),
    use_container_width=True
)

# ==========================
# ROC CURVE
# ==========================

st.subheader("📉 ROC Curve")

roc_path = (
    BASE_DIR
    / "Weather_Prediction_ML_Engine"
    / "outputs"
    / "roc_curve_xgboost.png"
)

st.image(
    Image.open(roc_path),
    use_container_width=True
)

# ==========================
# RESULTS
# ==========================

st.header("🏆 Key Results")

st.success(
    """
    • Dataset Size: 145,460 records
    
    • Best Model: XGBoost
    
    • Accuracy: 85.85%
    
    • ROC-AUC Score: 0.889
    
    • Successfully predicts rainfall using weather parameters
    """
)

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.markdown(
    "Developed as part of an AI/ML Weather Intelligence Project using Python and Machine Learning."
)