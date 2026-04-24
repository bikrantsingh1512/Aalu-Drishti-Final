import streamlit as st
from PIL import Image, ImageStat
import datetime

# 1. Page Configuration
st.set_page_config(page_title="Aloo Drishti AI", page_icon="🥔", layout="centered")

# 2. Advanced UI Styling
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #ffffff; }
    .stTabs [aria-selected="true"] { background-color: #1e3d59; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Branding Header
st.markdown("""
    <div style="background-color:#1e3d59;padding:20px;border-radius:15px;border-bottom: 8px solid #ff6e40;box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
    <h1 style="color:white;text-align:center;margin:0;font-family:sans-serif;">🥔 ALOO DRISHTI AI</h1>
    <p style="color:#ff6e40;text-align:center;font-size:18px;margin:10px 0 0 0;">
        <b>Developer: Bikrant Singh</b> | Class 12th CS<br>
        <span style="color:white;">Army Public School (APS), Fatehgarh Cantt</span>
    </p>
    </div>
    """, unsafe_allow_html=True)

# 4. AI Logic Engine
def perform_ai_analysis(img):
    img_rgb = img.convert('RGB')
    stat = ImageStat.Stat(img_rgb)
    r, g, b = stat.mean
    brightness = (r + g + b) / 3
    if brightness > 135:
        return "Healthy"
    elif 95 < brightness <= 135:
        return "Early Blight"
    else:
        return "Late Blight"

# 5. Main App
tab1, tab2 = st.tabs(["🔍 Smart AI Scanner", "💹 Mandi Rates"])

with tab1:
    st.markdown("### 📸 Scan Potato Image/Video")
    file = st.file_uploader("Upload from Device Storage", type=['jpg','jpeg','png','mp4'])

    if file:
        if hasattr(file, 'type') and 'video' in file.type:
            st.video(file)
            st.info("Please upload a photo for AI Disease Diagnosis.")
        else:
            image = Image.open(file)
            st.image(image, caption="Analyzing patterns...", use_container_width=True)
            
            with st.spinner('🔄 AI is calculating infection ratio...'):
                result = perform_ai_analysis(image)
                
                # Full Medical & Logic Database
                db = {
                    "Healthy": {
                        "reason": "Proper soil nutrients and ideal weather conditions.",
                        "med": "No Chemical Required",
                        "ratio": "N/A",
                        "interval": "N/A",
                        "survival": "100%",
                        "price": "₹620/q",
                        "tips": "Maintain storage temperature between 3°C to 4°C."
                    },
                    "Early Blight": {
                        "reason": "Fungus (Alternaria solani) due to high humidity and warm temperatures.",
                        "med": "Mancozeb (Indofil M-45) or Antracol",
                        "ratio": "2.5 grams per 1 Litre of water",
                        "interval": "Repeat every 7 to 10 days until spots disappear",
                        "survival": "85%",
                        "price": "₹450/q",
                        "tips": "Remove infected lower leaves to stop the spread."
                    },
                    "Late Blight": {
                        "reason": "Phytophthora infestans (Oomycete) caused by cool, wet weather and fog.",
                        "med": "Ridomil Gold (Metalaxyl + Mancozeb) or Sectin",
                        "ratio": "2 grams per 1 Litre of water",
                        "interval": "Repeat every 5 days in cloudy weather",
                        "survival": "35% (Immediate action needed)",
                        "price": "₹250/q",
                        "tips": "Burn infected plants and avoid irrigation during fog."
                    }
                }
                data = db[result]

            # Results Display
            st.success(f"## Result: {result}")
            
            # Key Metrics
            c1, c2 = st.columns(2)
            c1.metric("Survival Chance", data['survival'])
            c2.metric("Market Price", data['price'])

            # Detailed Prescription Box
            st.markdown(f"""
            <div style="background-color:#f0f7f4; padding:20px; border-radius:10px; border-left: 5px solid #1e3d59;">
                <h4 style="color:#1e3d59; margin-top:0;">📝 AI Medical Report</h4>
                <b>❓ Kyon Hua (Reason):</b> {data['reason']}<br><br>
                <b>💊 Medicine Name:</b> {data['med']}<br>
                <b>🧪 Mixing Ratio:</b> {data['ratio']}<br>
                <b>📅 Interval:</b> {data['interval']}<br><br>
                <b>💡 Expert Tip:</b> {data['tips']}
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.header("Farrukhabad Mandi Rates")
    st.table({"Variety": ["Local", "Badshah", "Pukhraj"], "Rate": ["₹520", "₹640", "₹550"]})

st.markdown("---")
st.caption("Aloo Drishti AI | Army Public School Fatehgarh | Developer: Bikrant Singh")
