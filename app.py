import io
import re
import requests
import json
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime
# 🚨 DEPLOYMENT MANDATE: Ensure 'pip install supabase pypdf' is run in your build environment
from supabase import create_client, Client
from pypdf import PdfReader, PdfWriter

# 1. Page Configuration Setup
st.set_page_config(
    page_title="Sovereign Supply Chain Engine", 
    layout="wide", 
    page_icon="🛡️"
)

st.title("🛡️ BLACK ONYX × LEOLA ADVISORY: AUTOMATED EXEC ADVISOR")
st.subheader("Decoupled 3-Tier Enterprise Role-Routing Node")
st.write("**Corporate Horizon:** Black Onyx Advisory × Leola Advisory | **Stewardship Mission:** Planted by Grace")

# 2. Resilient Hybrid Cloud Connection Layer
if "SUPABASE_URL" in st.secrets and "SUPABASE_SERVICE_ROLE_KEY" in st.secrets:
    FINAL_URL = st.secrets["SUPABASE_URL"]
    FINAL_KEY = st.secrets["SUPABASE_SERVICE_ROLE_KEY"]
else:
    # 🚨 SYSTEM BACKUP GATEWAY: Local/Codespace String Ingress Fallback
    FINAL_URL = "https://supabase.co"
    FINAL_KEY = "your-master-secret-service-role-api-key-string"

try:
    supabase: Client = create_client(FINAL_URL, FINAL_KEY)
except Exception as e:
    st.error(f"🔒 **Security Policy Exception:** Master Sourcing API Handshake Broken: {str(e)}")
    st.stop()

@st.cache_data(ttl=2) # 2-second quick cache refresh loop
def stream_live_ledger_from_supabase():
    try:
        response = supabase.table("global_compliance_ledger").select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"🚨 Supabase Cloud Connection Interrupted: {str(e)}")
        return []

# 3. State Synchronization Layer
if 'farm_database' not in st.session_state or st.sidebar.button("🔄 Force Cloud DB Sync"):
    st.session_state.farm_database = stream_live_ledger_from_supabase()

lookbook_df = pd.DataFrame(st.session_state.farm_database)

# Standardize visual presentation order of column arrays
if not lookbook_df.empty and "coop_id" in lookbook_df.columns:
    lookbook_df = lookbook_df[["coop_id", "entity_name", "origin_country", "legal_gps_eudr", "tax_id_corporate_bank", "moisture_content", "phytosanitary_inspection", "customs_clearance_status"]]

st.markdown("### 📊 Global Registry & Institutional Traceability Passport Ledger")
st.markdown("This live ledger reflects permanent data states streamed directly from your decoupled cloud database layer.")
st.dataframe(lookbook_df, use_container_width=True, hide_index=True)

# 🛡️ THE COMPLIANCE SHIELD DISCLAIMER
st.warning("""
**🛡️ The Compliance Shield: Sovereign Infrastructure Notice**  
US customs brokers, financial institutions, and boutique roasters must comply with strict federal guidelines (like **US FDA FSMA Section 204 traceability rules**). They are highly sensitive about security. Knowing that their supply chain data is stored securely on US soil behind a domestic cloud firewall removes a massive institutional trust barrier during procurement audits.
""")

st.divider()

# ==============================================================================
# PART 2: ROLE SELECTION HUB & WORKFLOW STATE INITIALIZATION
# ==============================================================================
st.sidebar.title("👤 Role Selection Workspace")

# Capture User Intent via your Simulated Role Selector dropdown matrix
current_role = st.sidebar.selectbox(
    "Simulate logging in as:", 
    [
        "1. Discovery & Diagnostic Panel", 
        "2. Cooperative Representative", 
        "3. Global Wholesale Buyer", 
        "4. Logistics & Customs Broker"
    ],
    key="multi_tenant_role_simulator_selector"
)

# Initialize System Master Step-Based Workflow States
if "current_step" not in st.session_state: st.session_state.current_step = 0
if "active_contingency" not in st.session_state: st.session_state.active_contingency = "Clear Transit"

if "workflow_data" not in st.session_state:
    st.session_state.workflow_data = {
        "coop_name": "Andean Coffee Co-Op", "coop_tax_id": "", "land_title_num": "",
        "lot_moisture": 12.0, "cupping_score": 84.5, "escrow_funded": False, "phyto_serial": "",
        "container_num": "", "carrier_scac": "", "bill_of_lading": "", "entry_num": "", "cbp_3461_status": "Locked"
    }

# Bind your asynchronous memory parameters straight to your active database rows
if not lookbook_df.empty:
    coop_profile_names = list(set(lookbook_df["entity_name"].dropna().tolist()))
    selected_coop_profile = st.sidebar.selectbox("Select Active Ledger Profile to Evaluate:", coop_profile_names, key="sidebar_active_profile_picker")
    coop_idx = next(index for (index, d) in enumerate(st.session_state.farm_database) if d["entity_name"] == selected_coop_profile)
    active_coop = st.session_state.farm_database[coop_idx]
    
    st.session_state.workflow_data["coop_name"] = active_coop["entity_name"]
    st.session_state.workflow_data["lot_moisture"] = float(active_coop["moisture_content"])
else:
    active_coop = {"coop_id": "COOP-LN01", "entity_name": "Default Cluster Node", "origin_country": "Global", "legal_gps_eudr": "Pending ⚠️", "tax_id_corporate_bank": "Failed ❌", "moisture_content": 12.0, "phytosanitary_inspection": "Failed ❌", "customs_clearance_status": "Blocked 🚫"}

st.sidebar.markdown(f"**Active Context:** `{current_role}`\n\n**Pipeline Step:** `Step {st.session_state.current_step}`\n\n**Transit Condition:** `{st.session_state.active_contingency}`")
st.sidebar.divider()

# ==============================================================================
# PART 3: DISCOVERY WORKSPACE & MULTI-USER WORKFLOW ENGINE
# ==============================================================================

# PANEL 1: INTAKE DIAGNOSTIC & COMPLIANCE FINANCIAL CALCULATOR
if current_role == "1. Discovery & Diagnostic Panel":
    st.title("🔍 Digital Maturity & Compliance Integrity Diagnostic")
    st.write("Assess how fragmented operations, manual handoffs, and paper documentation introduce financial risk.")
    st.info("💡 **Pitch Tip:** Guide your convention lead through these quick parameters to calculate their operational leakage.")

    col_profile1, col_profile2 = st.columns(2)
    with col_profile1:
        prospect_identity = st.selectbox("Identify Your Primary Alignment:", ["Select profile...", "Cooperative Representative / Origin Exporter", "US Importer / Wholesale Buyer"], key="p1_prospect_identity_selector")
    with col_profile2:
        annual_volume = st.number_input("Average volume of containers handled annually:", min_value=1, value=15, key="p1_annual_volume_input")

    if prospect_identity != "Select profile...":
        st.markdown("#### **📋 Core Operations Friction Audit**")
        q_custody = st.radio("1. Document Chain of Custody & Touchpoints:", ["**End-to-End Digital**: One centralized cloud file is updated securely by each stakeholder sequentially.", "**Multi-Hand Handling**: Paperwork is passed through multiple hands via email attachments, forcing manual file downloading or re-saving.", "**Fragmented/Siloed**: Every team creates independent versions of sheets and invoices; data is fragmented across disjointed systems."], key="p1_q_custody_radio")
        q_physical = st.radio("2. Reliance on Physical Assets & Stamps:", ["**100% Cloud/Digital**: Documents are securely archived in the cloud with no reliance on physical filing cabinets.", "**Hybrid/Paper-Reliant**: Files are regularly printed out, require physical signatures/wet ink stamps, and live in desk drawers.", "**High Vulnerability**: Intense reliance on physical photocopies. A localized climate hazard or office fire could destroy our proof of registration."], key="p1_q_physical_radio")
        q_rework = st.radio("3. Processing Typos, Mismatches, and Errors:", ["Our internal networks catch structural formatting mistakes instantly before documents are compiled or shared.", "Minor clerical typos (like mismatched IDs or container numbers) require manual email re-work loops and backtracking.", "Errors are usually discovered late at the port terminal, triggering immediate administrative panic and demurrage risk."], key="p1_q_rework_radio")

        st.subheader("🧮 Estimated Annual Financial Leakage Metrics")
        base_containers = float(annual_volume)
        incident_multiplier = 0.05
        if "Multi-Hand" in q_custody: incident_multiplier += 0.15
        if "Fragmented" in q_custody: incident_multiplier += 0.25
        if "Hybrid" in q_physical: incident_multiplier += 0.10
        if "High Vulnerability" in q_physical: incident_multiplier += 0.30
        if "manual email re-work" in q_rework: incident_multiplier += 0.20
        if "administrative panic" in q_rework: incident_multiplier += 0.40

        estimated_mishaps = max(1.0, base_containers * incident_multiplier)
        annual_rework_loss = estimated_mishaps * 150.00
        delay_days = 3.0 if ("High Vulnerability" in q_physical or "panic" in q_rework) else 1.5
        annual_port_loss = estimated_mishaps * (delay_days * 400.00)
        total_leakage = annual_rework_loss + annual_port_loss

        col_loss1, col_loss2 = st.columns(2)
        with col_loss1: st.metric("Annual Capital Lost to Administrative Re-Work", f"${annual_rework_loss:,.2f} USD", delta="Wasted Staff Hours", delta_color="inverse", key="p1_loss_metric1")
        with col_loss2: st.metric("Annual Port Delay & Storage Penalty Exposure", f"${annual_port_loss:,.2f} USD", delta="Demurrage Risk", delta_color="inverse", key="p1_loss_metric2")
        st.markdown(f"#### Total Estimated Cost of Paperwork Disjointedness: :red[**${total_leakage:,.2f} USD / Year**]")

# PANEL 2: THE COOPERATIVE ANCHOR WORKSPACE
elif current_role == "2. Cooperative Representative":
    st.title("🌾 Cooperative Control & Compliance Hub")
    st.info("Accountable Role: Validate legal land assets, manage quality logs, and publish premium lot lookbooks.")
    st.markdown(f"### **Current Shipment Stage Index: Step {st.session_state.current_step}**")
    
    tab_gate, tab_create = st.tabs(["1. Step 0: Legal Onboarding Gate", "2. Step 1: Lookbook Registry"])
    
    with tab_gate:
        st.write("Complete this gate to authorize your cooperative's crops for commercial export eligibility.")
        if st.session_state.current_step > 0:
            st.success("✅ **Step 0 Complete**: Your business tax framework and land deeds are fully validated.")
        else:
            with st.form("step0_gate_form"):
                tax_input = st.text_input("National Corporate/Cooperative Tax ID", value="CO-90088123-X", key="p2_tax_id_input")
                title_input = st.text_input("Government Land Deed Registry Serial Number", value="DEED-ANDES-4412", key="p2_land_deed_input")
                st.file_uploader("Upload Certified Land Title & GPS Coordinate Boundary Map File", type=["pdf"], key="p2_pdf_uploader")
                submit_0 = st.form_submit_button("Verify Identity & Authorize Lookbook Access")
                
                if submit_0:
                    if tax_input and title_input:
                        st.session_state.workflow_data["coop_tax_id"] = tax_input
                        st.session_state.workflow_data["land_title_num"] = title_input
                        st.session_state.current_step = 1
                        st.success("Identity Verified! Lookbook workspace unlocked.")
                        st.rerun()
                    else:
                        st.error("All legal data fields and land deeds must be supplied to pass.")

    with tab_create:
        if st.session_state.current_step < 1: st.warning("🔒 **Locked:** You must clear the Step 0 Legal Onboarding Gate before adding crop lots.")
        elif st.session_state.current_step > 1: st.success("✅ **Step 1 Complete**: This lot profile lookbook is locked and published to the active marketplace.")
        else:
            st.write("Build a transparent lot profile to catch the eye of global premium wholesale buyers.")
            with st.form("step1_lookbook_form"):
                moist_input = st.text_input("Measured Green Coffee Bean Moisture Content Log (%)", value="11.4%", key="p2_moisture_str_input")
                score_input = st.slider("Independent Cupping / Quality Score (Points)", 80.0, 100.0, 88.5, key="p2_cupping_score_slider")
                st.file_uploader("Upload Farm Marketing & Harvest Batch Photography", type=["jpg", "png"], key="p2_image_uploader")
                submit_1 = st.form_submit_button("🚀 Publish Lot to Global Buyer Marketplace")
                
                if submit_1:
                    st.session_state.workflow_data["lot_moisture"] = moist_input
                    st.session_state.workflow_data["cupping_score"] = score_input
                    st.session_state.current_step = 2
                    st.success("Lot profile successfully published online!")
                    st.rerun()

# PANEL 3: GLOBAL MARKETPLACE & ESCROW CONTRACTS
elif current_role == "3. Global Wholesale Buyer":
    st.title("☕ Global Green Coffee Lookbook Market")
    st.write("Browse transparent, identity-verified agricultural lots available for direct US importation.")
    
    if st.session_state.current_step < 2:
        st.warning("⏳ **Awaiting Inventory:** The Cooperative is currently compiling their legal validation gates. No lots are live yet.")
    elif st.session_state.current_step > 2:
        st.success("🎉 **Transaction Secured**: You have funded the escrow wallet for this shipment. Cargo is moving.")
    else:
        w = st.session_state.workflow_data
        st.markdown(f"### **Lot Profile: {w['coop_name']}**")
        c_m1, c_m2, c_m3 = st.columns(3)
        c_m1.metric("Sensory Quality Score", f"{w['cupping_score']} Points", key="p3_metric_cupping")
        c_m2.metric("Pre-Loading Moisture Log", w['lot_moisture'], key="p3_metric_moisture")
        c_m3.metric("Contract Value", "$85,000.00 USD", key="p3_metric_value")
        
        st.caption(f"🔒 **Legal Transparency Audit:** Registered Tax ID `{w['coop_tax_id']}` and Land Title `{w['land_title_num']}` verified at origin source.")
        st.warning("⚠️ **Contract Framework Alert:** IncoTerm: FOB (Free On Board). Legal liability shifts to buyer upon ship loading.")
        
        if st.button("🤝 Fund Escrow Wallet & Initialize Logistics Tracking Timeline", key="p3_fund_escrow_button"):
            st.session_state.workflow_data["escrow_funded"] = True
            st.session_state.current_step = 3
            st.success("Escrow secured! The commercial invoice has been compiled. The tracking timeline is active.")
            st.rerun()

# PANEL 4: BACKEND LOGISTICS & CUSTOMS BROKER WORKSPACE
elif current_role == "4. Logistics & Customs Broker":
    st.title("🚢 Supply Chain Logistics & Customs Integration Engine")
    w = st.session_state.workflow_data
    
    if st.session_state.current_step < 3: st.warning("⏳ **Awaiting Transaction:** This workspace unlocks sequentially once a buyer executes an escrow contract.")
    else:
        st.markdown("#### **📍 Live Operational Milestone Tracker**")
        st.write(f"Active Lifecycle Status Code: **Phase {st.session_state.current_step}**")
        
        # SYSTEM STEP 3 ACTION: LOCAL HEALTH CLEARANCE
        if st.session_state.current_step == 3:
            st.subheader("🔬 Phase 3: Phytosanitary Procurement Work Area")
            col_p_data, col_p_upload = st.columns(2)

---

### **Section 4: Universal Footers (Panels 5 & 6: Arbitrage, Exceptions, & Matrix)**
*Paste this as the final block at the absolute bottom of your file. This mounts your arbitrage engines, automated exceptions, document vaults, and the matrix checker universally underneath the workflow screens.*

```python
# ==============================================================================
# PART 4: UNIVERSALLY MOUNTED OPERATIONAL FOOTER WORKSPACES
# ==============================================================================
if current_role != "1. Discovery & Diagnostic Panel":
    # 📈 THE EXPANDED VALUATION PROTECTION FINANCIAL ENGINE
    st.divider()
    st.markdown("### 🏆 Premium Valuation & Market Arbitrage Engine")
    calc_col1, calc_col2 = st.columns(2)
    with calc_col1:
        st.markdown("##### 🎛️ Quality & Volume Variables")
        input_sca_score = st.slider("Verified Independent SCA Cup Score:", 75.0, 95.0, 84.5, step=0.5, key="premium_sca_slider")
        input_lot_bags = st.number_input("Isolated Residual Lot Volume (Standard 60KG Bags):", min_value=1, max_value=500, value=100, key="premium_volume_input")
        st.caption("Baseline Commodity Index Market Target Floor: **$2.25 / LB**")
    with calc_col2:
        st.markdown("##### 💰 Dynamic Revenue Capture Analytics")
        if st.session_state.current_step < 4:
            tier_status = "Awaiting Core Ingress Checks (Commodity Liquidation Default)"
            quality_premium = 0.00; penalty = 0.45
        else:
            penalty = 0.00
            tier_status = "Exotic Micro-Lot Portfolio (Premium Tier 1)" if input_sca_score >= 88.0 else "Fine Specialty Grade (Premium Tier 2)" if input_sca_score >= 85.0 else "Standard Specialty Grade (Premium Tier 3)"
            quality_premium = 3.75 if input_sca_score >= 88.0 else 1.95 if input_sca_score >= 85.0 else 0.60
        
        lbs = input_lot_bags * 132.277
        settlement_price = (2.25 + quality_premium) - penalty
        comm_val = lbs * (1.80 if st.session_state.current_step < 4 else 2.25)
        spec_val = lbs * settlement_price
        net_won = max(0.0, spec_val - comm_val)
        
        st.write(f"• **Assigned Market Sourcing Tier:** `{tier_status}`\n• **Final Settlement Price:** `${settlement_price:.2f} / LB` (Includes +${quality_premium:.2f} Premium)")
        v1, v2 = st.columns(2)
        v1.metric("Total Optimized Contract Value", f"${spec_val:,.2f}")
        v2.metric("Trapped Revenue Unlocked by Black Onyx", f"${net_won:,.2f}", delta=f"+{((net_won/comm_val)*100 if comm_val > 0 else 0):.1f}% Margin")

    # 🌧️ PANEL 5: CONTINGENCY ARBITRATOR & LIBRARY EXPANDERS
    st.divider()
    col_left_exceptions, col_right_library = st.columns(2)
    with col_left_exceptions:
        st.subheader("🚨 Ocean Transit Contingency Control")
        st.write("Simulate real-world supply chain exceptions to present your platform arbitration logic:")
        btn_c1, btn_c2, btn_c3 = st.columns(3)
        if btn_c1.button("🌧️ Weather / Storm at Sea", key="p5_storm_contingency_btn"): st.session_state.active_contingency = "Carrier Storm Delay"
        if btn_c2.button("🦠 Mold Found at Port", key="p5_mold_contingency_btn"): st.session_state.active_contingency = "Biological Failure"
        if btn_c3.button("☀️ Clean Voyage Tracker", key="p5_clean_contingency_btn"): st.session_state.active_contingency = "Clear Transit"
        
        st.markdown("##### **Automated Platform Referee Response:**")
        if st.session_state.active_contingency == "Carrier Storm Delay": st.warning("⚠️ **Schedule Disturbance Logged via Carrier Telemetry API**\n\n*Liability Ruling:* Under FOB terms, the Cooperative is not at fault. Escrow remains safely locked. Timeline adjustments automated.")
        elif st.session_state.active_contingency == "Biological Failure": st.error("❌ **Hygiene Failure Exception Tripped**\n\n*Liability Ruling:* Target moisture threshold breached. **Escrow Payout Suspended.** Funds queued for 100% buyer repayment loop.")
        else: st.success("🟢 **Telemetry Normal**\n\nContainer environment variables stable. Cargo routing smoothly.")

    with col_right_library:
        st.subheader("📂 Centralized Document Archive Vault")
        w_data = st.session_state.workflow_data
        with st.expander("📄 Step 0: Origin Legal Framework"): st.markdown(f"**Cooperative Tax Identifier:** `{w_data.get('coop_tax_id', 'Awaiting Upload')}`\n\n**Deed Reference ID:** `{w_data.get('land_title_num', 'Awaiting Onboarding')}`")
        with st.expander("🌾 Step 1: Crop Metric Logs"): st.markdown(f"**Pre-Loading Moisture Value:** `{w_data.get('lot_moisture', 'Awaiting Input')}`\n\n**Sensory Quality Score:** `{w_data.get('cupping_score', 0.0)} Points`")
        with st.expander("🔬 Step 3: Biosecurity Clearance"): st.markdown(f"**Phytosanitary Serial:** `{w_data.get('phyto_serial', 'Awaiting Exporter Action')}`")
        with st.expander("📋 Step 5: Border Documentation (CBP 3461)"): st.markdown(f"**Ocean Container Assignment ID:** `{w_data.get('container_num', 'Awaiting Loading')}`\n\n**ACE Transmit Status:** `{w_data.get('cbp_3461_status', 'Locked')}`")

    # 🏁 PANEL 6: INTERACTIVE COMPETITIVE MATRIX VIEWER
    st.divider(); st.markdown("## 🏁 The Sovereign Competitive Advantage")
    competitor_grid = {
        "Capability / Feature Milestone": ["🚜 Land Title Verification & GPS Mapping (Step 0)", "🌾 Crop Quality & Moisture Metrics Log (Step 1)", "☕ Visual Marketing Lookbook for Premium Buyers", "🔒 Secure Escrow Financial Checkout Backend", "🔬 Local Exporter Side-by-Side Data Pre-Fills", "🚢 Ocean Carrier Telemetry API Integration", "📋 Automated US Customs Entry Processing (CBP 3461)"],
        "Traditional Field Apps (AgUnity / TerraTrac / Mergdata)": ["✅ Yes (Excellent field tools)", "✅ Yes (Agronomy focus)", "❌ No (Strictly auditing tools)", "❌ No (No built-in payment rails)", "❌ No (Data trapped in silos)", "❌ No (Blind to ocean transit)", "❌ No (Manual email loops)"],
        "Our Sovereign Pipeline Engine": ["✅ Yes (Enformed Gatekeeper)", "✅ Yes (Bound to Lot Profile)", "🚀 Included (Drives New Sales)", "🚀 Included (Protects Capital)", "🚀 Included (Zero-Typo Workspaces)", "🚀 Included (Live Status Tracker)", "🏆 Included (One-Click Pre-Fill)"]
    }
    view_toggle = st.radio("Select Matrix Evaluation Scope:", ["Show Complete Ecosystem Grid", "Show Post-Farm Gate Gaps (Where Competitors Fail)"], key="p6_matrix_view_toggle_radio")
    if view_toggle == "Show Complete Ecosystem Grid": st.dataframe(pd.DataFrame(competitor_grid), use_container_width=True, hide_index=True)
    else:
        st.dataframe(pd.DataFrame(competitor_grid).iloc[2:], use_container_width=True, hide_index=True)
        st.warning("⚠️ **The Competitor Bottleneck:** Notice that traditional field apps stop entirely once the crop leaves the farm gate, dropping stakeholders back into the manual email mess.")

    # US CBP 3461 PASSPORT TEXT DATA EXPORT (PART 6 SUB-NODE)
    st.divider()
    st.markdown("### 🛂 Official Last-Mile Document Ingress Automation")
    st.info("🏢 Application Database Data Captured")
    st.markdown(f"- **Logged Entry ID:** `{active_coop.get('coop_id', 'COOP-LN01')}`\n- **Producer Business Entity:** `{active_coop.get('entity_name', w_data['coop_name'])}`\n- **Calculated Harmonized System Tariff Tag:** `HS Code 0901.11 (Green Coffee)`\n- **Active Biological Safety Pass Token:** `{active_coop.get('phytosanitary_inspection', 'Failed ❌')}`")
    
    if st.button("📥 Download Compiled CBP Form 3461 Text Passport Asset", key="p6_txt_passport_download_trigger_btn"):
        export_passport_payload = f"==================================================\nBLACK ONYX COMPLIANCE PASSPORT COOP ID: {active_coop.get('coop_id', 'COOP-LN01')}\n==================================================\n- Score: {st.session_state.current_step} / 6 Milestones Passed\n- Sourcing Risk Value Protected: ${total_exposure_mitigated:,.2f} USD\n- Trapped Revenue Unlocked     : ${net_arbitrage_capital_won:,.2f} USD\n=================================================="
        st.download_button(label="Click to save TXT Asset Payload", data=export_passport_payload, file_name=f"BlackOnyx_Compliance_Passport_{active_coop.get('coop_id', 'COOP-LN01')}.txt", mime="text/plain", key="bottom_download_passport_button_nested")

st.divider()
st.caption("🔒 Black Onyx Advisory Core Terminal. Protected under international trade database encryption protocols.")
