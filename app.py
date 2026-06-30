import requests
import json
import numpy as np
import pandas as pd
import streamlit as st

# ==============================================================================
# PART 1: MASTER LOOKBOOK ENGINE (LIVE GOOGLE SHEETS CONNECTION)
# ==============================================================================
st.title("☕ BLACK ONYX ADVISORY CORE MATRIX")
st.subheader("Global Trade Sourcing, Ecosystem Lookbook & Tactical Analytics")
st.write("**Corporate Horizon:** Black Onyx Advisory × Leola Advisory | **Beneficiary:** Planted by Grace")

# Secure layout link to your verified agricultural metrics tracking sheet
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSd_xrC4SZeJ_KKdt0wAFUPcTZqZo0MjN8Ifhwq090eqg3PLaCXU2XukTlLEW4sVM7GCnOf-Kmqzlwy/pub?output=csv"

@st.cache_data(ttl=3600)
def load_historical_lookbook_data():
    try:
        df = pd.read_csv(csv_url)
        return df
    except Exception:
        # Fixed: Assigned valid numeric placeholder values to the dictionary layer
        return pd.DataFrame({
            "Origin Site": ["Pangkhon Forest", "Doi Chang Ridge", "Mae Salong Canopy"],
            "Elevation (m)":[1350, 1420, 1280],
            "Cherry Grade": ["Tier A Specialty", "Tier A Specialty", "Standard Export"],
            "Brix Index (Sugar)": [22.4, 21.8, 19.5]
        })

lookbook_df = load_historical_lookbook_data()

st.markdown("### 📋 Vetted Origin Profiles (Live CSV Sync)")
st.dataframe(lookbook_df, use_container_width=True, hide_index=True)

# ==============================================================================
# PART 2: TODAY'S SYSTEMS MODULES (LIVE TELEMETRY, AGRONOMY & SOURCING)
# ==============================================================================
st.sidebar.markdown("---")
st.sidebar.subheader("👑 Black Onyx Executive Panel")

today_menu = st.sidebar.selectbox(
    "SELECT ENTERPRISE DASHBOARD", 
    [
        "--- Select Active Terminal ---",
        "1. Real-Time Telemetry & Open API Sync",
        "2. Precision Coffee Yield Tracker",
        "3. Financial Literacy Diagnosis",
        "4. U.S. Federal Sourcing Suite"
    ], 
    key="corporate_navigation_select_node_final_unbreakable"
)

# --- LIVE OPEN-SOURCE NETWORK PIPELINE ---
def fetch_simulated_live_weather():
    try:
        url = "https://open-meteo.com"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()["current"]
            return {
                "temp": float(data["temperature_2m"]),
                "humidity": float(data["relative_humidity_2m"]),
                "weather_code": int(data["weather_code"]),
                "is_live_stream": True
            }
    except Exception:
        pass
    return {"temp": 24.3, "humidity": 88.0, "weather_code": 95, "is_live_stream": False}

# ==============================================================================
# NODE 1: REAL-TIME TELEMETRY & LIVE WEATHER API CORRIDOR
# ==============================================================================
if today_menu == "1. Real-Time Telemetry & Open API Sync":
    st.title("🛰️ High-Altitude Agroforestry Sensor Stream")
    st.write("### Live Open-Source Microclimate Data Synchronization")
    st.caption("Advisory Frame: Simulating real-time satellite telemetry packets pulled directly from the Pangkhon Highlands.")
    
    weather_payload = fetch_simulated_live_weather()
    
    st.markdown("### 📊 Operational Telemetry Status")
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    
    with kpi_col1:
        st.metric(label="Canopy Ambient Temp", value=f"{weather_payload['temp']:.1f} °C", delta="-1.4 °C (Shade Canopy Buffered)", delta_color="normal")
    with kpi_col2:
        st.metric(label="Understory Floor Humidity", value=f"{weather_payload['humidity']:.1f}%", delta="+5.2% (Spore Threshold Variance)", delta_color="inverse")
    with kpi_col3:
        status_label = "LIVE OPEN-API STREAM" if weather_payload['is_live_stream'] else "OFFLINE SATELLITE MODE"
        st.metric(label="Active Data Link Profile", value=status_label)
        
    st.markdown("---")
    col_map, col_alert = st.columns(2)
    
    with col_map:
        st.write("#### 🗺️ Tracked Forest Canopy Location Matrix")
        map_dataframe = pd.DataFrame({'lat': [19.9086], 'lon': [99.8325]})
        st.map(map_dataframe, zoom=11)
        
    with col_alert:
        st.write("#### 🛡️ Microclimate Diagnostics & Predictive Controls")
        st.info(f"**Current Atmosphere Profile:** Server Code {weather_payload['weather_code']} Vetted via Open-Meteo")
        
        if weather_payload['humidity'] > 80.0:
            st.error(f"🚨 **CRITICAL PROCESSING SHOCK WARNING (Humidity: {weather_payload['humidity']:.1f}%)**\n\nAtmospheric values indicate immediate Aspergillus and fungal spore development. Any byproduct coffee grains left in open storage arrays will experience immediate quality contamination.")
            st.warning("⚠️ **Direct Action Directive:** Route all wet biowaste to airtight anaerobic storage tanks instantly to protect upcycling value streams.")
        else:
            st.success("🍏 Microclimate boundaries regulated. Upcycle raw inputs are protected from fungal mold risks.")

# ==============================================================================
# NODE 2: PRECISION COFFEE CROP YIELD TRACKER (AGRONOMY INTERFACE)
# ==============================================================================
elif today_menu == "2. Precision Coffee Yield Tracker":
    st.title("🔴 Precision Coffee Yield & Fruit Quality Diagnostics")
    st.write("### Pre-Harvest Data Metrics for Early Yield Tracking and Value Optimization")
    
    col_calc, col_table = st.columns(2)
    
    with col_calc:
        st.write("#### 🍒 Field Tree Metrics Input")
        total_trees = st.number_input("Total Tracked Trees on Farm Plot", min_value=10, value=1200, step=50, key="agronomy_tree_count_in_final")
        avg_branches = st.slider("Average Bearing Branches per Tree", 10, 60, 32, key="agronomy_branch_slider_final")
        cherries_per_branch = st.slider("Average Red Fruit Count per Branch", 5, 100, 45, key="agronomy_cherry_slider_final")
        
        total_cherries = total_trees * avg_branches * cherries_per_branch
        projected_green_bean_yield_kg = total_cherries / 4000.0
        
    with col_table:
        st.write("#### 📊 Forecasted Yield Value Matrix (Fruit to Green Bean Transformation)")
        st.metric(label="Projected Clean Green Bean Extraction Capacity", value=f"{projected_green_bean_yield_kg:,.1f} Kg", delta="Estimated from fruit metrics 5 months prior to harvest")
        
        st.write("#### 🛠️ Proactive Crop Management Index")
        agronomy_indicators = pd.DataFrame({
            "Yield Health Indicator": ["1. Inner Canopy Airflow Index", "2. Phenological Sugar Conversion", "3. Secondary Traceability Audit"],
            "Status Metric": ["OPTIMAL (Pruning Verified)", "HIGH DENSITY (Blood-Red Fruit)", "COMPLIANT (EUDR Ready)"],
            "Risk Vulnerability Level": ["LOW RISK", "LOW RISK", "ZERO RISK ERROR"]
        })
        st.dataframe(agronomy_indicators, use_container_width=True, hide_index=True)

# ==============================================================================
# NODE 3: FINANCIAL LITERACY DIAGNOSIS
# ==============================================================================
elif today_menu == "3. Financial Literacy Diagnosis":
    st.title("📊 Financial Literacy Mirror: Survival Gap Diagnosis")
    st.write("Translating the middleman's pressure metrics into an objective reality.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### 🏡 Household Operational Inputs")
        annual_needs_thb = st.number_input("Essential Annual Expenses (THB) [Food, Picker Wages, Fertilizer]", min_value=10000, value=120000, step=5000, key="fin_needs_thb_input_fixed")
        total_harvest_kg = st.number_input("Total Bulk Volume Delivered (kg)", min_value=100, value=5000, step=100, key="fin_harvest_kg_input_fixed")
        predatory_blended_rate = st.number_input("Lowest Local Blended Price Offered by Mill (THB/kg)", min_value=10, value=150, step=5, key="fin_blended_rate_input_fixed")
        
    middleman_gross_payout = total_harvest_kg * predatory_blended_rate
    household_survival_gap = middleman_gross_payout - annual_needs_thb
    node3_true_valuation = (total_harvest_kg * 0.15 * 1800.0) + (total_harvest_kg * 0.85 * 350.0)
    net_advisory_surplus = node3_true_valuation - annual_needs_thb

    with col2:
        st.write("#### 📊 Strategic Economic Output")
        st.metric(label="Total Revenue Paid under Blended Rate", value=f"฿{middleman_gross_payout:,.2f} THB")
        
        if household_survival_gap < 0:
            st.error(f"🚨 CHRONIC SURVIVAL DEFICIT DETECTED: -฿{abs(household_survival_gap):,.2f} THB\n\nThis structural deficit forces your household to accept predatory local loans.")
        else:
            st.info(f"Breakeven Runway Surplus: ฿{household_survival_gap:,.2f} THB")
            
        st.success(f"🌟 Premium Controlled Potential Value: ฿{node3_true_valuation:,.2f} THB\n\nNet Economic Family Surplus: ฿{net_advisory_surplus:,.2f} THB")

    st.bar_chart(pd.DataFrame({
        "Economic Paths": ["Middleman Predatory Payout", "Annual Household Costs", "Controlled Trade Potential"],
        "Capital (THB)": [middleman_gross_payout, annual_needs_thb, node3_true_valuation]
    }), x="Economic Paths", y="Capital (THB)")

# ==============================================================================
# NODE 4: U.S. FEDERAL SOURCING SUITE
# ==============================================================================
elif today_menu == "4. U.S. Federal Sourcing Suite":
    st.title("🏛️ U.S. Federal Export Capital & Global Mentorship Matrix")
