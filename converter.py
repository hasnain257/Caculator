import streamlit as st

# Layout ko wide rakha hai taake left side pe jagah bane
st.set_page_config(layout="wide", page_title="Liquid Unit Converter")

# ---------------- CSS (Premium Water Flow & Sidebar Styling) ----------------
st.markdown("""
<style>
/* 🌊 Animated Water Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #a1c4fd, #c2e9fb, #89f7fe, #66a6ff);
    background-size: 400% 400%;
    animation: waterFlow 12s ease-in-out infinite;
}

@keyframes waterFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* 💎 Glass Panels */
.glass-panel {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 30px;
    border: 1px solid rgba(255, 255, 255, 0.4);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.05);
    margin-bottom: 20px;
}

/* 🎯 Left Side Category Styling (Vertical) */
.stRadio div[role="radiogroup"] {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.stRadio div[role="radiogroup"] label {
    background: rgba(255, 255, 255, 0.6) !important;
    color: #1a3a5a !important;
    font-size: 22px !important;
    font-weight: bold !important;
    padding: 25px !important;
    border-radius: 15px !important;
    cursor: pointer;
    transition: 0.3s ease;
    border-left: 5px solid transparent !important;
}

.stRadio div[role="radiogroup"] label:hover {
    background: white !important;
    transform: translateX(10px);
}

/* Selected Category Style */
.stRadio div[role="radiogroup"] input:checked + div {
    background: #66a6ff !important;
    color: white !important;
}

/* Hide Streamlit default radio circles */
.stRadio div[role="radiogroup"] [data-testid="stWidgetLabel"] { display: none; }

/* 📦 Result Cards */
.result-card {
    background: white;
    padding: 15px;
    margin: 10px 0;
    border-radius: 15px;
    font-weight: 800;
    color: #1a3a5a;
    font-size: 20px;
    border-left: 10px solid #66a6ff;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}

.main-title {
    font-size: 55px;
    font-weight: 900;
    text-align: center;
    color: #1a3a5a;
    margin-bottom: 40px;
}

header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌊 Unit Converter</div>', unsafe_allow_html=True)

# ---------------- Split Layout (Left & Right) ----------------
col_left, col_right = st.columns([1, 2.5], gap="large")

with col_left:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown("### 🏷️ Categories")
    # Categories now on the left
    category = st.radio("", ["Length", "Mass", "Time", "Temp", "Current"])
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # Input Area
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    val = st.number_input("Enter Value to Convert", value=1.0, step=0.1)
    st.markdown('</div>', unsafe_allow_html=True)

    # Output Area
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.write(f"### 💧 {category} Conversions")
    
    # Logic
    if category == "Length":
        res = {"Meter": val, "Kilometer": val/1000, "Centimeter": val*100, "Feet": val*3.2808}
    elif category == "Mass":
        res = {"KG": val, "Gram": val*1000, "Pound": val*2.2046, "Ounce": val*35.274}
    elif category == "Time":
        res = {"Seconds": val, "Minutes": val/60, "Hours": val/3600}
    elif category == "Temp":
        res = {"Celsius": val, "Fahrenheit": (val * 9/5) + 32, "Kelvin": val + 273.15}
    else: # Current
        res = {"Ampere": val, "Milliampere": val*1000}

    for k, v in res.items():
        st.markdown(f'<div class="result-card">{k}: {round(v, 4)}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)