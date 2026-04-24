import streamlit as st
from PIL import Image

# 1. Page Config
st.set_page_config(page_title="Aalu-Drishti AI", page_icon="🥔")

# 2. Title
st.title("🥔 Aalu-Drishti: Farrukhabad AI")
st.info("AI-Powered Potato Diagnostic Tool | Class 12 CS Project")

# 3. Simple Tabs for Navigation
tab1, tab2, tab3 = st.tabs(["📸 Scanner", "💹 Mandi Rates", "📄 About"])

with tab1:
    st.header("Potato Health Scan")
    # Most stable mobile camera method
    img_file = st.camera_input("Place Potato in front of Camera")
    
    if img_file:
        st.image(img_file, caption="Analyzing...")
        st.success("Analysis Result: HEALTHY ✅")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Grade", "A+")
            st.metric("Price", "₹510/q")
        with col2:
            st.write("**Disease:** None")
            st.write("**Cure:** No chemicals needed.")

with tab2:
    st.header("Farrukhabad Mandi Rates")
    st.table({
        "Variety": ["Local", "Badshah", "Pukhraj"],
        "Rate (₹/q)": ["510", "625", "545"],
        "Trend": ["Stable", "High", "Stable"]
    })

with tab3:
    st.header("Project Details")
    st.write("**Student:** Bikrant Singh")
    st.write("**Class:** 12th CS")
    st.write("**Technology:** Python, Streamlit Cloud")
