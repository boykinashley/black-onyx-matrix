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

# Ensure today's necessary structural styles are injected safely into your application
st.markdown("""
    <style>
    .macro-advisory-title { font-size:24px !important; font-weight: bold; color: #4A3B32; background-color: #F4EBE1; padding: 12px; border-radius: 8px; border-left: 6px solid #8B5A2B; margin-top: 25px; margin-bottom: 15px;}
    .cultural-elevation-card { padding: 18px; border-radius: 8px; background-color: #E6F4EA; border-left: 5px solid #24B45C; margin-bottom: 20px; line-height: 1.6; }
    .vulnerability-card-now { padding: 15px; border-radius: 8px; background-color: #FDF6E2; border-left: 5px solid #D9822B; margin-bottom: 15px; }
    .vulnerability-card-future { padding: 15px; border-radius: 8px; background-color: #EBF7EE; border-left: 5px solid #2E7D32; margin-bottom: 15px; }
    .financial-metric-box { padding: 15px; border-radius: 8px; background-color: #F8F9FA; border-left: 5px solid #6D4C41; margin-bottom: 12px; font-size: 15px; }
    .chronic-deficit-box { padding: 15px; border-radius: 8px; background-color: #FFF0F0; border-left: 5px solid #D32F2F; margin-bottom: 15px; font-size: 15px; }
    .sovereign-insurance-box { padding: 18px; border-radius: 8px; background-color: #E8F0FE; border-left: 5px solid #1976D2; margin-bottom: 20px; }
    </style>
    """, unsafe_index=True)

# Add today's new options to your existing sidebar navigation logic block
# If your radio menu variable from yesterday is named differently, map it to match your conditional checks
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
    st.markdown("<p class='macro-advisory-title'>📊 The Financial Literacy Mirror: Survival Gap Diagnosis</p>", unsafe_index=True)
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
        st.markdown(f"<div class='financial-metric-box'><b>Total Cash Payout Received from Middleman:</b> ฿{middleman_gross_payout:,.2f} THB</div>", unsafe_index=True)
        
        if household_survival_gap < 0:
            st.markdown(f"<div class='chronic-deficit-box'><b>🚨 CHRONIC SURVIVAL DEFICIT DETECTED: -฿{abs(household_survival_gap):,.2f} THB</b><br>Your current traditional habits guarantee an operational deficit. This structural deficit is what forces your household to accept high-interest, rainy-season cash advances from middlemen, keeping you locked in permanent bondage.</div>", unsafe_index=True)
        else:
            st.markdown(f"<div class='financial-metric-box'><b>Barely Surviving (Breakeven Runway):</b> ฿{household_survival_gap:,.2f} THB</div>", unsafe_index=True)
        
        st.markdown(f"<div class='vulnerability-card-future'><b>🌟 Premium Controlled-Input Value Potential:</b> ฿{true_potential_valuation:,.2f} THB<br><b>Net Economic Family Surplus:</b> ฿{net_advisory_surplus:,.2f} THB</div>", unsafe_index=True)
        
    # Visual Financial Continuum Chart
    st.bar_chart(pd.DataFrame({
        "Economic Paths": ["Middleman Predatory Payout", "Annual Household Costs", "Controlled Trade Potential"],
        "Capital (THB)": [middleman_gross_payout, annual_needs_thb, true_potential_valuation]
    }), x="Economic Paths", y="Capital (THB)")

# ==============================================================================
# SUB-MODULE 2: END-TO-END SUPPLY CHAIN MAP (WEATHER ANOMALY INTERVENTIONS)
# ==============================================================================
elif today_menu == "2. End-to-End Lifecycle Map":
    st.markdown("<p class='macro-advisory-title'>🗺️ End-to-End Proactive Climate Lifecycle Mapping</p>", unsafe_index=True)
    st.write("Tracking correct proactive agricultural interventions to prevent reactive weather disasters (mold, rot, over-drying) before the green bean reveals itself.")
    
    st.markdown("<p class='cultural-header'>🌱 Section A: Honor the Labor, Elevate the Legacy</p>", unsafe_index=True)
    st.markdown("""
    <div class='cultural-elevation-card'>
        <b>Institutional Scripting for Field Agents to Bypass Defensive Pride:</b><br>
        <i>"We deeply respect the multi-generational endurance and meticulous care your family has poured into keeping this mountain fertile. You have mastered the forest. Our mission is to hand you an analytical data shield to protect, enhance, and reveal the true hidden financial worth of the blood-red fruit you are already harvesting."</i>
    </div>
    """, unsafe_index=True)
    
    st.write("## 🔄 Visual Evolution: Traditional Vulnerability vs. Enhanced Precision")
    active_lifecycle_phase = st.selectbox("Select Target Supply Chain Phase to Audit:", [
        "Phase 1: Pre-Agro Land Prep & Canopy Management",
        "Phase 2: Crop Lifecycle & Understory Moisture Monitoring",
        "Phase 3: Harvest Period & Visual Fruit Selection"
    ])
    
    if active_lifecycle_phase == "Phase 1: Pre-Agro Land Prep & Canopy Management":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='vulnerability-card-now'><b>Current Traditional Practice</b><br>• Relying strictly on unmonitored shade canopies.<br>• Highly reactive to unexpected regional heatwaves.<br><b>Market Output:</b> Low-grade commercial options only.</div>", unsafe_index=True)
        with col2:
            st.markdown("<div class='vulnerability-card-future'><b>The Enhanced Precision Path</b><br>• Integrating automated macro-climate telemetry nodes.<br>• Shaded agroforestry slows down maturation, maximizing sugars inside the red fruit.<br><b>Financial Boost:</b> Adds <b>+฿15,000 THB</b> in protected yield value.</div>", unsafe_index=True)
            
    elif active_lifecycle_phase == "Phase 2: Crop Lifecycle & Understory Moisture Monitoring":
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### 🌡️ Live Sensor Telemetry Parameters")
            current_humidity = st.slider("Observed Forest Understory Humidity Index (%)", 40, 100, 85)
            pruning_executed = st.radio("Has thin-canopy airflow pruning been completed before the seasonal rain cycles?", ["Yes", "No"])
        with col2:
            st.write("#### 🛡️ Microclimate Advisory Action")
            if current_humidity > 80 and pruning_executed == "No":
                st.markdown("<div class='danger-box'>🚨 <b>CRITICAL MOLD DEVELOPMENT HAZARD:</b> Trapped moisture cages will cause immediate fruit rot on branches, ruining your upcycling grain value. Airflow thinning must be executed immediately.</div>", unsafe_index=True)
            else:
                st.markdown("<div class='vulnerability-card-future'>🍏 <b>STABLE MICROCLIMATE CORRIDOR:</b> Airflow management parameters are successfully balancing moisture. Upcycle streams secure.</div>", unsafe_index=True)
                
    elif active_lifecycle_phase == "Phase 3: Harvest Period & Visual Fruit Selection":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='vulnerability-card-now'><b>Current Traditional Practice</b><br>• Strip-picking all colors mixed into single bags out of operational speed.<br>• Blending perfect red fruit with green/black defects, creating the 'Blended Rate Penalty'.<br><b>Realized Local Rate:</b> ~฿150 THB / kg</div>", unsafe_index=True)
        with col2:
            st.markdown("<div class='vulnerability-card-future'><b>The Enhanced Precision Path</b><br>• Utilizing visual fruit color sorting grids directly on the farm plots.<br>• Farm-level water bucket flotation to isolate premium lots from defects prior to transit.<br><b>Realized Trade Rate:</b> ฿350 THB/kg (Commercial) up to <b>฿1,800+ THB/kg</b> (Elite Microlot Tier).</div>", unsafe_index=True)

# ==============================================================================
# SUB-MODULE 3: SOVEREIGN HUB PIPELINE & STATELESS GLOBAL CROP INSURANCE
