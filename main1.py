import streamlit as st
from gtts import gTTS
import sqlite3
import os
from twilio.rest import Client

# -------------------
# CONFIG
# -------------------

# Twilio credentials (optional, for SMS alert)
ACCOUNT_SID = "YOUR_TWILIO_SID"
AUTH_TOKEN = "YOUR_TWILIO_TOKEN"
TWILIO_NUMBER = "+923338392822"
OWNER_PHONE = "+923410066916"  # Verified number for trial

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)

# -------------------
# DATABASE
# -------------------
conn = sqlite3.connect("issues.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS issues(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue TEXT
)
""")
conn.commit()

# -------------------
# STREAMLIT UI
# -------------------
st.title("🤖 AI Call Center Agent")
st.write("Simulated AI agent will greet, take issue, and respond in Urdu voice.")

# -------------------
# Step 1: Greet the client
# -------------------
if st.button("Start Call"):
    greeting = "السلام علیکم! آپ کا خیرمقدم ہے۔ میں آپ کی مدد کے لیے یہاں ہوں۔"
    st.markdown(f"**Agent:** {greeting}")
    
    # Voice for greeting
    tts_greet = gTTS(greeting, lang="ur")
    if not os.path.exists("voice"):
        os.makedirs("voice")
    greet_file = "voice/greet.mp3"
    tts_greet.save(greet_file)
    st.audio(greet_file)

    st.session_state['call_started'] = True

# -------------------
# Step 2: Input user issue
# -------------------
if 'call_started' in st.session_state and st.session_state['call_started']:
    issue = st.text_input("Client: Apna masla yahan likhen")
    
    if st.button("Submit Issue") and issue.strip() != "":
        # Save issue in DB
        cursor.execute("INSERT INTO issues(issue) VALUES(?)", (issue,))
        conn.commit()
        st.success("Masla save ho gaya ✅")
        
        # Voice reply
        reply_text = "سر ابھی مصروف ہوں۔ مسئلہ نوٹ کر لیا ہے۔ میں بعد میں بتا دوں گا۔"
        tts_reply = gTTS(reply_text, lang="ur")
        reply_file = "voice/reply.mp3"
        tts_reply.save(reply_file)
        st.audio(reply_file)
        st.markdown(f"**Agent:** {reply_text}")
        
        # Optional: Send SMS to owner
        try:
            message = twilio_client.messages.create(
                body=f"New Issue: {issue}",
                from_=TWILIO_NUMBER,
                to=OWNER_PHONE
            )
            st.success(f"SMS sent to owner! (SID: {message.sid})")
        except Exception as e:
            st.warning(f"SMS sending failed: {e}")
        
        # Goodbye
        goodbye = "خدا حافظ! جلد آپ کو جواب دیا جائے گا۔"
        tts_goodbye = gTTS(goodbye, lang="ur")
        goodbye_file = "voice/goodbye.mp3"
        tts_goodbye.save(goodbye_file)
        st.audio(goodbye_file)
        st.markdown(f"**Agent:** {goodbye}")
        
        st.session_state['call_started'] = False

# -------------------
# Step 3: Show Issue History
# -------------------
st.subheader("📋 Issue History")
cursor.execute("SELECT * FROM issues")
data = cursor.fetchall()
for row in data:
    st.write(f"{row[0]}. {row[1]}")