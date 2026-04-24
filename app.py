import streamlit as st
from PIL import Image
import datetime

# 1. Page Configuration (Title aur Layout)
st.set_page_config(page_title="AALU DRISHTI AI", page_icon="🚜", layout="centered")

# 2. CSS for Professional Look & Hiding GitHub Info
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .main { background-color: #f5f7f9; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section (Aapka Naam aur School)
st.markdown("""
    <div style="background-color:#004b23;padding:15px;border-radius:15px;border: 2px solid #ccff33;">
    <h1 style="color:white;text-align:center;margin:0;">🚜 AALU DRISHTI AI</h1>
    <p style="color:#ccff33;text-align:center;font-size:18px;margin:5px 0 0 0;">
        <b>Developed by: Bikrant Singh</b><br>
        Class: 12th | Section: A<br>
        <b>Army Public School (APS), Fatehgarh Cantt</b>
    </p>
    </div>
    """, unsafe_allow_html=True)

st.write(f"**Date:** {datetime.date.today()} | **Project:** AI for Agriculture")

# 4. User ID & History System (Session State)
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Sidebar for Farmer Login
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1993/1993420.png", width=100)
st.sidebar.title("Farmer Login")
f_id = st.sidebar.text_input("Enter Farmer ID", value="F-2026")
st.sidebar.info(f"Logged in as: {f_id}")

# 5. Main Content Tabs
tabs = st.tabs(["🔍 AI Diagnosis", "📜 Farmer History", "💹 Mandi Rates"])

with tabs[0]:
    st.header("Potato Health Scanner")
    
    # Selection: Camera or Files
    choice = st.radio("Upload Method:", ["📸 Use Camera", "📁 Upload from Device (Image/Video)"])
    
    if choice == "📸 Use Camera":
        file = st.camera_input("Scan your potato")
    else:
        file = st.file_uploader("Select Photo/Video from Gallery", type=['jpg', 'png', 'jpeg', 'mp4'])

    if file:
        st.write("---")
        # Logic Selection for Demo
        st.subheader("Select Condition for AI Verification:")
        condition = st.selectbox("Observed Symptom:", 
            ["Healthy", "Early Blight", "Late Blight", "Common Scab"])

        # Full Database (Cure, Days, Meds, Price, Survival)
        db = {
            "Healthy": {
                "med": "No Medicine Required", "days": "0", "price": "₹600/q", 
                "survive": "100%", "cure": "Keep in cool, dry storage.", "status": "Safe ✅"
            },
            "Early Blight": {
                "med": "Mancozeb / Antracol", "days": "7-10", "price": "₹450/q", 
                "survive": "85%", "cure": "Spray 2g per litre of water.", "status": "Warning ⚠️"
            },
            "Late Blight": {
                "med": "Ridomil Gold (Metalaxyl)", "days": "15-21", "price": "₹280/q", 
                "survive": "35%", "cure": "Immediate spray required to save crop.", "status": "Danger 🚨"
            },
            "Common Scab": {
                "med": "Emisan-6 / Boric Acid", "days": "Next Crop Cycle", "price": "₹400/q", 
                "survive": "90%", "cure": "Seed treatment and soil pH balance.", "status": "Issue 🛠️"
            }
        }

        res = db[condition]
        
        # Displaying Results in Clean UI
        st.markdown(f"### Result: {res['status']} ({condition})")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Survival Chance", res['survive'])
        c2.metric("Market Price", res['price'])
        c3.metric("Cure Time", f"{res['days']} Days")

        st.error(f"**Required Medicine:** {res['med']}")
        st.info(f"**Treatment Plan:** {res['cure']}")

        if st.button("Save to Farmer Records"):
            st.session_state['history'].append({
                "date": str(datetime.date.today()),
                "id": f_id,
                "result": condition,
                "med": res['med']
            })
            st.success("Record saved successfully!")

with tabs[1]:
    st.header(f"History for {f_id}")
    if st.session_state['history']:
        for i, h in enumerate(reversed(st.session_state['history'])):
            st.write(f"{i+1}. **{h['date']}** - {h['result']} (Med: {h['med']})")
    else:
        st.write("No previous scans found.")

with tabs[2]:
    st.header("Farrukhabad Live Mandi Prices")
    st.table({
        "Potato Variety": ["Local (Aalu)", "Badshah", "Pukhraj", "Chipsona"],
        "Rate (₹/Quintal)": ["510", "630", "545", "680"],
        "Market Condition": ["Stable", "Bullish", "Stable", "High Demand"]
    })

# Footer
st.markdown("---")
st.caption("© 2026 Aalu-Drishti Project | APS Fatehgarh Cantt")

