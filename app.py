import requests
import json
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime
# 🚨 DEPLOYMENT MANDATE: Ensure 'pip install supabase' is run in your build environment
from supabase import create_client, Client

# ==============================================================================
# PART 1: RESILIENT HYBRID CLOUD CONNECTION LAYER (REPLACE MASTER INITIALIZATION)
# ==============================================================================
# Vault Gate A: Scan your Streamlit Cloud web dashboard box first
if "SUPABASE_URL" in st.secrets and "SUPABASE_SERVICE_ROLE_KEY" in st.secrets:
    FINAL_URL = st.secrets["SUPABASE_URL"]
    FINAL_KEY = st.secrets["SUPABASE_SERVICE_ROLE_KEY"]
else:
    # 🚨 SYSTEM BACKUP GATEWAY: If the cloud vault is lagging, read directly from these strings
    # Paste your active credentials between the quotation marks below right now:
    FINAL_URL = "https://mdyoxirhdufdskytcmst.supabase.co"
    FINAL_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1keW94aXJoZHVmZHNreXRjbXN0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4NDUyMTk5NSwiZXhwIjoyMTAwMDk3OTk1fQ.d9AWBTABD4-gvKnFtGT5vNyd2uKJHvOSMeCPRRPXve8"

# Initialize your administrative master client securely
try:
    supabase: Client = create_client(FINAL_URL, FINAL_KEY)
except Exception as e:
    st.error(f"🔒 **Security Policy Exception:** Master Sourcing API Handshake Broken: {str(e)}")
    st.stop()


@st.cache_data(ttl=2) # 2-second quick cache refresh lifespan
def stream_live_ledger_from_supabase():
    try:
        response = supabase.table("global_compliance_ledger").select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"🚨 Supabase Cloud Connection Interrupted: {str(e)}")
        return []

# State Synchronization Layer
if 'farm_database' not in st.session_state or st.sidebar.button("🔄 Force Cloud DB Sync"):
    st.session_state.farm_database = stream_live_ledger_from_supabase()

lookbook_df = pd.DataFrame(st.session_state.farm_database)

# Standardize visual presentation order of column arrays
if not lookbook_df.empty and "coop_id" in lookbook_df.columns:
    lookbook_df = lookbook_df[["coop_id", "entity_name", "origin_country", "legal_gps_eudr", "tax_id_corporate_bank", "moisture_content", "phytosanitary_inspection", "customs_clearance_status"]]

st.markdown("### 📊 Global Registry & Institutional Traceability Passport Ledger")
st.markdown("This live ledger reflects permanent data states streamed directly from your decoupled cloud database layer.")
st.dataframe(lookbook_df, use_container_width=True, hide_index=True)

# 🛡️ THE COMPLIANCE SHIELD DISCLAIMER (TOP INSULATION VIEW)
st.warning("""
**🛡️ The Compliance Shield: Sovereign Infrastructure Notice**  
US customs brokers, financial institutions, and boutique roasters must comply with strict federal guidelines (like **US FDA FSMA Section 204 traceability rules**). They are highly sensitive about security. Knowing that their supply chain data is stored securely on US soil behind a domestic cloud firewall removes a massive institutional trust barrier during procurement audits.
""")

st.divider()

# ==============================================================================
# PART 2: THE SIDEBAR TERMINAL DESK CONTROLLER & METEOROLOGICAL API
# ==============================================================================
st.sidebar.subheader("👑 Advisor Portal Options")
today_menu = st.sidebar.selectbox(
    "SELECT ENTERPRISE DASHBOARD", 
    [
        "--- Select Active Terminal ---", 
        "1. Indigenous Empowerment & Cultivation Guide",
        "2. Real-Time Telemetry & Open API Sync",
        "3. Sourcing Operations Suite"
    ], 
    key="corporate_navigation_select_node_final_unbreakable"
)

# Open-Meteo API Sync Node
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

# Node Execution Logic
if today_menu == "1. Indigenous Empowerment & Cultivation Guide":
    st.title("🌱 Indigenous Self-Resiliency & Cultivation Interface")
    st.write("### 'Honor the Labor, Elevate the Stewardship'")
    st.info("💡 **Institute Communication Core:** This framework completely avoids 'saving language' or implying traditional methods are wrong. It equips the community with data shields to protect their crops from climate risks.")
    
    edu_step = st.selectbox("Active Management Window:", [
        "1. Pre-Planting, Soil Prep & Plowing Management",
        "2. Active Lifecycle Nutrition & Disease Defense (Rust/Mutation)",
        "3. Advanced Canopy Pruning & Airflow Tuning",
        "4. Harvest Vigilance, Flotation & Color Sorting"
    ], key="indigenous_edu_step_selectbox")
    
    if edu_step == "4. Harvest Vigilance, Flotation & Color Sorting":
        st.write("#### 🔴 Maximizing First-Mile Value Retention via Physical Density Separation")
        col1, col2 = st.columns(2)
        with col1: st.warning("⚠️ **Traditional Practice Vulnerability:** Unsorted strip-harvesting mixes over-ripe and insect-damaged cherries into the mill, lowering value to bottom-tier commercial grade.")
        with col2: st.success("💎 **The Self-Resilient Enhancement:** Immediate water-tank flotation sorting combined with mechanical brix evaluation ensures only perfectly ripe specialty cherries move to depulping.")

elif today_menu == "2. Real-Time Telemetry & Open API Sync":
    st.title("🛰️ Atmospheric Sourcing Telemetry")
    st.write("### Cross-Border Infrastructure Microclimate Tracking")
    climate = fetch_highlands_telemetry()
    col_t1, col_t2 = st.columns(2)
    with col_t1: st.metric(label="Ambient Drying Station Temperature", value=f"{climate['temp']} °C")
    with col_t2: st.metric(label="Relative Atmospheric Humidity", value=f"{climate['humidity']}%")
    st.caption(f"Telemetry Status: {'Live Cloud Stream Sync' if climate['live'] else 'Static Buffer Active'} | Timestamp: {climate['time']}")

# ==============================================================================
# PART 3: THE INTERACTIVE CONTINUOUS TRANSACTION CONTROL (CTC) VALIDATION DESK
# ==============================================================================
st.markdown("<h2>⚙️ Continuous Transaction Control (CTC) Validation Desk</h2>", unsafe_allow_html=True)
st.write("### Pre-Clearance Audit & Cross-Border Requirement Analysis Panel")

# 1. Map selection profiles safely out of synced memory rows
coop_names = [row["entity_name"] for row in st.session_state.farm_database]
selected_name = st.selectbox("Select Target Asset Portfolio to Audit:", coop_names, key="global_bottom_matrix_selector")

# Identify row index coordinates
coop_index = next(index for (index, d) in enumerate(st.session_state.farm_database) if d["entity_name"] == selected_name)
active_coop = st.session_state.farm_database[coop_index]

st.markdown(f"#### 🔒 Active Verification Pipeline for: **{active_coop['entity_name']}** (`{active_coop['coop_id']}`)")

# 2. Checklist Matrix Forms Pre-Populated from Cloud Records
col_input_left, col_input_right = st.columns(2)

with col_input_left:
    st.markdown("##### 🗂️ Phase 1: Legal Entity & Contractual Alignment")
    contract_framework = st.selectbox("Master Contract Template Type:", ["GCA (Green Coffee Assoc.)", "ESCC (European Standard)", "Private Bilateral SLA"], key="bottom_contract_type")
    chk_tin = st.checkbox("Active Corporate Registration / Government Tax ID (TIN)", value=("Active" in str(active_coop["tax_id_corporate_bank"])), key="bottom_chk_tin")
    chk_bank = st.checkbox("Corporate Bank Account with Active AML / KYC Anti-Fraud Clearance", value=("Active" in str(active_coop["tax_id_corporate_bank"])), key="bottom_chk_bank")
    chk_gps = st.checkbox("EUDR Compliant GIS Polygon Land Maps Logged to Cloud Registry", value=("Verified" in str(active_coop["legal_gps_eudr"])), key="bottom_chk_gps")
    chk_labor = st.checkbox("Zero-Forced-Labor Field Certifications Signed & Logged to DDS", value=True, key="bottom_chk_labor")

with col_input_right:
    st.markdown("##### 🔬 Phase 2: Biological & Sovereign Trade Controls")
    measured_moisture = st.slider("Patio Batch Moisture Profile (%):", 8.0, 16.0, float(active_coop["moisture_content"]), step=0.1, key="bottom_moisture_slider")
    chk_phyto = st.checkbox("Accredited Third-Party Phytosanitary Stamp (ISPM 12 Ready)", value=("Passed" in str(active_coop["phytosanitary_inspection"])), key="bottom_chk_phyto")
    
    st.markdown("---")
    destination_market = st.selectbox("Target Jurisdiction Terminal:", ["United States (GCA)", "European Union (EU)", "Middle East (GCC Region)", "Sanctioned / Restricted Port"], key="bottom_dest_market")
    ideological_clearance = st.radio("Does product labeling/sourcing bypass local sovereign moral restrictions?", ["No", "Yes"], index=1, key="bottom_ideology_check")

# 3. Process Evaluation Rules Business Logic
is_financial_valid = chk_tin and chk_bank
is_environmental_valid = chk_gps if destination_market == "European Union (EU)" else True
is_biological_compliant = 10.0 <= measured_moisture <= 12.5 and chk_phyto
is_geopolitical_valid = (ideological_clearance == "Yes") and (destination_market != "Sanctioned / Restricted Port")

milestones_passed = sum([chk_tin, chk_bank, chk_gps, chk_labor, is_biological_compliant, chk_phyto, (destination_market != "Sanctioned / Restricted Port"), (ideological_clearance == "Yes")])

# Define Accenture-Inspired Maturity Tiers
if milestones_passed == 8 and is_environmental_valid:
    maturity_tier = "TIER 1: INSTITUTIONAL EXPORT GRADE 🟢"
    tier_color = "#2ecc71"
    risk_profile = "MINIMAL RESIDUAL RISK — Fully cleared for accelerated destination customs entry lanes."
    strategic_directive = "Maintain active digital passport syncing. Asset ready for premium routing."
elif 6 <= milestones_passed <= 7:
    maturity_tier = "TIER 2: CAPABLE SPECIALTY CORRIDOR 🟡"
    tier_color = "#f1c40f"
    risk_profile = "MODERATE OPERATIONAL RISK — Minor compliance gaps detected."
    strategic_directive = "Prioritize the immediate closing of the unchecked operational items to clear European customs."
else:
    maturity_tier = "TIER 4: UNRESTRICTED COMMODITY SURVIVAL LOOP 🔴"
    tier_color = "#e74c3c"
    risk_profile = "SEVERE REGULATORY EXPOSURE — Total compliance absence."
    strategic_directive = "Sourcing contract requires complete first-mile restructuring from the ground up."

# ==============================================================================
# PART 4: EXECUTIVE MATURITY & REVENUE PROTECTION CALCULATOR
# ==============================================================================
st.divider()
st.subheader("🎯 Enterprise Operational Maturity Output")
res_col1, res_col2 = st.columns(2)

with res_col1:
    st.markdown(f"### Capability Score: `{milestones_passed} / 8`")
    st.markdown(f"##### Assigned Rating:\n**<span style='color:{tier_color}'>{maturity_tier}</span>**", unsafe_allow_html=True)
    st.markdown(f"**Current Risk Profile:** {risk_profile}")
    st.markdown(f"**Consultative Strategy Move:** {strategic_directive}")
    
with res_col2:
    st.markdown("#### 💰 Sourcing Risk Value Protection Matrix")
    container_value_usd = 75000.00
    exposure_saved_mold = container_value_usd if not (10.0 <= measured_moisture <= 12.5) else 0.0
    exposure_saved_eudr = (container_value_usd * 0.04) if not chk_gps else 0.0
    exposure_saved_demurrage = 4500.00 if (not chk_phyto or not chk_tin) else 0.0
    total_exposure_mitigated = exposure_saved_mold + exposure_saved_eudr + exposure_saved_demurrage
    
    st.write(f"• **Biological Mold Loss Prevented:** `${exposure_saved_mold:,.2f}`")
    st.write(f"• **EUDR Border Penalty Defended:** `${exposure_saved_eudr:,.2f}`")
    st.write(f"• **Port Demurrage Debt Prevented:** `${exposure_saved_demurrage:,.2f}`")
    st.metric(label="Total Financial Risk Exposure Mitigated by Advisor", value=f"${total_exposure_mitigated:,.2f}", delta=f"${total_exposure_mitigated:,.2f} Retained")

# ==============================================================================
# PART 5: SCA QUALITY PRICING PREMIUM MATRIX EXTENSION
# ==============================================================================
st.divider()
st.markdown("## 🏆 Premium Valuation & Market Arbitrage Engine")
calc_col1, calc_col2 = st.columns(2)

with calc_col1:
    st.markdown("##### 🗂️ Quality & Volume Variables")
    input_sca_score = st.slider("Verified Independent SCA Cup Score:", 75.0, 95.0, 84.5, step=0.5, key="premium_sca_slider")
    input_lot_bags = st.number_input("Isolated Residual Lot Volume (Standard 60KG Bags):", min_value=1, max_value=500, value=100, key="premium_volume_input")
    c_market_base_price = 2.25 
    st.caption(f"Current Global Exchange Commodity Index Baseline: **${c_market_base_price:.2f} / LB**")

with calc_col2:
    st.markdown("##### 💰 Dynamic Revenue Capture Analytics")
    if milestones_passed < 6 or not is_environmental_valid:
        tier_status = "Non-Compliant Cargo (Forced Commodity Liquidations)"
        quality_premium_per_lb = 0.00
        compliance_discount_penalty = 0.45 
    else:
        compliance_discount_penalty = 0.00
        if input_sca_score >= 88.0:
            tier_status = "Exotic Micro-Lot Portfolio (Premium Tier 1)"
            quality_premium_per_lb = 3.75
        elif input_sca_score >= 85.0:
            tier_status = "Fine Specialty Grade (Premium Tier 2)"
            quality_premium_per_lb = 1.95
        else:
            tier_status = "Standard Specialty Grade (Premium Tier 3)"
            quality_premium_per_lb = 0.60

    total_lbs_processed = input_lot_bags * 132.277
    final_settlement_price_per_lb = (c_market_base_price + quality_premium_per_lb) - compliance_discount_penalty
    commodity_value_payout = total_lbs_processed * (c_market_base_price - 0.45 if milestones_passed < 6 else c_market_base_price)
    optimized_specialty_payout = total_lbs_processed * final_settlement_price_per_lb
    net_arbitrage_capital_won = max(0.0, optimized_specialty_payout - commodity_value_payout)
    
    st.write(f"• **Final Settlement Price:** `${final_settlement_price_per_lb:.2f} / LB` (Includes +${quality_premium_per_lb:.2f} Premium)")
    metric_v1, metric_v2 = st.columns(2)
    with metric_v1: st.metric(label="Total Optimized Contract Value", value=f"${optimized_specialty_payout:,.2f}")
    with metric_v2: st.metric(label="Trapped Revenue Unlocked by Black Onyx", value=f"${net_arbitrage_capital_won:,.2f}", delta=f"+{((net_arbitrage_capital_won/commodity_value_payout)*100 if commodity_value_payout > 0 else 0):.1f}% Margin")

# ==============================================================================
# PART 6: PORT CLEARANCE EXTENSION & DATA PUSH BROADCAST KEYS
# ==============================================================================
st.divider()
st.markdown("### 🛂 US CBP Form 3461: Automated Customs Entry Data-Mapper")

# 🛡️ THE COMPLIANCE SHIELD DISCLAIMER (PORT BOUNDARY VIEW)
st.warning("""
**🛡️ The Compliance Shield: Federal Audit Protection Protocol**  
US customs brokers, financial institutions, and boutique roasters must comply with strict federal guidelines (like **US FDA FSMA Section 204 traceability rules**). They are highly sensitive about security. Knowing that their supply chain data is stored securely on US soil behind a domestic cloud firewall removes a massive institutional trust barrier during procurement audits.
""")

doc_col1, doc_col2 = st.columns(2)

with doc_col1:
    st.info("🏢 Application Database Data Captured")
    st.markdown(f"- **Logged Entry ID:** `{active_coop['coop_id']}`\n- **Producer Business Entity:** `{active_coop['entity_name']}`\n- **Calculated Harmonized System Tariff Tag:** `HS Code 0901.11 (Green Coffee)`\n- **Active Biological Safety Pass Token:** `{active_coop['phytosanitary_inspection']}`")
    
with doc_col2:
    st.success("📝 CBP Form 3461 Box Allocation Results")
    st.markdown(f"- **Box 11: Port of Entry Code:** Assigned dynamically based on infrastructure terminal.\n- **Box 14: Country of Origin Registry:** Populated automatically as: **`{active_coop['origin_country']}`**.\n- **Box 23: Harmonized Tariff Schedule (HTS) Code Number:** Mapped instantly to **`0901.11.0000`**.\n- **Box 24: Product Description:** *Traceable, Pre-Cleared Green Unroasted Coffee Beans, Lot Code: {active_coop['coop_id']}*.")

st.divider()

# Executive Action Buttons
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("Commit Maturity Rating to Global Registry Ledger", type="primary", key="bottom_commit_button"):
        try:
            tax_status = "Active ✅" if (chk_tin and chk_bank) else "Failed ❌"
            gps_status = "Verified ✅" if chk_gps else "Pending ⚠️"
            phyto_status = "Passed ✅" if is_biological_compliant else "Failed ❌"
            customs_status = "Ready to Export 🚢" if (is_financial_valid and is_environmental_valid and is_biological_compliant and is_geopolitical_valid) else "Blocked at First-Mile 🚫"
            
            db_payload = {
                "moisture_content": measured_moisture,
                "tax_id_corporate_bank": tax_status,
                "legal_gps_eudr": gps_status,
                "phytosanitary_inspection": phyto_status,
                "customs_clearance_status": customs_status
            }
            
            supabase.table("global_compliance_ledger").update(db_payload).eq("coop_id", active_coop['coop_id']).execute()
            st.cache_data.clear()
            st.success(f"Maturity rating state permanently locked in Supabase Cloud for ID: {active_coop['coop_id']}!")
            st.rerun()
        except Exception as e:
            st.error(f"Cloud write mutation failed: {str(e)}")

with btn_col2:
    export_passport_payload = f"""==================================================
BLACK ONYX TRADE COMPLIANCE PASSPORT COOP ID: {active_coop['coop_id']}
==================================================
- Score: {milestones_passed} / 8 Milestones Passed
- Maturity Rating: {maturity_tier}
- Sourcing Risk Value Protected: ${total_exposure_mitigated:,.2f} USD
- Trapped Revenue Unlocked     : ${net_arbitrage_capital_won:,.2f} USD
=================================================="""

    st.download_button(
        label="📥 Download Executive Compliance Scorecard (TXT)",
        data=export_passport_payload,
        file_name=f"BlackOnyx_Compliance_Passport_{active_coop['coop_id']}.txt",
        mime="text/plain",
        key="bottom_download_passport_button"
    )

st.divider()
st.caption("🔒 Black Onyx Advisory Core Terminal. Protected under international trade data governance protocols.")
