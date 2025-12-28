import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="CardioGuard | Health Risk Assessment",
    page_icon="💚",
    layout="wide"
)

# Load model
model = joblib.load("models/health_risk_dt.joblib")

# ========= THEME: BLACK BG + DARK GREEN GLASS BOXES =========
BLACK = "#000000"
DARK_GREEN = "#0A3D2C"
DARK_GREEN_2 = "#0F5239"
GREEN = "#14B07D"
GREEN_LIGHT = "#5EE6B8"
GREEN_NEON = "#00FF88"
WHITE = "#FFFFFF"
GREY = "#B0BEC5"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
html, body, [class*="css"] {{ font-family: 'Poppins', sans-serif; }}

/* Pure black background */
.stApp {{
  background: {BLACK};
}}

.block-container {{ max-width: 1300px; padding-top: 1rem; }}
[data-testid="stHeader"] {{ background: transparent; }}

/* ALL TEXT */
html, body, p, li, span, div, label, small {{ color: {GREY} !important; }}
h1, h2, h3, h4 {{ 
  color: {GREEN_LIGHT} !important; 
  font-weight: 800 !important; 
  text-shadow: 0 0 15px rgba(94, 230, 184, 0.4);
}}

/* HERO BANNER with heartbeat line */
.hero {{
  position: relative;
  border-radius: 24px;
  padding: 40px 48px;
  background: linear-gradient(135deg, {DARK_GREEN} 0%, {DARK_GREEN_2} 100%);
  border: 3px solid {GREEN};
  box-shadow: 0 0 50px rgba(20, 176, 125, 0.4), 0 20px 60px rgba(0,0,0,0.8);
  overflow: hidden;
  margin-bottom: 28px;
}}

/* Heartbeat animation */
@keyframes heartbeat {{
  0%, 100% {{ transform: translateY(0); }}
  10% {{ transform: translateY(-8px); }}
  20% {{ transform: translateY(0); }}
  30% {{ transform: translateY(-4px); }}
  40%, 100% {{ transform: translateY(0); }}
}}

.heart-pulse {{
  position: absolute;
  right: 40px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 110px;
  opacity: 0.12;
  filter: drop-shadow(0 0 30px {GREEN_NEON});
  animation: heartbeat 2s ease-in-out infinite;
}}

.hero-badge {{
  display: inline-block;
  padding: 8px 20px;
  background: linear-gradient(135deg, {GREEN} 0%, {GREEN_LIGHT} 100%);
  color: {BLACK} !important;
  font-weight: 900;
  border-radius: 999px;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: 16px;
  box-shadow: 0 4px 15px rgba(20, 176, 125, 0.5);
}}

.hero-title {{
  font-size: 3rem;
  font-weight: 900;
  color: {WHITE} !important;
  margin-bottom: 12px;
  line-height: 1.2;
}}

.hero-sub {{
  color: {GREEN_LIGHT} !important;
  font-size: 1.15rem;
  line-height: 1.7;
  opacity: 0.95;
}}

/* DARK GREEN GLASS BOXES */
.glass-box {{
  border-radius: 20px;
  background: linear-gradient(135deg, rgba(10, 61, 44, 0.85) 0%, rgba(15, 82, 57, 0.75) 100%);
  border: 2px solid {GREEN};
  box-shadow: 0 10px 40px rgba(0,0,0,0.7), 0 0 30px rgba(20, 176, 125, 0.2);
  backdrop-filter: blur(10px);
  padding: 32px;
  margin-bottom: 24px;
}}

.box-header {{
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 20px;
}}

.box-icon {{
  font-size: 2.2rem;
  filter: drop-shadow(0 0 10px {GREEN_NEON});
}}

.box-title {{
  font-size: 1.5rem;
  font-weight: 800;
  color: {GREEN_LIGHT} !important;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 1px;
}}

.box-subtitle {{
  color: {GREY} !important;
  font-size: 0.95rem;
  margin-bottom: 20px;
  opacity: 0.85;
}}

/* Inputs */
.stNumberInput input,
.stSelectbox select,
.stTextInput input {{
  background: rgba(0, 0, 0, 0.7) !important;
  border: 2px solid {GREEN} !important;
  border-radius: 12px !important;
  color: {GREEN_LIGHT} !important;
  font-weight: 700 !important;
}}

.stSelectbox div[data-baseweb="select"] > div {{
  background: rgba(0, 0, 0, 0.7) !important;
  border: 2px solid {GREEN} !important;
}}

.stSelectbox span {{
  color: {GREEN_LIGHT} !important;
  font-weight: 800 !important;
}}

/* Buttons */
.stButton > button {{
  width: 100%;
  border: none;
  border-radius: 16px;
  padding: 1.2rem 1.8rem;
  font-weight: 900;
  font-size: 1.15rem;
  letter-spacing: 2px;
  color: {BLACK} !important;
  background: linear-gradient(135deg, {GREEN} 0%, {GREEN_LIGHT} 100%);
  box-shadow: 0 15px 40px rgba(20, 176, 125, 0.5);
  text-transform: uppercase;
}}

.stButton > button:hover {{
  transform: translateY(-3px);
  box-shadow: 0 20px 50px rgba(20, 176, 125, 0.7);
}}

/* Metrics */
[data-testid="stMetric"] {{
  background: rgba(10, 61, 44, 0.6);
  border: 2px solid {GREEN};
  border-radius: 16px;
  padding: 1.3rem;
  box-shadow: 0 8px 25px rgba(0,0,0,0.5);
}}

[data-testid="stMetricValue"] {{
  color: {GREEN_LIGHT} !important;
  font-weight: 900 !important;
  font-size: 2rem !important;
}}

[data-testid="stMetricLabel"] {{
  color: {GREY} !important;
  font-weight: 700 !important;
  text-transform: uppercase;
}}

/* Alerts */
.stAlert {{
  border-radius: 14px !important;
  border: 2px solid {GREEN} !important;
}}

/* Divider */
.divider {{
  height: 2px;
  background: linear-gradient(90deg, transparent, {GREEN}, transparent);
  margin: 32px 0;
}}

/* Info section */
.info-card {{
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid {GREEN};
  border-radius: 12px;
  padding: 16px;
  margin-top: 12px;
}}

.info-card p {{
  margin: 0;
  color: {GREY} !important;
  font-size: 0.9rem;
}}

/* Label icons */
label {{
  color: {GREEN_LIGHT} !important;
  font-weight: 700 !important;
}}
</style>
""", unsafe_allow_html=True)

# ========= HERO BANNER =========
st.markdown(f"""
<div class="hero">
  <div class="heart-pulse">💚</div>
  <div class="hero-badge">AI-Powered Risk Assessment</div>
  <div class="hero-title">💚 CardioGuard Health Monitor</div>
  <div class="hero-sub">
    Advanced machine learning system to assess your cardiovascular health risk. Get instant predictions based on clinical parameters.
  </div>
</div>
""", unsafe_allow_html=True)

# ========= BMI CALCULATOR BOX =========
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
st.markdown("""
<div class="box-header">
  <div class="box-icon">📏</div>
  <h2 class="box-title">BMI Calculator</h2>
</div>
<div class="box-subtitle">Don't know your BMI? Calculate it here first.</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    weight = st.number_input("⚖️ Weight (kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.1)
with col2:
    height = st.number_input("📐 Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
with col3:
    if height > 0:
        calculated_bmi = weight / ((height / 100) ** 2)
        st.metric("🧮 Your BMI", f"{calculated_bmi:.1f}")
    else:
        calculated_bmi = 25.0

st.markdown("""
<div class="info-card">
  <p><strong>BMI Categories:</strong> Underweight (&lt;18.5) | Normal (18.5-24.9) | Overweight (25-29.9) | Obese (≥30)</p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ========= HEALTH METRICS BOX =========
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
st.markdown("""
<div class="box-header">
  <div class="box-icon">🩺</div>
  <h2 class="box-title">Health Metrics</h2>
</div>
<div class="box-subtitle">Enter your vital signs and health parameters.</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age_years = st.number_input("🎂 Age (years)", min_value=18, max_value=100, value=40, step=1)
    bmi = st.number_input("📊 BMI (calculate above if dont know)", min_value=10.0, max_value=60.0, value=calculated_bmi, step=0.1)
    ap_hi = st.number_input("💉 Systolic BP (ap_hi)", min_value=80, max_value=250, value=120, step=1, help="Upper blood pressure reading")
    ap_lo = st.number_input("💉 Diastolic BP (ap_lo)", min_value=40, max_value=150, value=80, step=1, help="Lower blood pressure reading")

with col2:
    chol = st.selectbox("🧪 Cholesterol Level", [1, 2, 3], format_func=lambda x: {1: "Normal", 2: "Above Normal", 3: "Well Above Normal"}[x])
    gluc = st.selectbox("🍬 Glucose Level", [1, 2, 3], format_func=lambda x: {1: "Normal", 2: "Above Normal", 3: "Well Above Normal"}[x])
    smoke = st.selectbox("🚬 Smoker?", ["No", "Yes"])
    alco = st.selectbox("🍺 Alcohol Intake?", ["No", "Yes"])
    active = st.selectbox("🏃 Physically Active?", ["No", "Yes"])

st.markdown("</div>", unsafe_allow_html=True)

# ========= PREDICTION BOX =========
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
st.markdown("""
<div class="box-header">
  <div class="box-icon">🔬</div>
  <h2 class="box-title">Risk Analysis</h2>
</div>
""", unsafe_allow_html=True)

# Convert inputs
smoke_val = 1 if smoke == "Yes" else 0
alco_val = 1 if alco == "Yes" else 0
active_val = 1 if active == "Yes" else 0

features = np.array([[age_years, bmi, ap_hi, ap_lo, chol, gluc, smoke_val, alco_val, active_val]])

if st.button("🔍 Analyze My Risk"):
    pred = model.predict(features)[0]
    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(features)[0, 1]
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    if pred == 1:
        st.error("⚠️ **HIGH CARDIOVASCULAR RISK DETECTED**")
        st.markdown("""
        <div class="info-card">
          <p>🚨 Your health profile indicates elevated risk. Please consult a cardiologist for professional evaluation and personalized treatment plan.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.success("✅ **LOW CARDIOVASCULAR RISK**")
        st.markdown("""
        <div class="info-card">
          <p>💚 Your health profile shows low risk. Continue maintaining a healthy lifestyle with regular exercise and balanced diet.</p>
        </div>
        """, unsafe_allow_html=True)
    
    if proba is not None:
        risk_pct = proba * 100
        col1, col2, col3 = st.columns(3)
        col1.metric("🎯 Risk Probability", f"{risk_pct:.1f}%")
        col2.metric("📊 Model Confidence", f"{max(proba, 1-proba)*100:.1f}%")
        col3.metric("🏥 Recommendation", "See Doctor" if pred == 1 else "Stay Healthy")

st.markdown("</div>", unsafe_allow_html=True)

# ========= FOOTER =========
st.markdown(f"""
<div class="divider"></div>
<div style="text-align: center; padding: 1.5rem 0; color: {GREY}; font-size: 0.9rem;">
  © 2025 <span style="font-weight: 900; color: {GREEN_LIGHT};">CardioGuard</span> · Developed by 
  <span style="font-weight: 900;">Mayank Goyal</span><br>
  <a href="https://www.linkedin.com/in/mayank-goyal-4b8756363" target="_blank" 
     style="color: {GREEN_LIGHT}; text-decoration: none; font-weight: 800; margin-right: 18px;">LinkedIn</a>
  <a href="https://github.com/mayank-goyal09" target="_blank" 
     style="color: {GREEN_LIGHT}; text-decoration: none; font-weight: 800;">GitHub</a><br>
  <span style="font-size: 0.8rem; opacity: 0.7;">💚 Decision Tree ML · Clinical Risk Assessment · For Educational Purposes Only</span>
</div>
""", unsafe_allow_html=True)
