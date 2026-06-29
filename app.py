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
    "3. Sovereign Hub & Global Insurance"
])

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
    "3. Sovereign Hub & Global Insurance"
])

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
        st.info("🔹 **AUTOMATED INSURANCE SHIELD TRIGGERED (Data-Verified)**\n\nTelemetry sensors registered critical prolonged moisture traps. \n\n**Sovereign Liquidation Output:** Global Climate Funds automatically route a **฿35,000 THB emergency cash installment** to the independent farmer's account. This covers immediate local picker wages and family food security, eliminating the need to ask local middlemen for predatory survival loans.\n\n*Advisory Note: Because telemetry logs verified the producer completed Phase 2 pruning, they qualify for instant automated liquidation.*")
        
    elif weather_anomaly_simulation == "Sudden High-Altitude Frost / Thermal Shock Event":
