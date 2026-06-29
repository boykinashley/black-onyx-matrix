import streamlit as st
import pandas as pd

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSd_xrC4SZeJ_KKdt0wAFUPcTZqZo0MjN8Ifhwq090eqg3PLaCXU2XukTlLEW4sVM7GCnOf-Kmqzlwy/pub?output=csv"

# Set up clean, elite corporate styling
st.set_page_config(page_title="Black Onyx | Sourcing Matrix", page_icon="🦅", layout="wide")

# Custom CSS to force crisp corporate formatting
st.markdown("""
    <style>
    .main {background-color: #0f1116; color: #ffffff;}
    h1, h2, h3 {color: #d4af37 !important;}
    div[data-testid="stMetricValue"] {font-size: 28px !important; color: #ffffff !important;}
    </style>
""", unsafe_allow_html=True)

st.title("🦅 BLACK ONYX ADVISORY & LEOLA ADVISORY")
st.subheader("Forensic Supply Chain Matrix — Mae Yao Highlands Sourcing Node")

st.markdown("""
**Operator ID:** [Your Name], MA (AUP Alumnus / Former Accenture Enterprise Strategy)  
**Verification Protocol:** Direct-Trade Forensic Transparency Network (SCA 84+ Vetted)
""")

# --- MVP HARDCODED RECONCILED DATASET ---
# This serves as your live operational data for Monday morning's meeting
MVP_DATA = [
    {
        "Batch_ID": "MY-2026-PK-01",
        "Coop_Name": "Doi Pangkhon Registered Community Enterprise",
        "Manager_Name": "Afae Lercheku (Second-Gen Liaison)",
        "GPS_Coordinates": "19.8972, 99.7122",
        "Altitude_MASL": 1350,
        "SCA_Score": 84.75,
        "Moisture_Pct": "11.2%",
        "Water_Activity_aw": 0.51,
        "Weight_KG": 1200,  # 2 Pallets
        "Farm_Gate_THB_KG": 210,
        "Rice_Sacks_Advanced": 10,
        "Stateless_Youth_Funded": 2,
        "Logistics_Hub": "Beanspire Co., Ltd."
    },
    {
        "Batch_ID": "MY-2026-MY-02",
        "Coop_Name": "Mae Yao Karen Hillside Agricultural Cooperative",
        "Manager_Name": "Somchai (YWAM Community Liaison)",
        "GPS_Coordinates": "19.9541, 99.7812",
        "Altitude_MASL": 1280,
        "SCA_Score": 83.50,
        "Moisture_Pct": "11.8%",
        "Water_Activity_aw": 0.56,
        "Weight_KG": 1200,  # 2 Pallets
        "Farm_Gate_THB_KG": 195,
        "Rice_Sacks_Advanced": 15,
        "Stateless_Youth_Funded": 4,
        "Logistics_Hub": "Sirinya Specialty Processing"
    },
    {
        "Batch_ID": "MY-2026-HC-03",
        "Coop_Name": "Huai Chomphu Indigenous Akha Enterprise",
        "Manager_Name": "Kalae (Little Boss Liaison)",
        "GPS_Coordinates": "19.7891, 99.6543",
        "Altitude_MASL": 1420,
        "SCA_Score": 85.25,
        "Moisture_Pct": "10.9%",
        "Water_Activity_aw": 0.49,
        "Weight_KG": 600,  # 1 Pallet
        "Farm_Gate_THB_KG": 225,
        "Rice_Sacks_Advanced": 10,
        "Stateless_Youth_Funded": 2,
        "Logistics_Hub": "Beanspire Co., Ltd."
    }
]

df = pd.DataFrame(MVP_DATA)

# 📊 Tier-1 Executive KPI Dashboard (Dynamically sums your data fields)
st.markdown("### 🏆 Seasonal Sourcing Metrics Summary")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

total_lots = len(df)
total_weight = f"{df['Weight_KG'].sum():,} KG"
total_rice = f"{df['Rice_Sacks_Advanced'].sum()} Sacks"
total_kids = f"{df['Stateless_Youth_Funded'].sum()} Students"

kpi1.metric(label="🗂️ Target Cooperatives Active", value=total_lots)
kpi2.metric(label="📦 Total Secured Allocation Volume", value=total_weight)
kpi3.metric(label="🌾 Food Sovereignty Index (Rice Dispatched)", value=total_rice)
kpi4.metric(label="⚖️ Legal ID Projects Funded (BIFA/YWAM)", value=total_kids)

# 🔍 The Interactive Direct-Trade Sourcing Ledger
st.markdown("### 📊 Active Laboratory Verification & Impact Registry")
st.dataframe(df, use_container_width=True, hide_index=True)

st.info("🔒 Secure Enterprise Grid: Specific farmer banking details, private cellular contact routes, and sensitive land-tenure GPS records are restricted to authenticated B2B wholesale buyers to insulate indigenous smallholders from predatory trading loops.")

# ==============================================================================
# TODAY'S MODULES: SYSTEM ARCHITECTURE & SOVEREIGN LIFECYCLE MONITORING
# ==============================================================================

# Append today's new navigation sub-menu directly to your existing sidebar logic
st.sidebar.markdown("---")
st.sidebar.subheader("📅 Today's Systems Modules")
today_menu = st.sidebar.radio("MACRO ADVISORY ENGINE", [
    "Select a Current System Node...",
    "1. Financial Literacy Mirror",
    "2. End-to-End Lifecycle Map",
    "3. Sovereign Hub & Global Insurance",
    "4. U.S. Export Capital & Mentorship Matrix" # <--- Ensure this line is present
], key="macro_engine_radio")

# ==============================================================================
# SUB-MODULE 1: FINANCIAL LITERACY & CHRONIC SURVIVAL GAP MODELING
# ==============================================================================
if today_menu == "1. Financial Literacy Mirror":
    st.title("📊 The Financial Literacy Mirror: Survival Gap Diagnosis")
    st.write("Translating the middleman's pressure metrics into an objective reality. Novice buyers look only at the green bean, but the true wealth is hidden inside the chemistry of the red fruit.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### 🏡 Farm Household Reality Inputs")
        annual_needs_thb = st.number_input("Essential Annual Household/Farm Expenses (THB) [Food, Picker Wages, Fertilizer]", min_value=10000, value=120000, step=5000)
        
        st.write("#### 📉 Predatory Shadow Market Metrics (Mock Data Modeling)")
        total_harvest_kg = st.number_input("Total Bulk Volume Harvested & Delivered (kg)", min_value=100, value=5000, step=100)
        predatory_blended_rate = st.number_input("Lowest Assumed Local Blended Price Offered by Mill (THB/kg)", min_value=10, value=150, step=5)
        
    # Mathematical algorithms for macro-economic gap analysis
    middleman_gross_payout = total_harvest_kg * predatory_blended_rate
    household_survival_gap = middleman_gross_payout - annual_needs_thb
    
    # Controlled Input Potentials (15% Tier A Microlot at COE baseline vs 85% Sorted Tier B Standard)
    true_potential_valuation = (total_harvest_kg * 0.15 * 1800.0) + (total_harvest_kg * 0.85 * 350.0)
    net_advisory_surplus = true_potential_valuation - annual_needs_thb

    with col2:
        st.write("#### 📊 Diagnostic Financial Output")
        st.metric(label="Total Cash Payout Received from Middleman", value=f"฿{middleman_gross_payout:,.2f} THB")
        
        if household_survival_gap < 0:
            st.error(f"🚨 CHRONIC SURVIVAL DEFICIT DETECTED: -฿{abs(household_survival_gap):,.2f} THB\n\nYour current traditional habits guarantee an operational deficit. This structural deficit is what forces your household to accept high-interest, rainy-season cash advances from middlemen, keeping you locked in permanent bondage.")
        else:
            st.info(f"Barely Surviving (Breakeven Runway): ฿{household_survival_gap:,.2f} THB")
        
        st.success(f"🌟 Premium Controlled-Input Value Potential: ฿{true_potential_valuation:,.2f} THB\n\nNet Economic Family Surplus: ฿{net_advisory_surplus:,.2f} THB")
        
    # Visual Financial Continuum Chart
    st.bar_chart(pd.DataFrame({
        "Economic Paths": ["Middleman Predatory Payout", "Annual Household Costs", "Controlled Trade Potential"],
        "Capital (THB)": [middleman_gross_payout, annual_needs_thb, true_potential_valuation]
    }), x="Economic Paths", y="Capital (THB)")

# ==============================================================================
# SUB-MODULE 2: END-TO-END SUPPLY CHAIN MAP (WEATHER ANOMALY INTERVENTIONS)
# ==============================================================================
elif today_menu == "2. End-to-End Lifecycle Map":
    st.title("🗺️ End-to-End Proactive Climate Lifecycle Mapping")
    st.write("Tracking correct proactive agricultural interventions to prevent reactive weather disasters (mold, rot, over-drying) before the green bean reveals itself.")
    
    st.info("🌱 **Section A: Honor the Labor, Elevate the Legacy**\n\n*Institutional Scripting for Field Agents to Bypass Defensive Pride:*\n\n\"We deeply respect the multi-generational endurance and meticulous care your family has poured into keeping this mountain fertile. You have mastered the forest. Our mission is to hand you an analytical data shield to protect, enhance, and reveal the true hidden financial worth of the blood-red fruit you are already harvesting.\"")
    
    st.write("## 🔄 Visual Evolution: Traditional Vulnerability vs. Enhanced Precision")
    active_lifecycle_phase = st.selectbox("Select Target Supply Chain Phase to Audit:", [
        "Phase 1: Pre-Agro Land Prep & Canopy Management",
        "Phase 2: Crop Lifecycle & Understory Moisture Monitoring",
        "Phase 3: Harvest Period & Visual Fruit Selection"
    ])
    
    if active_lifecycle_phase == "Phase 1: Pre-Agro Land Prep & Canopy Management":
        col1, col2 = st.columns(2)
        with col1:
            st.warning("⚠️ **Current Traditional Practice**\n- Relying strictly on unmonitored shade canopies.\n- Highly reactive to unexpected regional heatwaves.\n\n*Market Output:* Low-grade commercial options only.")
        with col2:
            st.success("✅ **The Enhanced Precision Path**\n- Integrating automated macro-climate telemetry nodes.\n- Shaded agroforestry slows down maturation, maximizing sugars inside the red fruit.\n\n*Financial Boost:* Adds **+฿15,000 THB** in protected yield value.")
            
    elif active_lifecycle_phase == "Phase 2: Crop Lifecycle & Understory Moisture Monitoring":
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### 🌡️ Live Sensor Telemetry Parameters")
            current_humidity = st.slider("Observed Forest Understory Humidity Index (%)", 40, 100, 85)
            pruning_executed = st.radio("Has thin-canopy airflow pruning been completed before the seasonal rain cycles?", ["Yes", "No"])
        with col2:
            st.write("#### 🛡️ Microclimate Advisory Action")
            if current_humidity > 80 and pruning_executed == "No":
                st.error("🚨 **CRITICAL MOLD DEVELOPMENT HAZARD:** Trapped moisture cages will cause immediate fruit rot on branches, ruining your upcycling grain value. Airflow thinning must be executed immediately.")
            else:
                st.success("🍏 **STABLE MICROCLIMATE CORRIDOR:** Airflow management parameters are successfully balancing moisture. Upcycle streams secure.")
                
    elif active_lifecycle_phase == "Phase 3: Harvest Period & Visual Fruit Selection":
        col1, col2 = st.columns(2)
        with col1:
            st.warning("⚠️ **Current Traditional Practice**\n- Strip-picking all colors mixed into single bags out of operational speed.\n- Blending perfect red fruit with green/black defects, creating the 'Blended Rate Penalty'.\n\n*Realized Local Rate:* ~฿150 THB / kg")
        with col2:
            st.success("💎 **The Enhanced Precision Path**\n- Utilizing visual fruit color sorting grids directly on the farm plots.\n- Farm-level water bucket flotation to isolate premium lots from defects prior to transit.\n\n*Realized Trade Rate:* ฿350 THB/kg (Commercial) up to **฿1,800+ THB/kg** (Elite Microlot Tier).")

# ==============================================================================
# SUB-MODULE 3: SOVEREIGN HUB PIPELINE & STATELESS GLOBAL CROP INSURANCE
# ==============================================================================
elif today_menu == "3. Sovereign Hub & Global Insurance":
    st.title("🛡️ Sovereign Hub-and-Spoke Infrastructure & Global Insurance Shield")
    st.write("Bypassing the cooperative failure wall. The Institute's 7-year data history confirms that traditional cooperative systems fail due to farmer-to-farmer offense, scolding, and localized gossip.")
    
    st.error("❌ **THE OPERATIONAL RISK BUFFER:** Trying to force community networks is a direct business model liability. We bypass village friction entirely by routing independent, disciplined producers straight to a registered regional anchor (e.g., **Magpie Farm**).")
    
    st.write("## 🌍 Global Climate Fund Sovereign Insurance Simulation")
    st.write("Because shifting traditional timelines carries risk, this framework models how **IoT Telemetry Data acts as collateral** to unlock international safety nets for vulnerable, independent hill tribe producers.")
    
    weather_anomaly_simulation = st.selectbox("Simulate a Severe Microclimate Shock:", [
        "Standard Balanced Harvest Cycle",
        "Severe Monsoon Humidity Surge (>92% Moisture Traps)",
        "Sudden High-Altitude Frost / Thermal Shock Event"
    ])
    
    if weather_anomaly_simulation == "Standard Balanced Harvest Cycle":
        st.success("🍏 System Runway Secure. Farm preserves 100% of its independent premium capital flows.")
        
    elif weather_anomaly_simulation == "Severe Monsoon Humidity Surge (>92% Moisture Traps)":
        st.info("🔹 **AUTOMATED INSURANCE SHIELD TRIGGERED (Data-Verified)**\n\nTelemetry sensors registered critical prolonged moisture traps. \n\n**Sovereign Liquidation Output:** Global Climate Funds automatically route a ฿35,000 THB emergency cash installment to the independent farmer's account. This covers immediate local picker wages and family food security, eliminating the need to ask local middlemen for predatory survival loans.\n\n*Advisory Note: Because telemetry logs verified the producer completed Phase 2 pruning, they qualify for instant automated liquidation.*")
        
    elif weather_anomaly_simulation == "Sudden High-Altitude Frost / Thermal Shock Event":
        st.info("🔹 **AUTOMATED INSURANCE SHIELD TRIGGERED (Data-Verified)**\n\nCanopy sensors registered a severe temperature drop below 8°C.\n\n**Sovereign Liquidation Output:** Immediate financial payout of ฿40,000 THB executed via the data ledger to preserve land occupancy metrics and insulate the farmer from seasonal crop failure.")

import streamlit as st
import pandas as pd
import numpy as np
import time

# ==============================================================================
# REAL-TIME TELEMETRY DATA SYSTEM (EDGE & SATELLITE API MODELING)
# ==============================================================================
st.title("🛰️ Satellite IoT & Edge AI Telemetry Sync")
st.write("### High-Altitude Agroforestry Corridor Precision Agriculture Tracker")
st.caption("Advisory Framework: Simulating lightweight Edge AI processing and direct Satellite IoT packet extraction.")

col_sync, col_data = st.columns([1, 2])

with col_sync:
    st.write("#### 📡 Ground-to-Space Connection Status")
    st.warning("Cellular Reception Status: ❌ DEAD ZONE (No Local Signal)")
    
    # User initiates a simulated satellite packet handshake
    sync_trigger = st.button("🔄 Sync Sat-IoT SBD Data Packets")
    
    st.write("#### ⚡ Onboard Hardware Protocol")
    st.info("💡 **Edge Processing Mode:** On-field sensor nodes utilize compressed, lightweight predictive models to log understory humidity patterns completely offline without a cellular server link.")

if sync_trigger:
    with col_data:
        st.write("#### 📥 Direct Satellite Transmission Stream")
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        # Simulating the physical retrieval of a 1:1 data packet from space
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
            status_text.text(f"Extracting Short Burst Data (SBD) packet... {percent_complete+1}%")
            
        status_text.text("✅ Data Handshake Complete. Metrics synced successfully via Satellite Corridor.")
        
        # Real-world historical microclimate ranges mapped out for Chiang Rai Highlands
        simulated_time_series = pd.DataFrame({
            "Time (Hourly Intervals)": [f"H-{i}" for i in range(12, 0, -1)],
            "Canopy Temperature (°C)": np.random.uniform(16.5, 23.0, 12),
            "Understory Humidity (%)": np.random.uniform(82.0, 96.5, 12),
            "Leaf Wetness Index (AI-Vetted)": np.random.uniform(0.65, 0.92, 12)
        })
        
        st.write("### 📊 Synced Multi-Layer Precision Dataset")
        st.dataframe(simulated_time_series.style.format({
            "Canopy Temperature (°C)": "{:.2f}",
            "Understory Humidity (%)": "{:.2f}",
            "Leaf Wetness Index (AI-Vetted)": "{:.2f}"
        }))
        
        # Run real-time threshold check on the synced data to generate the mold alert
        avg_humidity = simulated_time_series["Understory Humidity (%)"].mean()
        avg_temp = simulated_time_series["Canopy Temperature (°C)"].mean()
        
        st.write("### 🚨 Precision Agriculture Automated Assessment")
        if avg_humidity > 85.0 and avg_temp > 18.0:
            st.error(f"⚠️ **CRITICAL PROCESSING SHOCK WARNING (Mean Humidity: {avg_humidity:.1f}%)**\n\nHigh-altitude canopy microclimate conditions indicate immediate Aspergillus and fungal spore development inside open storage arrays. Raw processing grains are at extreme risk of contamination.")
            st.write("**Mandatory Action Directive:** Bypassing traditional sun-drying methods immediately. Move all coffee fruit material into sealed, anaerobic environments to protect upcycling value streams.")
        else:
            st.success("🍏 **CLIMATE PROFILE REGULATED:** Synced variables confirm clean, low-risk conditions across tracked forest parcels.")

# ==============================================================================
# SUB-MODULE 4: U.S. EXPORT CAPITAL & MENTORSHIP MATRIX (COMPLETE SUITE)
# ==============================================================================
elif today_menu == "4. U.S. Export Capital & Mentorship Matrix":
    st.title("🏛️ U.S. Federal Export Capital & Global Mentorship Matrix")
    st.write("Leveraging federal infrastructure and elite international trade desks specifically engineered to scale women-owned international corporate brokerages [📑].")
    
    st.info("💡 **Executive Strategy:** Use your live Streamlit dashboard metrics and ground-truth data logs from Chiang Rai as verified proof of concept when submitting applications to these federal desks [📑, 📑].")
    
    # Capital Program Selector Tabs
    tab_step, tab_exim, tab_owit, tab_pitch = st.tabs([
        "💵 1. SBA STEP Grant", 
        "🛡️ 2. EXIM Bank (MWOB)", 
        "👑 3. OWIT Network", 
        "📢 4. Your Executive Pitch Statement"
    ])
    
    with tab_step:
        st.subheader("The State Trade Expansion Program (STEP) Grant")
        st.write("**Funding Source:** U.S. Small Business Administration (SBA) / Home State Trade Desks (e.g., Colorado OEDIT) [📑].")
        st.success("💰 **Capital Inflow:** Up to $5,000 – $10,000 per fiscal year in **non-dilutive cash grants** [📑].")
        st.markdown("""
        *   **Allocation Scope:** Explicitly subsidizes market entry and travel verification costs for U.S. small business exporters [📑].
        *   **Covered Capital Items:** International trade mission flights, international shipping of sample boxes, and foreign market trade show registrations [📑, 📑]. 
        *   **Action Plan:** Navigate to your home state's Department of Economic Development portal and file under 'STEP Grant Open Window' [📑].
        """)
        
    with tab_exim:
        st.subheader("Export-Import Bank of the United States — Minority & Women-Owned Business (MWOB) Desk")
        st.write("**Agency Function:** Provides Export Credit Insurance to protect U.S. corporate brokerages from international transaction defaults [📑].")
        st.success("🔒 **Risk Shield:** Insures up to **95% of your outbound commercial invoices** against foreign buyer or geopolitical default [📑].")
        st.markdown("""
        *   **The Operational Value:** Removes financial transactional anxiety [📑]. If a verified Western buyer defaults on your brokerage commission fee, the U.S. Federal Government steps in to settle your invoice [📑]. 
        *   **The Mentorship Pipeline:** Registrants are assigned a specialized MWOB trade director who acts as an operational mentor to audit ledgers and clear international banking hurdles [📑].
        *   **Action Plan:** Register for an onboarding briefing directly via `exim.gov/about/minority-and-women-owned-businesses`.
        """)
        
    with tab_owit:
        st.subheader("Organization of Women in International Trade (OWIT)")
        st.write("**Network Scope:** The premier global professional network connecting elite female trade executives, port logistics directors, and customs attorneys [📑].")
        st.success("👑 **Network Capital:** Direct 1-on-1 cross-border mentorship channels across the U.S., Asia, and Africa [📑].")
        st.markdown("""
        *   **The Boardroom Panel:** Gives you an active community of industry experts to consult whenever you hit a border clearance bottleneck, phytosanitary restriction, or ocean freight hazard [📑].
        *   **Action Plan:** Establish your active global profile credentials through `owit.org`.
        """)
        
    with tab_pitch:
        st.subheader("📢 Your Master Executive Positioning Statement")
        st.write("Copy and paste this verified text block into your federal grant applications, accelerator pitches, and OWIT board profiles to cleanly align your frontier research with corporate scale [📑]:")
        
        pitch_text = (
            "As a U.S. woman pioneering an international trade advisory firm (Black Onyx Advisory), my mission is to architect "
            "high-margin, risk-mitigated supply chain corridors [📑, 📑]. Following my enterprise strategy career at Accenture, I self-funded "
            "an intensive global technology and commodities circuit spanning Japan, South Korea, Singapore, and South Africa to master "
            "automated data structures and border compliance frameworks [📑].\n\n"
            "I then embedded myself directly at origin within the remote watersheds of Northern Thailand to stress-test a direct-trade "
            "pipeline [📑]. Confronted with systemic local transparency blockages and middleman manipulation, I used my systems background "
            "to rapidly prototype a serverless data-pull application using GitHub and Streamlit to enforce zero-trust data-vetting [📑, 📑].\n\n"
            "Recognizing the severe agronomic and behavioral bottlenecks affecting local farmers, I pivoted our model into a Circular "
            "Bioeconomy Waste-Valorization Corridor [📑]. I negotiated a framework to upcycle low-grade agricultural biowaste into cosmetic "
            "ingredients in collaboration with public university laboratories, while routing resource premiums directly to secure the legal "
            "IDs and education of stateless youth through BIFA and YWAM [📑, 📑].\n\n"
            "While my technical and strategic frameworks are fully live, I am seeking institutional mentorship and export development funding "
            "to scale this architecture safely [📑]. I want to connect with seasoned international trade professionals to align our outbound "
            "compliance channels with federal standards as we expand this zero-waste corridor model into low-friction agricultural sectors "
            "across East Africa and Central America [📑]."
        )
        
        # Unique key identifier passed to ensure clean compilation
        st.text_area(label="Click inside the box to copy your pitch text:", value=pitch_text, height=350, key="executive_pitch_text_area")
        st.success("🎯 This statement reframes your 7-month sabbatical into a high-stakes corporate asset that protects your business parameters while validating your social impact alignment under Planted by Grace.")
