import requests
import json
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Black Onyx Advisor Terminal", 
    layout="wide", 
    page_icon="🛡️"
)

st.title("🛡️ BLACK ONYX × LEOLA ADVISORY: AUTOMATED EXEC ADVISOR")
st.subheader("Continuous Transaction Controls (CTC) & First-Mile Compliance Engine")
st.write("**System Architecture:** Automated Supply Chain Risk Mitigator | **HS Code Baseline:** 0901 (Green Coffee)")

# 🚨 PASTE YOUR ENTIRE "PUBLISHED TO WEB" GOOGLE SHEETS CSV EXPORT LINK HERE:
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSd_xrC4SZeJ_KKdt0wAFUPcTZqZo0MjN8Ifhwq090eqg3PLaCXU2XukTlLEW4sVM7GCnOf-Kmqzlwy/pub?output=csv"

@st.cache_data(ttl=5) # 5-second short cache lifespan so edits appear quickly
def fetch_and_translate_google_sheet(url):
    try:
        # Step A: Pull raw records straight from your Google Sheet cloud network
        raw_df = pd.read_csv(url)
        
        # Step B: THE BRIDGING LAYER — Translate your Google Sheet columns to match the Python logic!
        # Syntax: "Your Real Google Sheet Header Name" : "The Core App's Expected Name"
        column_mapping_dictionary = {
            "What is the name of your farm or village?": "Entity Name",
            "Cooperative / Estate Name": "Entity Name",
            "Farm Location or Site Node": "Entity Name",
            "Current Elevation": "Elevation (m)",
            "Observed Sugar Brix Content": "Brix Index (Sugar)",
            "EUDR Mapping Status": "Legal & GPS (EUDR)",
            "Tax Registration / Bank Profile": "Tax ID & Corporate Bank",
            "Measured Moisture Level": "Moisture Content",
            "Phytosanitary Audit Status": "Phytosanitary Inspection"
        }
        
        # Execute an automated column rename map to standardize the payload
        mapped_df = raw_df.rename(columns=column_mapping_dictionary)
        
        # Step C: Inject structural safety backstops for missing critical tracking keys
        if "Coop ID" not in mapped_df.columns:
            mapped_df.insert(0, "Coop ID", [f"COOP-LN{i+1:02d}" for i in range(len(mapped_df))])
        if "Entity Name" not in mapped_df.columns:
            mapped_df["Entity Name"] = "Unknown Cooperative Profile"
        if "Legal & GPS (EUDR)" not in mapped_df.columns:
            mapped_df["Legal & GPS (EUDR)"] = "Pending ⚠️"
        if "Tax ID & Corporate Bank" not in mapped_df.columns:
            mapped_df["Tax ID & Corporate Bank"] = "Failed ❌"
        if "Moisture Content" not in mapped_df.columns:
            mapped_df["Moisture Content"] = 12.0
        if "Phytosanitary Inspection" not in mapped_df.columns:
            mapped_df["Phytosanitary Inspection"] = "Failed ❌"
            
        # Step D: Business Logic Engine: Compute Customs Clearance Status at runtime
        customs_status = []
        for _, row in mapped_df.iterrows():
            is_legal = "Verified ✅" in str(row.get("Legal & GPS (EUDR)", ""))
            is_financial = "Active ✅" in str(row.get("Tax ID & Corporate Bank", ""))
            try:
                moisture = float(row.get("Moisture Content", 12.0))
                is_dry = 10.0 <= moisture <= 12.5
            except ValueError:
                is_dry = False
                
            if is_legal and is_financial and is_dry:
                customs_status.append("Ready to Export 🚢")
            else:
                customs_status.append("Blocked at First-Mile 🚫")
                
        mapped_df["Customs Clearance Status"] = customs_status
        return mapped_df.to_dict(orient="records")
        
    except Exception as e:
        # Production-grade fallback matrix representing formal registered entity structures if URL is private or empty
        return [
            {
                "Coop ID": "COOP-TH01",
                "Entity Name": "Pangkhon Forest Women's Collective",
                "Legal & GPS (EUDR)": "Verified ✅",
                "Tax ID & Corporate Bank": "Active ✅",
                "Moisture Content": 11.2,
                "Phytosanitary Inspection": "Passed ✅",
                "Customs Clearance Status": "Ready to Export 🚢"
            },
            {
                "Coop ID": "COOP-HN02",
                "Entity Name": "Valley View Smallholder Network",
                "Legal & GPS (EUDR)": "Pending ⚠️",
                "Tax ID & Corporate Bank": "Failed ❌",
                "Moisture Content": 13.8,
                "Phytosanitary Inspection": "Failed ❌",
                "Customs Clearance Status": "Blocked at First-Mile 🚫"
            }
        ]

# 2. STATE SYNCHRONIZATION
# Always query the spreadsheet cloud first instead of locking in a static hardcoded array
if 'farm_database' not in st.session_state or st.sidebar.button("🔄 Force Global Sheet Sync"):
    st.session_state.farm_database = fetch_and_translate_google_sheet(CSV_URL)

# Transform active memory state back into dataframes for analytics dashboard presentation
lookbook_df = pd.DataFrame(st.session_state.farm_database)

st.markdown("### 📊 Global Registry & Institutional Traceability Passport Ledger")
st.markdown("This live ledger converts first-mile operations into auditable corporate assets, eliminating informal economy vulnerabilities.")
st.dataframe(lookbook_df, use_container_width=True, hide_index=True)
st.divider()

# ==============================================================================
# PART 2: SIDEBAR TERMINAL DESK & METEOROLOGICAL TELEMETRY
# ==============================================================================
st.sidebar.subheader("👑 Advisor Portal Options")

today_menu = st.sidebar.selectbox(
    "SELECT ENTERPRISE DASHBOARD", 
    [
        "--- Select Active Terminal ---",
        "1. Indigenous Empowerment & Cultivation Guide",
        "2. Real-Time Telemetry & Open API Sync",
        "3. Financial Literacy & Sourcing Suite"
    ], 
    key="corporate_navigation_select_node_final_unbreakable"
)

def fetch_highlands_telemetry(lat=19.90, lon=99.83):
    try:
        url = f"https://open-meteo.com{lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "temp": float(data["current"]["temperature_2m"]),
                "humidity": float(data["current"]["relative_humidity_2m"]),
                "live": True,
                "time": data["current"]["time"]
            }
    except Exception:
        pass
    return {"temp": 24.3, "humidity": 88.0, "live": False, "time": "Static Buffer Activated"}

if today_menu == "2. Real-Time Telemetry & Open API Sync":
    st.title("🛰️ Atmospheric Sourcing Telemetry")
    st.write("### Cross-Border Infrastructure Microclimate Tracking")
    
    climate = fetch_highlands_telemetry()
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.metric(label="Ambient Drying Station Temperature", value=f"{climate['temp']} °C")
    with col_t2:
        st.metric(label="Relative Atmospheric Humidity", value=f"{climate['humidity']}%")
        
    st.caption(f"Telemetry Status: {'Live Cloud Stream Sync' if climate['live'] else 'Static Buffer Active'} | Timestamp: {climate['time']}")
    
    if climate['humidity'] > 75.0:
        st.error("🚨 **High Moisture Alert:** Ambient relative humidity limits natural patio sun-drying. Extend mechanical drying schedules immediately to protect the lot from biological decay and prevent validation failure at the destination port.")
    else:
        st.success("☀️ **Optimal Processing Window:** Microclimate supported. Proceed with natural patio sun-drying. Recalibrate sorting frequencies to 45-minute intervals.")

# ==============================================================================
# PART 3: SOURCING STRATEGY DASHBOARD NODES
# ==============================================================================
if today_menu == "1. Indigenous Empowerment & Cultivation Guide":
    st.title("🌱 Indigenous Self-Resiliency & Cultivation Interface")
    st.write("### 'Honor the Labor, Elevate the Stewardship'")
    st.info("💡 **Institute Communication Core:** This framework completely avoids 'saving language' or implying traditional methods are wrong. It equips the community with data shields to protect their crops from climate risks and unlock international markets.")
    
    edu_step = st.selectbox("Active Management Window:", [
        "1. Pre-Planting, Soil Prep & Plowing Management",
        "2. Active Lifecycle Nutrition & Disease Defense (Rust/Mutation)",
        "3. Advanced Canopy Pruning & Airflow Tuning",
        "4. Harvest Vigilance, Flotation & Color Sorting"
    ], key="indigenous_edu_step_selectbox")
    
    if edu_step == "1. Pre-Planting, Soil Prep & Plowing Management":
        st.write("#### 🪵 Prepping the Land for Long-Term Root Resilience")
        col1, col2 = st.columns(2)
        with col1: st.warning("⚠️ **Traditional Practice Vulnerability:** Direct sunlight exposure without soil mineral stabilization makes early coffee root systems highly vulnerable to flash thermal shock.")
        with col2: st.success("💎 **The Self-Resilient Enhancement:** Deep contour plowing combined with natural organic fertilizer lining builds an immediate moisture-retaining buffer.")
    else:
        st.write("Review core cultivation parameters inside selection tabs to maximize crop density outcomes.")

elif today_menu == "3. Financial Literacy & Sourcing Suite":
    st.title("🚢 Global Trade Sourcing & Requirement Analysis Panel")
    st.write("Use the permanent assessment terminal displayed below at the foot of the screen to actively audit, grade, and configure corporate data for each unique Cooperative profile.")

# ==============================================================================
# PART 4: SYSTEM FOOTER, RECOVERY ASSESSMENT & VALUE CALCULATOR ARCHITECTURE
# ==============================================================================
st.divider()
st.markdown("## 📊 Institutional Operational Readiness Assessment")
st.write("### Accenture-Inspired First-Mile Capability & Risk Maturity Matrix")
st.markdown("""
This permanent diagnostic panel scores unorganized outgrower networks against structural international trade milestones, 
calculating real-time capital protection and compliance ROI.
""")

# Extract data keys safely from synced memory registry mapping variables
coop_names = [row["Entity Name"] for row in st.session_state.farm_database]
selected_name = st.selectbox(
    "Select Target Asset Portfolio to Audit:", 
    coop_names, 
    key="global_bottom_matrix_selector"
)

# Locate active array index inside memory rows
coop_index = next(index for (index, d) in enumerate(st.session_state.farm_database) if d["Entity Name"] == selected_name)
active_coop = st.session_state.farm_database[coop_index]

st.markdown(f"#### 🔒 Active Capability Evaluation Node: **{active_coop['Entity Name']}** (`{active_coop['Coop ID']}`)")

# 2. Consultative Requirement Gathering Input Checkboxes
col_input_left, col_input_right = st.columns(2)

with col_input_left:
    st.markdown("##### 🗂️ Pillar 1: Regulatory & Structural Formalization")
    chk_tin = st.checkbox("Active Corporate Registration / Government Tax ID (TIN)", value=("Active ✅" in str(active_coop["Tax ID & Corporate Bank"])), key="bottom_chk_tin")
    chk_bank = st.checkbox("Corporate Bank Account with Active AML / KYC Anti-Fraud Clearance", value=("Active ✅" in str(active_coop["Tax ID & Corporate Bank"])), key="bottom_chk_bank")
    chk_gps = st.checkbox("EUDR Compliant GIS Polygon Land Maps Logged to Cloud Registry", value=("Verified ✅" in str(active_coop["Legal & GPS (EUDR)"])), key="bottom_chk_gps")
    chk_labor = st.checkbox("Zero-Forced-Labor Field Certifications Signed & Logged to DDS", value=True, key="bottom_chk_labor")

with col_input_right:
    st.markdown("##### 🔬 Pillar 2: Agricultural Processing & Infrastructure Discipline")
    measured_moisture = st.slider("Patio Batch Moisture Profile (%):", 8.0, 16.0, float(active_coop["Moisture Content"]), step=0.1, key="bottom_moisture_slider")
    chk_phyto = st.checkbox("Accredited Third-Party Phytosanitary Stamp (ISPM 12 Ready)", value=("Passed ✅" in str(active_coop["Phytosanitary Inspection"])), key="bottom_chk_phyto")
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

# 4. Render Executive Results & ROI Matrix Panel
st.subheader("🎯 Enterprise Operational Maturity Output")
res_col1, res_col2 = st.columns(2)

with res_col1:
    st.markdown(f"### Score: `{milestones_passed} / 8`")
    st.markdown(f"##### Assigned Rating:\n**<span style='color:{tier_color}'>{maturity_tier}</span>**", unsafe_allow_html=True)
    st.markdown(f"**Current Risk Profile:** {risk_profile}")
    st.markdown(f"**Consultative Strategy Move:** {strategic_directive}")
    
with res_col2:
    st.markdown("#### 💰 Sourcing Risk Value Protection Matrix")
    st.caption("Quantifying the financial losses mitigated by this first-mile digital pre-check.")
    
    container_value_usd = 75000.00
    exposure_saved_mold = container_value_usd if not is_moisture_compliant else 0.0
    exposure_saved_eudr = (container_value_usd * 0.04) if not chk_gps else 0.0
    exposure_saved_demurrage = 4500.00 if (not chk_phyto or not chk_tin) else 0.0
    total_exposure_mitigated = exposure_saved_mold + exposure_saved_eudr + exposure_saved_demurrage
    
    st.write(f"• **Biological Mold Loss Prevented:** `${exposure_saved_mold:,.2f}`")
    st.write(f"• **EUDR Border Penalty Defended:** `${exposure_saved_eudr:,.2f}`")
    st.write(f"• **Port Demurrage Debt Prevented:** `${exposure_saved_demurrage:,.2f}`")
    st.metric(label="Total Financial Risk Exposure Mitigated by Advisor", value=f"${total_exposure_mitigated:,.2f}", delta=f"${total_exposure_mitigated:,.2f} Saved")

st.divider()

# 5. Executive Export Control Desk
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
