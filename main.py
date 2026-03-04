import streamlit as st

st.set_page_config(page_title="Animated Calculator", page_icon="🧮", layout="centered")

# -------------------
# CSS Styling
# -------------------
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #1e3c72, #2a5298, #6dd5ed, #2193b0);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Calculator Container */
[data-testid="stAppViewContainer"] .calc-container {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(15px);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    animation: float 6s ease-in-out infinite;
}

/* Floating Animation */
@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0);}
}

/* Display */
.display {
    background: rgba(255,255,255,0.3);
    padding: 20px;
    border-radius: 20px;
    font-size: 32px;
    text-align: right;
    margin-bottom: 20px;
    color: black;
    font-weight: bold;
    box-shadow: inset 0 0 15px rgba(0,0,0,0.2);
}

/* Buttons */
.stButton>button {
    width: 100%;
    height: 55px;
    font-size: 30px !important;
    font-weight: 900 !important;
    color: black !important;
    border-radius: 15px;
    border: none;
    background: rgba(255,255,255,0.3);
    font-family: Arial, sans-serif;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.1);
    background: rgba(255,255,255,0.0);
    box-shadow: 0 0 black;
}

div.stButton > button[kind="primary"] {
    background: linear-gradient(45deg, #00f2fe, #4facfe);
    box-shadow: 0 0 20px #00f2fe;
}

</style>
""", unsafe_allow_html=True)

# -------------------
# Session State
# -------------------
if "expr" not in st.session_state:
    st.session_state.expr = ""

def add_val(v):
    st.session_state.expr += str(v)

def clear():
    st.session_state.expr = ""

def calc():
    try:
        st.session_state.expr = str(eval(st.session_state.expr))
    except:
        st.session_state.expr = "Error"

# -------------------
# Calculator UI
st.markdown('<div class="calc-container">', unsafe_allow_html=True)

# ✅ Add Title inside calc-container
st.markdown('<h2 style="color:black; text-align:center; margin-bottom:20px;  font-weight:bold; ">Stylish Calculator</h2>', unsafe_allow_html=True)
# Murqee at the end
st.markdown('''
<marquee behavior="scroll" direction="left" style="color:#ffd700;  font-weight:bold; font-size:20px; margin-top:15px;">
🎉 Welcome to Hasnain\'s Premium Calculator! 🎉
</marquee>
''', unsafe_allow_html=True)
# Display Current Expression
st.markdown(f'<div class="display">{st.session_state.expr}</div>', unsafe_allow_html=True)
# Row 1
c1, c2, c3, c4 = st.columns(4)
c1.button("7", on_click=add_val, args=("7",))
c2.button("8", on_click=add_val, args=("8",))
c3.button("9", on_click=add_val, args=("9",))
c4.button("➗", on_click=add_val, args=("/"))

# Row 2
c1, c2, c3, c4 = st.columns(4)
c1.button("4", on_click=add_val, args=("4",))
c2.button("5", on_click=add_val, args=("5",))
c3.button("6", on_click=add_val, args=("6",))
c4.button("✖", on_click=add_val, args=("*"))

# Row 3
c1, c2, c3, c4 = st.columns(4)
c1.button("1", on_click=add_val, args=("1",))
c2.button("2", on_click=add_val, args=("2",))
c3.button("3", on_click=add_val, args=("3",))
c4.button("➖", on_click=add_val, args=("-"))

# Row 4
c1, c2, c3, c4 = st.columns(4)
c1.button("C", on_click=clear)
c2.button("0", on_click=add_val, args=("0",))
c3.button(".", on_click=add_val, args=("."))
c4.button("➕", on_click=add_val, args=("+"))

# Equal
st.button("🟩=🟩", on_click=calc, use_container_width=True, type="primary")

st.markdown('</div>', unsafe_allow_html=True)
