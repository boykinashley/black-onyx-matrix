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
# NODE 3: FINANCIAL LITERACY & FORMALIZATION MATRIX (DYNAMIC MAPPING)
# ==============================================================================
elif today_menu == "3. Financial Literacy & Formalization Matrix":
    st.title("🏦 Financial Literacy & Institutional Inclusion Blueprint")
    st.write("### De-Risking the Sourcing Corridor: From Cash Shadows to Wire Compliance")
    
    # Step A: Convert your master dataframe rows into an interactive selector
    st.subheader("🎯 Select Cooperative Entity to Audit")
    coop_names = [row["Entity / Association Name"] for row in st.session_state.farm_database]
    selected_name = st.selectbox("Choose a profile from the registry:", coop_names)
    
    # Step B: Isolate the exact dictionary index for the chosen cooperative
    coop_index = next(index for (index, d) in enumerate(st.session_state.farm_database) if d["Entity / Association Name"] == selected_name)
    active_coop = st.session_state.farm_database[coop_index]
    
    st.markdown(f"#### 🛠️ Direct Audit Console for: **{active_coop['Entity / Association Name']}** (`{active_coop['Coop ID']}`)")
    
    # Step C: Bind checkboxes to the specific values inside that Coop's data dictionary
    # Pre-populating the UI based on whether their string state says "Active ✅" or "Verified ✅"
    initial_tax_state = "Active ✅" in active_coop["Tax ID & Corporate Bank"]
    
    st.markdown("##### Execute Pillar Verification Checks:")
    f1 = st.checkbox("The cooperative possesses a valid government-issued Tax Identification Number (TIN).", value=initial_tax_state)
    f2 = st.checkbox("Financial transactions flow through a verified Corporate Business Bank Account rather than a personal wallet.", value=initial_tax_state)
    f3 = st.checkbox("The association has a standardized framework for rendering formal Commercial Invoices to buyers.", value=initial_tax_state)
    
    # Step D: Save Modifications Button — Commits changes directly back to the matching Coop ID
    if st.button("Commit Financial Status to Ledger", type="primary"):
        if f1 and f2 and f3:
            st.session_state.farm_database[coop_index]["Tax ID & Corporate Bank"] = "Active ✅"
        else:
            st.session_state.farm_database[coop_index]["Tax ID & Corporate Bank"] = "Failed ❌ (Informal Cash Outflow)"
            
        # Re-evaluate complete export readiness rules for this specific ID
        db_ref = st.session_state.farm_database[coop_index]
        if "Verified ✅" in db_ref["Legal & GPS (EUDR)"] and "Active ✅" in db_ref["Tax ID & Corporate Bank"] and db_ref["Moisture Content"] <= 12.5:
            st.session_state.farm_database[coop_index]["Customs Clearance Status"] = "Ready to Export 🚢"
        else:
            st.session_state.farm_database[coop_index]["Customs Clearance Status"] = "Blocked at First-Mile 🚫"
            
        st.success(f"Ledger entry for ID {active_coop['Coop ID']} successfully updated! Refreshing registry matrix...")
        st.rerun()

# ==============================================================================
# NODE 4: GLOBAL TRADE SOURCING SUITE (DYNAMIC MAPPING)
# ==============================================================================
elif today_menu == "4. Global Trade Sourcing Suite":
    st.title("🚢 Border Logistics & Regulatory Clearance Desk")
    st.write("### Conforming First-Mile Agriculture to Destination Port Demands")
    
    st.subheader("🎯 Select Active Container Shipment to Clear")
    coop_names = [row["Entity / Association Name"] for row in st.session_state.farm_database]
    selected_name = st.selectbox("Choose a profile to clear for custom borders:", coop_names)
    
    # Match the active profile index
    coop_index = next(index for (index, d) in enumerate(st.session_state.farm_database) if d["Entity / Association Name"] == selected_name)
    active_coop = st.session_state.farm_database[coop_index]
    
    st.markdown(f"#### 🛂 Custom Inspection Stream for: **{active_coop['Entity / Association Name']}** (`{active_coop['Coop ID']}`)")
    
    col_la, col_lb = st.columns(2)
    with col_la:
        st.subheader("🎛️ Live Metrics Overrides")
        # Pull current values from database state as default starting positions on sliders
        target_moisture = st.slider("Measured Bean Moisture Percentage:", 8.0, 16.0, float(active_coop["Moisture Content"]), step=0.1)
        
        init_phyto = "Yes" if "Passed ✅" in active_coop["Phytosanitary Inspection"] else "No"
        has_phyto_cert = st.radio("Has Local Ministry of Agriculture issued a Phytosanitary Certificate?", ["No", "Yes"], index=1 if init_phyto == "Yes" else 0)
        
        init_gps = "Yes" if "Verified ✅" in active_coop["Legal & GPS (EUDR)"] else "No"
        has_gps_poly = st.radio("Are Land Plot GPS Polygons completely mapped (EUDR Deforestation Compliance)?", ["No", "Yes"], index=1 if init_gps == "Yes" else 0)
        
    with col_lb:
        st.subheader("📑 Border Customs Clearance Outlook")
        
        # Save Override Data back to State Row
        if st.button("Calculate & Lock Clearance Validation"):
            # Update individual data rows
            st.session_state.farm_database[coop_index["Moisture Content"]] = target_moisture
            st.session_state.farm_database[coop_index]["Phytosanitary Inspection"] = "Passed ✅" if has_phyto_cert == "Yes" else "Failed ❌"
            st.session_state.farm_database[coop_index]["Legal & GPS (EUDR)"] = "Verified ✅" if has_gps_poly == "Yes" else "Pending ⚠️"
            
            # Execute Global Rules Evaluator for the Specific Coop ID
            if 10.0 <= target_moisture <= 12.5 and has_phyto_cert == "Yes" and has_gps_poly == "Yes":
                st.session_state.farm_database[coop_index]["Customs Clearance Status"] = "Ready to Export 🚢"
                st.balloons()
                st.success(f"🟢 **PASSPORT GENERATED FOR ID: {active_coop['Coop ID']}**\n\nThis container lot matches all regulatory frameworks for entry. Rules updated on main dashboard ledger.")
            else:
                st.session_state.farm_database[coop_index]["Customs Clearance Status"] = "Blocked at First-Mile 🚫"
                st.error("🔴 **CONTAINER SHIPMENT RISK ACTIVE**\n\nLedger updated. Check main registry matrix view to see active validation failure nodes.")
            
            st.rerun()

# ==============================================================================
# TERMINAL NODE: OPERATIONAL READINESS ASSESSMENT ARCHITECTURE
# ==============================================================================
elif today_menu == "3. Financial Literacy & Formalization Matrix": # Or assign to a dedicated node
    st.title("📊 Institutional Operational Readiness Assessment")
    st.write("### Accenture-Inspired First-Mile Capability & Risk Maturity Matrix")
    st.markdown("""
    This assessment engine scores unorganized outgrower networks against structural international trade milestones. 
    It assigns a definitive Maturity Tier to dictate downstream corporate purchasing safety.
    """)
    st.divider()

    # Step A: Select Active Cooperative Entity from Global Registry Memory
    coop_names = [row["Entity Name"] for row in st.session_state.farm_database]
    selected_name = st.selectbox("Select Target Asset Portfolio to Audit:", coop_names)
    
    # Locate array index mapping node
    coop_index = next(index for (index, d) in enumerate(st.session_state.farm_database) if d["Entity Name"] == selected_name)
    active_coop = st.session_state.farm_database[coop_index]
    
    st.markdown(f"#### 🔒 Active Capability Evaluation Node: **{active_coop['Entity Name']}** (`{active_coop['Coop ID']}`)")
    
    # Step B: Consultative Requirement Gathering Input Checkboxes
    col_input_left, col_input_right = st.columns(2)
    
    with col_input_left:
        st.markdown("##### 🗂️ Pillar 1: Regulatory & Structural Formalization")
        chk_tin = st.checkbox("Active Corporate Registration / Government Tax ID (TIN)", value=("Active ✅" in active_coop["Tax ID & Corporate Bank"]))
        chk_bank = st.checkbox("Corporate Bank Account with Active AML / KYC Anti-Fraud Clearance", value=("Active ✅" in active_coop["Tax ID & Corporate Bank"]))
        chk_gps = st.checkbox("EUDR Compliant GIS Polygon Land Maps Logged to Cloud Registry", value=("Verified ✅" in active_coop["Legal & GPS (EUDR)"]))
        chk_labor = st.checkbox("Zero-Forced-Labor Field Certifications Signed & Logged to DDS", value=True)

    with col_input_right:
        st.markdown("##### 🔬 Pillar 2: Agricultural Processing & Infrastructure Discipline")
        measured_moisture = st.slider("Patio Batch Moisture Profile (%):", 8.0, 16.0, float(active_coop["Moisture Content"]), step=0.1)
        chk_phyto = st.checkbox("Accredited Third-Party Phytosanitary Stamp (ISPM 12 Ready)", value=("Passed ✅" in active_coop["Phytosanitary Inspection"]))
        chk_sorting = st.checkbox("On-Site Flotation Tanks & Sieve Density Machinery Present", value=True)
        chk_trace = st.checkbox("First-Mile Lot Code Batch Tracking Utilized at Receiving Desk", value=False)

    # Step C: Matched Capability Rulebook Logic Engine
    # Total possible infrastructure milestones = 8
    is_moisture_compliant = 10.0 <= measured_moisture <= 12.5
    milestones_passed = sum([chk_tin, chk_bank, chk_gps, chk_labor, is_moisture_compliant, chk_phyto, chk_sorting, chk_trace])
    
    # Define Corporate Maturity Matrix Threshold Tiers
    if milestones_passed == 8:
        maturity_tier = "TIER 1: INSTITUTIONAL EXPORT GRADE 🟢"
        tier_color = "green"
        risk_profile = "MINIMAL RESIDUAL RISK — Fully cleared for instant B2B wire transfers, multi-year forward contracts, and accelerated destination customs entry lanes."
        strategic_directive = "Maintain active digital passport syncing. This asset is ready to be routed to top-tier premium global buyers."
    elif 6 <= milestones_passed <= 7:
        maturity_tier = "TIER 2: CAPABLE SPECIALTY CORRIDOR 🟡"
        tier_color = "orange"
        risk_profile = "MODERATE OPERATIONAL RISK — Minor compliance gaps detected. Eligible for spot purchases, but vulnerable to localized administrative friction."
        strategic_directive = "Prioritize the immediate closing of the unchecked operational items below before attempting to clear European customs."
    elif 4 <= milestones_passed <= 5:
        maturity_tier = "TIER 3: EMERGING INFORMAL NETWORK 🟠"
        tier_color = "orange"
        risk_profile = "ELEVATED TRANSACTIONAL RISK — Supply chain operates within cash shadows or lacks spatial compliance. High probability of border cargo seizure."
        strategic_directive = "Deploy first-mile field agronomists and structural advisors. Do not issue a Bill of Lading text manifest under current operational conditions."
    else:
        maturity_tier = "TIER 4: UNRESTRICTED COMODITY SURVIVAL LOOP 🔴"
        tier_color = "red"
        risk_profile = "SEVERE REGULATORY EXPOSURE — Total compliance absence. Asset is completely decoupled from formal global trade architecture."
        strategic_directive = "Corporate buyers must halt all funding allocation. Sourcing contract requires complete first-mile restructuring from the ground up."

    st.divider()
    
    # Step D: Render Executive Results Panel
    st.subheader("🎯 Enterprise Operational Maturity Output")
    
    res_col1, res_col2 = st.columns([1, 2])
    
    with res_col1:
        st.markdown(f"### Score: `{milestones_passed} / 8`")
        st.markdown(f"##### Assigned Rating:\n**<span style='color:{tier_color}'>{maturity_tier}</span>**", unsafe_allow_html=True)
        
    with res_col2:
        st.markdown(f"**Current Risk Profile:** {risk_profile}")
        st.markdown(f"**Consultative Strategy Move:** {strategic_directive}")

    # Step E: Trigger Live Memory Sync Updates
    if st.button("Commit Maturity Rating to Global Registry Ledger", type="primary"):
        st.session_state.farm_database[coop_index]["Moisture Content"] = measured_moisture
        st.session_state.farm_database[coop_index]["Tax ID & Corporate Bank"] = "Active ✅" if (chk_tin and chk_bank) else "Failed ❌"
        st.session_state.farm_database[coop_index]["Legal & GPS (EUDR)"] = "Verified ✅" if chk_gps else "Pending ⚠️"
        st.session_state.farm_database[coop_index]["Phytosanitary Inspection"] = "Passed ✅" if (chk_phyto and is_moisture_compliant) else "Failed ❌"
        
        if milestones_passed >= 6:
            st.session_state.farm_database[coop_index]["Customs Clearance Status"] = "Ready to Export 🚢"
        else:
            st.session_state.farm_database[coop_index]["Customs Clearance Status"] = "Blocked at First-Mile 🚫"
            
        st.success(f"Maturity rating locked for ID {active_coop['Coop ID']}! Registry updated successfully.")
        st.rerun()

# ==============================================================================
# PART 5: SYSTEM FOOTER, RECOVERY ASSESSMENT & VALUE CALCULATOR ARCHITECTURE
# ==============================================================================
st.divider()
st.markdown("## 📊 Institutional Operational Readiness Assessment")
st.write("### Accenture-Inspired First-Mile Capability & Risk Maturity Matrix")
st.markdown("""
This diagnostic panel scores unorganized outgrower networks against structural international trade milestones, 
calculating real-time capital protection and compliance ROI.
""")

# 1. Select Active Cooperative Entity from Global Registry Memory
coop_names = [row["Entity Name"] for row in st.session_state.farm_database]
selected_name = st.selectbox(
    "Select Target Asset Portfolio to Audit:", 
    coop_names, 
    key="global_bottom_matrix_selector"
)

# Locate array index mapping node
coop_index = next(index for (index, d) in enumerate(st.session_state.farm_database) if d["Entity Name"] == selected_name)
active_coop = st.session_state.farm_database[coop_index]

st.markdown(f"#### 🔒 Active Capability Evaluation Node: **{active_coop['Entity Name']}** (`{active_coop['Coop ID']}`)")

# 2. Consultative Requirement Gathering Input Checkboxes
col_input_left, col_input_right = st.columns(2)

with col_input_left:
    st.markdown("##### 🗂️ Pillar 1: Regulatory & Structural Formalization")
    chk_tin = st.checkbox("Active Corporate Registration / Government Tax ID (TIN)", value=("Active ✅" in active_coop["Tax ID & Corporate Bank"]), key="bottom_chk_tin")
    chk_bank = st.checkbox("Corporate Bank Account with Active AML / KYC Anti-Fraud Clearance", value=("Active ✅" in active_coop["Tax ID & Corporate Bank"]), key="bottom_chk_bank")
    chk_gps = st.checkbox("EUDR Compliant GIS Polygon Land Maps Logged to Cloud Registry", value=("Verified ✅" in active_coop["Legal & GPS (EUDR)"]), key="bottom_chk_gps")
    chk_labor = st.checkbox("Zero-Forced-Labor Field Certifications Signed & Logged to DDS", value=True, key="bottom_chk_labor")

with col_input_right:
    st.markdown("##### 🔬 Pillar 2: Agricultural Processing & Infrastructure Discipline")
    measured_moisture = st.slider("Patio Batch Moisture Profile (%):", 8.0, 16.0, float(active_coop["Moisture Content"]), step=0.1, key="bottom_moisture_slider")
    chk_phyto = st.checkbox("Accredited Third-Party Phytosanitary Stamp (ISPM 12 Ready)", value=("Passed ✅" in active_coop["Phytosanitary Inspection"]), key="bottom_chk_phyto")
    chk_sorting = st.checkbox("On-Site Flotation Tanks & Sieve Density Machinery Present", value=True, key="bottom_chk_sorting")
    chk_trace = st.checkbox("First-Mile Lot Code Batch Tracking Utilized at Receiving Desk", value=False, key="bottom_chk_trace")

# 3. Matched Capability Rulebook Logic Engine
is_moisture_compliant = 10.0 <= measured_moisture <= 12.5
milestones_passed = sum([chk_tin, chk_bank, chk_gps, chk_labor, is_moisture_compliant, chk_phyto, chk_sorting, chk_trace])

# Define Corporate Maturity Matrix Threshold Tiers
if milestones_passed == 8:
    maturity_tier = "TIER 1: INSTITUTIONAL EXPORT GRADE 🟢"
    tier_color = "#2ecc71"
    risk_profile = "MINIMAL RESIDUAL RISK — Fully cleared for instant B2B wire transfers, multi-year forward contracts, and accelerated destination customs entry lanes."
    strategic_directive = "Maintain active digital passport syncing. This asset is ready to be routed to top-tier premium global buyers."
elif 6 <= milestones_passed <= 7:
    maturity_tier = "TIER 2: CAPABLE SPECIALTY CORRIDOR 🟡"
    tier_color = "#f1c40f"
    risk_profile = "MODERATE OPERATIONAL RISK — Minor compliance gaps detected. Eligible for spot purchases, but vulnerable to localized administrative friction."
    strategic_directive = "Prioritize the immediate closing of the unchecked operational items to clear European customs."
elif 4 <= milestones_passed <= 5:
    maturity_tier = "TIER 3: EMERGING INFORMAL NETWORK 🟠"
    tier_color = "#e67e22"
    risk_profile = "ELEVATED TRANSACTIONAL RISK — Supply chain operates within cash shadows or lacks spatial compliance. High probability of border cargo seizure."
    strategic_directive = "Deploy first-mile field agronomists and structural advisors. Do not issue a Bill of Lading text manifest under current operational conditions."
else:
    maturity_tier = "TIER 4: UNRESTRICTED COMMODITY SURVIVAL LOOP 🔴"
    tier_color = "#e74c3c"
    risk_profile = "SEVERE REGULATORY EXPOSURE — Total compliance absence. Asset is completely decoupled from formal global trade architecture."
    strategic_directive = "Corporate buyers must halt all funding allocation. Sourcing contract requires complete first-mile restructuring from the ground up."

st.divider()

# 4. Render Executive Results Panel
st.subheader("🎯 Enterprise Operational Maturity Output")
res_col1, res_col2 = st.columns(2)

with res_col1:
    st.markdown(f"### Score: `{milestones_passed} / 8`")
    st.markdown(f"##### Assigned Rating:\n**<span style='color:{tier_color}'>{maturity_tier}</span>**", unsafe_allow_html=True)
    st.markdown(f"**Current Risk Profile:** {risk_profile}")
    st.markdown(f"**Consultative Strategy Move:** {strategic_directive}")
    
# ==============================================================================
# FINANCIAL ENGINE: VALUE PROTECTION & ROI CALCULATOR
# ==============================================================================
with res_col2:
    st.markdown("#### 💰 Sourcing Risk Value Protection Matrix")
    st.caption("Quantifying the financial losses mitigated by this first-mile digital pre-check.")
    
    # Financial baseline assumptions per standard 20ft shipping container load
    container_value_usd = 75000.00
    
    # Dynamic Loss Prevention Tracking Logic
    exposure_saved_mold = container_value_usd if not is_moisture_compliant else 0.0
    exposure_saved_eudr = (container_value_usd * 0.04) if not chk_gps else 0.0 # 4% Corporate revenue fine proxy
    exposure_saved_demurrage = 4500.00 if (not chk_phyto or not chk_tin) else 0.0 # Average 15 days port hold fees
    
    total_exposure_mitigated = exposure_saved_mold + exposure_saved_eudr + exposure_saved_demurrage
    
    # Render Financial Analytics Data View
    st.write(f"• **Biological Mold Loss Prevented:** `${exposure_saved_mold:,.2f}`")
    st.write(f"• **EUDR Border Penalty Defended:** `${exposure_saved_eudr:,.2f}`")
    st.write(f"• **Port Demurrage Debt Prevented:** `${exposure_saved_demurrage:,.2f}`")
    
    st.metric(
        label="Total Financial Risk Exposure Mitigated by Advisor", 
        value=f"${total_exposure_mitigated:,.2f}",
        delta=f"${total_exposure_mitigated:,.2f} Retained Capital",
        delta_color="normal"
    )

st.divider()

# ==============================================================================
# EXPORT CORE: EXECUTIVE DATA PASSPORT TRANSMISSION
# ==============================================================================
st.subheader("📋 Executive Export Control Desk")
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("Commit Maturity Rating to Global Registry Ledger", type="primary", key="bottom_commit_button"):
        st.session_state.farm_database[coop_index]["Moisture Content"] = measured_moisture
        st.session_state.farm_database[coop_index]["Tax ID & Corporate Bank"] = "Active ✅" if (chk_tin and chk_bank) else "Failed ❌"
        st.session_state.farm_database[coop_index]["Legal & GPS (EUDR)"] = "Verified ✅" if chk_gps else "Pending ⚠️"
        st.session_state.farm_database[coop_index]["Phytosanitary Inspection"] = "Passed ✅" if (chk_phyto and is_moisture_compliant) else "Failed ❌"
        
        if milestones_passed >= 6:
            st.session_state.farm_database[coop_index]["Customs Clearance Status"] = "Ready to Export 🚢"
        else:
            st.session_state.farm_database[coop_index]["Customs Clearance Status"] = "Blocked at First-Mile 🚫"
            
        st.success(f"Maturity rating locked for ID {active_coop['Coop ID']}! Registry updated successfully.")
        st.rerun()

with btn_col2:
    # Constructing a clean, machine-readable text payload blueprint for C-suite distribution
    export_passport_payload = f"""==================================================
BLACK ONYX × LEOLA ADVISORY: TRADE COMPLIANCE PASSPORT
TIMESTAMP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
HARMONIZED HS CODE BASELINE: 0901.11 (GREEN COFFEE)
==================================================
[1. COUNTERPARTY METRICS]
- Assigned Entity ID : {active_coop['Coop ID']}
- Association Name  : {active_coop['Entity Name']}
- Global Score      : {milestones_passed} / 8 Milestones Passed
- Maturity Rating   : {maturity_tier}

[2. PILLAR ATTESTATION VERDICTS]
- Corporate & Tax ID : {'PASSED' if (chk_tin and chk_bank) else 'CRITICAL OUTFLOW EXPOSURE RISK'}
- Environmental Maps : {'VERIFIED COMPLIANT (EUDR READY)' if chk_gps else 'EMBARGOED - NO GEOGON POLYGONS'}
- Measured Moisture  : {measured_moisture}% ({'STABLE' if is_moisture_compliant else 'BIOLOGICAL DAMAGE ALERT'})
- Phytosanitary ISPM : {'VALID STAMP RETRIEVED' if chk_phyto else 'MISSING BIOSECURITY AUDIT'}

[3. ADVISORY REVENUE PROTECTION STATEMENT]
- Gross Capital Loss Exposure Defended: ${total_exposure_mitigated:,.2f} USD
- Customs Pipeline Routing Verdict     : {strategic_directive}
=================================================="""

    st.download_button(
        label="📥 Download Executive Compliance Scorecard (TXT)",
        data=export_passport_payload,
        file_name=f"BlackOnyx_Compliance_Passport_{active_coop['Coop ID']}.txt",
        mime="text/plain",
        key="bottom_download_passport_button"
    )

st.divider()
st.caption("🔒 Black Onyx Advisory Core Terminal. Protected under international trade data governance protocols.")


