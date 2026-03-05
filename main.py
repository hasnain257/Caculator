import streamlit as st

st.set_page_config(page_title="Animated Calculator", page_icon="🧮", layout="centered")

# ------------------- CSS Styling -------------------
st.markdown("""
<style>
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
.calc-container {
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(15px);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}
.display {
    background: rgba(255,255,255,0.3);
    padding: 20px;
    border-radius: 20px;
    font-size: 32px;
    text-align: right;
    margin-bottom: 20px;
    color: black;
    font-weight: bold;
}
.stButton>button {
    width: 100%;
    height: 55px;
    font-size: 30px !important;
    font-weight: 900 !important;
    color: black !important;
    border-radius: 15px;
    border: none;
    background: rgba(255,255,255,0.3);
}
.stButton>button:hover {
    transform: scale(1.1);
    background: rgba(255,255,255,0.0);
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(45deg, #00f2fe, #4facfe);
    box-shadow: 0 0 20px #00f2fe;
}
</style>
""", unsafe_allow_html=True)

# ------------------- Session State -------------------
if "expr" not in st.session_state:
    st.session_state.expr = ""

# ------------------- Functions -------------------
def add_val(v):
    st.session_state.expr += str(v)

def clear():
    st.session_state.expr = ""

def calc():
    try:
        st.session_state.expr = str(eval(st.session_state.expr))
    except:
        st.session_state.expr = "Error"

# ------------------- Calculator UI -------------------
st.markdown('<div class="calc-container">', unsafe_allow_html=True)
st.markdown('<h2 style="color:black; text-align:center; margin-bottom:20px; font-weight:bold;">Stylish Calculator</h2>', unsafe_allow_html=True)

# ✅ Keyboard Input directly updates expr
st.text_input("Type using Keyboard", key="expr", value=st.session_state.expr)

# Display
st.markdown(f'<div class="display">{st.session_state.expr}</div>', unsafe_allow_html=True)

# Buttons
rows = [
    ["7", "8", "9", "➗"],
    ["4", "5", "6", "✖️"],
    ["1", "2", "3", "➖"],
    ["C", "0", ".", "➕"]
]

for row in rows:
    c1, c2, c3, c4 = st.columns(4)
    buttons = [c1, c2, c3, c4]
    for btn, val in zip(buttons, row):
        if val == "C":
            btn.button(val, on_click=clear)
        elif val in ["➕", "➖", "✖️", "➗"]:
            mapping = {"➕":"+","➖":"-","✖️":"*","➗":"/"}
            btn.button(val, on_click=add_val, args=(mapping[val],))
        else:
            btn.button(val, on_click=add_val, args=(val,))

# Equal
st.button("🟩=🟩", on_click=calc, use_container_width=True, type="primary")

# Welcome Marquee
st.markdown('''
<marquee behavior="scroll" direction="left" style="color:#ffd700; font-weight:bold; font-size:20px; margin-top:15px;">
🎉Thank you for visiting! 🥳😄😀 🎉
</marquee>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)