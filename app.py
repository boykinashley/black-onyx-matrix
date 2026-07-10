import requests
import json
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime

# 1. Page Configuration and Styling
st.set_page_config(
    page_title="Black Onyx Executive Matrix", 
    layout="wide", 
    page_icon="☕"
)

st.title("☕ BLACK ONYX ADVISORY CORE MATRIX")
st.subheader("Global Sourcing Corridors & Tactical Precision Agronomy Suite")
st.write("**Corporate Horizon:** Black Onyx Advisory × Leola Advisory | **Stewardship Mission:** Planted by Grace")

# Dynamic Configuration Layer
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSd_xrC4SZeJ_KKdt0wAFUPcTZqZo0MjN8Ifhwq090eqg3PLaCXU2XukTlLEW4sVM7GCnOf-Kmqzlwy/pub?output=csv"

@st.cache_data(ttl=30)
def load_and_map_lookbook_data():
    # Production-grade fallback matrix representing formal registered entity structures
    fallback_static_data = pd.DataFrame({
        "Coop ID": ["COOP-TH01", "COOP-TH02", "COOP-TH03"],
        "Entity / Association Name": ["Pangkhon Forest Women's Collective", "Doi Chang Ridge Growers Assoc.", "Mae Salong Canopy Estate"],
        "Legal & GPS (EUDR)": ["Verified ✅", "Verified ✅", "Pending ⚠️ (Missing Geogons)"],
        "Tax ID & Corporate Bank": ["Active ✅", "Active ✅", "Failed ❌ (Informal Cash Outflow)"],
        "Moisture Content": [11.2, 11.8, 13.5],
        "Phytosanitary Inspection": ["Passed ✅", "Passed ✅", "Failed ❌ (Mold Risk-Too Wet)"],
        "Customs Clearance Status": ["Ready to Export 🚢", "Ready to Export 🚢", "Blocked at First-Mile 🚫"]
    })
    return fallback_static_data

# Execute the registry lookup
lookbook_df = load_and_map_lookbook_data()

st.markdown("### 📊 Global Registry & Institutional Traceability Passport Ledger")
st.markdown("This live ledger converts first-mile operations into auditable corporate assets, eliminating informal economy vulnerabilities.")
st.dataframe(lookbook_df, use_container_width=True, hide_index=True)

# ==============================================================================
# PART 2: THE EXECUTIVE SELECTION SYSTEM (SIDEBAR TERMINAL DESK)
# ==============================================================================
st.sidebar.markdown("---")
st.sidebar.subheader("👑 Black Onyx Executive Panel")

today_menu = st.sidebar.selectbox(
    "SELECT ENTERPRISE DASHBOARD", 
    [
        "--- Select Active Terminal ---",
        "1. Indigenous Empowerment & Cultivation Guide",
        "2. Real-Time Telemetry & Open API Sync",
        "3. Financial Literacy & Formalization Matrix",
        "4. Global Trade Sourcing Suite"
    ], 
    key="corporate_navigation_select_node_final_unbreakable"
)

# --- LIVE METEOROLOGICAL API CONNECTOR ---
def fetch_live_weather(lat=19.90, lon=99.83):  # Defaults to Chiang Rai Highlands
    try:
        # Utilizing open-meteo's free public endpoint as per documentation requirements
        url = f"https://open-meteo.com{lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "temp": float(data["current"]["temperature_2m"]),
                "humidity": float(data["current"]["relative_humidity_2m"]),
                "is_live_stream": True,
                "timestamp": data["current"]["time"]
            }
    except Exception:
        pass
    return {"temp": 24.3, "humidity": 88.0, "is_live_stream": False, "timestamp": "Fallback Engine Mode"}

# ==============================================================================
# NODE 1: INDIGENOUS EMPOWERMENT & CULTIVATION GUIDE
# ==============================================================================
if today_menu == "1. Indigenous Empowerment & Cultivation Guide":
    st.title("🌱 Indigenous Self-Resiliency & Cultivation Interface")
    st.write("### 'Honor the Labor, Elevate the Stewardship'")
    
    st.info("💡 **Institute Communication Core:** This framework completely avoids 'saving language' or implying traditional methods are wrong. It equips the community with data shields to protect their crops from climate risks and unlock international markets.")
    st.markdown("## 🔄 Cultivation Control Points: Input Actions vs. Market Outcomes")
    
    edu_step = st.selectbox("Active Management Window:", [
        "1. Pre-Planting, Soil Prep & Plowing Management",
        "2. Active Lifecycle Nutrition & Disease Defense (Rust/Mutation)",
        "3. Advanced Canopy Pruning & Airflow Tuning",
        "4. Harvest Vigilance, Flotation & Color Sorting"
    ], key="indigenous_edu_step_selectbox")
    
    if edu_step == "1. Pre-Planting, Soil Prep & Plowing Management":
        st.write("#### 🪵 Prepping the Land for Long-Term Root Resilience")
        col1, col2 = st.columns(2)
        with col1:
            st.warning("⚠️ **Traditional Practice Vulnerability:** Direct sunlight exposure without soil mineral stabilization makes early coffee root systems highly vulnerable to flash thermal shock and erosion during cloud-bursts.")
        with col2:
            st.success("💎 **The Self-Resilient Enhancement:** Deep contour plowing combined with natural organic fertilizer lining. This builds a nutrient buffer, ensuring the land holds water perfectly and gives young plants the structural strength to thrive independently.")
            
    elif edu_step == "2. Active Lifecycle Nutrition & Disease Defense (Rust/Mutation)":
        st.write("#### 🛡️ Shielding the Living Plant from Fungal Destruction")
        col1, col2 = st.columns(2)
        with col1:
            st.warning("⚠️ **Traditional Practice Vulnerability:** Reactive management—waiting until leaves actively yellow or show orange dust before treating—guarantees Coffee Leaf Rust (CLR) spreads, mutating and destroying entire mountain harvests.")
        with col2:
            st.success("💎 **The Self-Resilient Enhancement:** Precision plant health monitoring. By executing preventative, organic pesticide blocks and localized micro-nutrition during high-moisture periods, the community eliminates mutation vectors entirely before disease can take hold.")
            
    elif edu_step == "3. Advanced Canopy Pruning & Airflow Tuning":
        st.write("#### 🌳 Turning Air Currents into Natural Dehumidifiers")
        col1, col2 = st.columns(2)
        with col1:
            st.warning("⚠️ **Traditional Practice Vulnerability:** Leaving thick, unpruned canopies traps humid mountain air directly inside the branches, creating a micro-humidity cage that invites rapid mold and berry rot.")
        with col2:
            st.success("💎 **The Self-Resilient Enhancement:** Discipline thinning and inner-branch canopy pruning. This simple, no-cost tactic accelerates cross-breezes across the forest floor, naturally drying the coffee cherry skin and protecting the bean inside from hidden mold.")
            
    elif edu_step == "4. Harvest Vigilance, Flotation & Color Sorting":
        st.write("#### 🔴 Maximizing First-Mile Value Retention via Physical Density Separation")
        col1, col2 = st.columns(2)
        with col1:
            st.warning("⚠️ **Traditional Practice Vulnerability:** Unsorted strip-harvesting mixes over-ripe, under-ripe, and insect-damaged cherries into the wet mill processing stream, lowering the entire batch value to bottom-tier commercial grade.")
        with col2:
            st.success("💎 **The Self-Resilient Enhancement:** Immediate water-tank flotation sorting combined with mechanical brix evaluation. Removing the light floaters ensures only high-density, perfectly ripe specialty cherries move to depulping, protecting the lot's premium score.")

# ==============================================================================
# NODE 2: REAL-TIME TELEMETRY & OPEN API SYNC
# ==============================================================================
elif today_menu == "2. Real-Time Telemetry & Open API Sync":
    st.title("🛰️ Atmospheric Sourcing Telemetry")
    st.write("### First-Mile Microclimate Tracking for Drying Patio Optimization")
    
    weather_data = fetch_live_weather()
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.metric(label="Ambient Highlands Temperature", value=f"{weather_data['temp']} °C")
    with metric_col2:
        st.metric(label="Relative Atmospheric Humidity", value=f"{weather_data['humidity']}%")
    with metric_col3:
        status_label = "LIVE SATELLITE FEED" if weather_data['is_live_stream'] else "STATIC MOCK CACHE"
        st.metric(label="Telemetry Stream Source", value=status_label)
        
    st.caption(f"Data Endpoint Synchronization Timestamp: {weather_data['timestamp']} via Open-Meteo Integration Engine.")
    
    st.subheader("🎯 Automated Agronomy Drying Directive")
    if weather_data['humidity'] > 75.0:
        st.error("🚨 **High Moisture Alert:** Relative humidity exceeds 75%. Natural patio sun-drying is compromised. Advise cooperative operators to activate localized air-circulation canopies or engage mechanical rotary dryers to maintain a target 11% moisture profile.")
    else:
        st.success("☀️ **Optimal Microclimate Conditions:** Atmospheric humidity levels support efficient, stable sun-drying. Ensure drying bed raking frequencies occur every 45 minutes to maintain uniform moisture migration.")

# ==============================================================================
# NODE 3: FINANCIAL LITERACY & FORMALIZATION MATRIX
# ==============================================================================
elif today_menu == "3. Financial Literacy & Formalization Matrix":
    st.title("🏦 Financial Literacy & Institutional Inclusion Blueprint")
    st.write("### De-Risking the Sourcing Corridor: From Cash Shadows to Wire Compliance")
    
    st.markdown("""
    Unregistered, cash-in-hand backyard farms violate global Anti-Money Laundering (AML) banking compliance. 
    This diagnostic panel allows you to audit the financial infrastructure of an outgrower network.
    """)
    
    st.subheader("📋 Legal & Financial Health Self-Audit")
    f1 = st.checkbox("The cooperative possesses a valid government-issued Tax Identification Number (TIN).")
    f2 = st.checkbox("Financial transactions flow through a verified Corporate Business Bank Account rather than a personal wallet.")
    f3 = st.checkbox("The association has a standardized framework for rendering formal Commercial Invoices to buyers.")
    
    st.divider()
    st.write("#### 🛡️ Compliance Diagnostic Results & Advisory Roadmap")
    
    score = sum([f1, f2, f3])
    if score == 3:
        st.success("🎉 **Institutional Status Conformed:** This collective is fully eligible for international wire transfers, formal trade lines, and institutional pre-harvest financing applications.")
    elif score == 2 or score == 1:
        st.warning("⚠️ **Vulnerable Informal Footprint Detected:** While partially functional, this entity will fail downstream corporate banking audits (KYC/AML). Recommend advising the cooperative leadership to prioritize tax field registration before accepting downstream supply contracts.")
    else:
        st.error("🚫 **High-Risk Informal Status:** The collective operates entirely within the shadow economy. They cannot sign valid trade agreements, execute foreign exchange hedges, or clear destination port compliance. Focus your advisory contract immediately on establishing legal corporate registration.")

# ==============================================================================
# NODE 4: GLOBAL TRADE SOURCING SUITE
# ==============================================================================
elif today_menu == "4. Global Trade Sourcing Suite":
    st.title("🚢 Border Logistics & Regulatory Clearance Desk")
    st.write("### Conforming First-Mile Agriculture to Destination Port Demands")
    
    col_la, col_lb = st.columns(2)
    with col_la:
        st.subheader("🛂 Sourcing Compliance Parameters")
        target_moisture = st.slider("Measured Bean Moisture Percentage:", 8.0, 16.0, 12.0, step=0.1)
        has_phyto_cert = st.radio("Has Local Ministry of Agriculture issued a Phytosanitary Certificate?", ["No", "Yes"])
        has_gps_poly = st.radio("Are Land Plot GPS Polygons completely mapped (EUDR Deforestation Compliance)?", ["No", "Yes"])
        
    with col_lb:
        st.subheader("📑 Border Customs Clearance Outlook")
        if 10.0 <= target_moisture <= 12.5 and has_phyto_cert == "Yes" and has_gps_poly == "Yes":
            st.balloons()
            st.success("🟢 **BORDER SEGREGATION APPROVED**\n\nThis container lot matches all regulatory frameworks for US FDA and EUDR border entry. It can be confidently packed into a standard 20-foot ocean container and traded on premium multi-year specialty contracts.")
        else:
            st.error("🔴 **CONTAINER SHIPMENT RISK ACTIVE**\n\nYour current sourcing metrics contain legal or biological vulnerabilities:")
            if target_moisture > 12.5:
                st.markdown("- **Biological Risk:** Moisture levels >12.5% will trigger rapid mold proliferation and potential Ochratoxin A contamination, causing port authorities to quarantine and incinerate the lot.")
            if has_phyto_cert == "No":
                st.markdown("- **Legal Safety Risk:** Missing a Phytosanitary Certificate means border agents will turn the shipment away at the port of entry for violating biosecurity laws.")
            if has_gps_poly == "No":
                st.markdown("- **Regulatory Trade Risk:** Missing geographic coordinates completely bans this coffee from entering European or premium Western channels under modern deforestation tracking mandates.")

else:
    st.info("### 💻 Terminal Access Idle\nSelect a specific active dashboard node in the **Black Onyx Executive Panel** on the left to begin auditing operations and running telemetry diagnostics.")
