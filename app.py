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
    FINAL_URL = "https://mdyoxirhdufdskytcmst.supabase.co"
    FINAL_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1keW94aXJoZHVmZHNreXRjbXN0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4NDUyMTk5NSwiZXhwIjoyMTAwMDk3OTk1fQ.d9AWBTABD4-gvKnFtGT5vNyd2uKJHvOSMeCPRRPXve8"

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

        # ==============================================================================
        # 🎯 PYTHON 3.14 HARDENED METRICS INTERFACE LAYER
        # ==============================================================================
        col_loss1, col_loss2 = st.columns(2)
        with col_loss1: 
            st.metric(
                label="Annual Capital Lost to Administrative Re-Work", 
                value=round(float(annual_rework_loss), 2),
                delta="Wasted Hours"
            )
        with col_loss2: 
            st.metric(
                label="Annual Port Delay & Storage Penalty Exposure", 
                value=round(float(annual_port_loss), 2),
                delta="Demurrage Risk"
            )


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


### **Section 4: Universal Footers (Panels 5 & 6: Arbitrage, Exceptions, & Matrix)**
### *Paste this as the final block at the absolute bottom of your file. This mounts your arbitrage engines, automated exceptions, document vaults, and the matrix checker universally underneath the workflow screens.* ###

# ==============================================================================
# 🚢 PANEL 4: LOGISTICS & CUSTOMS BROKER WORKSPACE
# ==============================================================================
elif current_role == "4. Logistics & Customs Broker":
    st.title("🚢 Supply Chain Logistics & Customs Integration Engine")
    w = st.session_state.workflow_data
    
    if st.session_state.current_step < 3:
        st.warning("⏳ **Awaiting Transaction:** This workspace unlocks sequentially once a buyer executes an escrow contract.")
    else:
        st.markdown("#### **📍 Live Operational Milestone Tracker**")
        st.write(f"Active Lifecycle Status Code: **Phase {st.session_state.current_step}**")
        
        # --- PHASE 3: BIOLOGICAL HEALTH CERTIFICATE INTAKE ---
        if st.session_step == 3:
            st.subheader("🔬 Phase 3: Phytosanitary Procurement Work Area")
            st.info("The app provides structured data panels below. Copy these parameters into your local Single Window portal.")
            
            col_p_data, col_p_upload = st.columns(2)
            with col_p_data:
                st.write(f"**Applicant Entity:** {w['coop_name']}")
                st.write(f"**Origin Land Deed Reference:** {active_coop.get('legal_gps_eudr')}")
                st.write(f"**Moisture Integrity Baseline:** {w['lot_moisture']}%")
            with col_p_upload:
                with st.form("step3_form_broker"):
                    p_serial = st.text_input("Official Phytosanitary Certificate String", value="PHYTO-CO-2026-991A")
                    st.file_uploader("Upload Government Issued Signed Certificate PDF", type=["pdf"])
                    submit_3 = st.form_submit_button("Verify Biological Health Certification")
                    if submit_3 and p_serial:
                        st.session_state.workflow_data["phyto_serial"] = p_serial
                        st.session_state.current_step = 4
                        st.success("Health logs saved. Moving to Carrier Gate-In Phase.")
                        st.rerun()

        # --- PHASE 4: PORT AND CARRIER ALLOCATION ---
        elif st.session_state.current_step == 4:
            st.subheader("⚓ Phase 4: Ocean Carrier Allocation")
            with st.form("step4_carrier_form"):
                container_input = st.text_input("Ocean Container Tracking ID (4 Letters + 7 Digits)", value="MSKU1192843")
                carrier_input = st.selectbox("Ocean Steamship Carrier SCAC Line:", ["MAEU (Maersk Line)", "MSCU (Mediterranean Shipping)", "CMAC (CMA CGM)"])
                bl_input = st.text_input("Bill of Lading (B/L) Reference ID", value="BL-Msk-883921")
                
                submit_4 = st.form_submit_button("Map Carrier API Telemetry")
                if submit_4 and container_input and bl_input:
                    st.session_state.workflow_data["container_num"] = container_input
                    st.session_state.workflow_data["carrier_scac"] = carrier_input
                    st.session_state.workflow_data["bill_of_lading"] = bl_input
                    st.session_state.current_step = 5
                    st.success("Carrier mapped successfully! Telemetry stream is active.")
                    st.rerun()

               # --- PHASE 5: US CUSTOMS AUTOMATED FORM 3461 payload ---
        elif st.session_state.current_step == 5:
            st.subheader("📋 Phase 5: US Customs Entry Processing Engine")
            st.write("Avoid manual data-entry fatigue. Extract verified historical stakeholder parameters with one-click.")
            
            if st.button("⚡ Fetch & Pre-fill CBP Form 3461 Schema", key="p4_fetch_3461_schema_btn"):
                st.session_state.workflow_data["cbp_3461_status"] = "Compiled via Platform API — Zero Typo Risk"
                st.success("Consolidated Step 0 Tax Framework, Step 1 Moisture Log, Step 3 Phyto Serial, and Step 4 Container ID.")
            
            st.write(f"CBP Form 3461 Status: **{w['cbp_3461_status']}**")
            
            # Initialize processing states safely in session memory
            if "pdf_generation_triggered" not in st.session_state:
                st.session_state.pdf_generation_triggered = False
            if "saved_entry_num" not in st.session_state:
                st.session_state.saved_entry_num = "123-4567890-1"

            # --- SUBMISSION INPUT FORM (STRICTLY DATA INPUT ONLY) ---
            with st.form("final_cbp_submission"):
                st.markdown("### **Review Auto-Populated Document Elements**")
                st.text_input("Block 9: Importer Number (Auto-Populated)", value="12-345678900", disabled=True)
                st.text_input("Block 14: Country of Origin (Auto-Populated)", value="CO", disabled=True)
                st.text_input("Block 12: Bill of Lading ID (Auto-Populated)", value=w.get("bill_of_lading", "BL-PENDING"), disabled=True)
                
                st.markdown("### **Broker Action Required: Entry Registration**")
                entry_num_input = st.text_input("Block 1: Entry Number String (Format: XXX-XXXXXXX-X)", value=st.session_state.saved_entry_num)
                
                submit_5 = st.form_submit_button("Transmit Document Payload to US CBP ACE Portal")
                
                if submit_5:
                    entry_pattern = r"^\d{3}-\d{7}-\d{1}$"
                    if not re.match(entry_pattern, entry_num_input):
                        st.error("❌ **Format Exception (Block 1):** Entry Number must follow the standard US Customs 11-digit hyphenated structure (e.g., 123-4567890-1).")
                        st.session_state.pdf_generation_triggered = False
                    else:
                        st.session_state.saved_entry_num = entry_num_input
                        st.session_state.workflow_data["entry_num"] = entry_num_input
                        st.session_state.pdf_generation_triggered = True

            # ==============================================================================
            # 🚏 SAFELY LIFTED OUTSIDE THE FORM: TRUE CBP FORM 3461 PDF ENGINE
            # ==============================================================================
            if st.session_state.pdf_generation_triggered:
                try:
                    pdf_reader = PdfReader("cbp_3461_blank.pdf")
                    pdf_writer = PdfWriter()
                    pdf_writer.append(pdf_reader)

                    pdf_form_payload = {
                        "topmostSubform.Page1.EntryNum": str(st.session_state.saved_entry_num),
                        "topmostSubform.Page1.EntryType": "01",
                        "topmostSubform.Page1.PortCode": "2704", 
                        "topmostSubform.Page1.ImporterNum": "12-345678900",
                        "topmostSubform.Page1.ImporterNameAddr": str(w.get('coop_name')),
                        "topmostSubform.Page1.Carrier": str(w.get('carrier_scac')),
                        "topmostSubform.Page1.BL_AWB": str(w.get('bill_of_lading')),
                        "topmostSubform.Page1.ContainerNum": str(w.get('container_num'))
                    }

                    pdf_writer.update_page_form_field_values(pdf_writer.pages, pdf_form_payload)

                    pdf_buffer = io.BytesIO()
                    pdf_writer.write(pdf_buffer)
                    pdf_buffer.seek(0)
                    final_pdf_bytes = pdf_buffer.getvalue()

                    st.success("🎉 Official US CBP Form 3461 Document Compiled Successfully!")
                    
                    col_preview, col_dl = st.columns([1.5, 1])
                    
                    with col_preview:
                        st.markdown("#### **📄 Live Border Document Preview**")
                        base64_pdf = base64.b64encode(final_pdf_bytes).decode('utf-8')
                        pdf_iframe_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" type="application/pdf"></iframe>'
                        st.markdown(pdf_iframe_display, unsafe_html=True)
                        
                    with col_dl:
                        st.markdown("#### **🛂 Legal Customs Asset Handshake**")
                        st.write("Save this verified, filled PDF to submit directly to port authorities or archive for auditing.")
                        
                        st.download_button(
                            label="⬇️ Download Official Filled CBP 3461 PDF",
                            data=final_pdf_bytes,
                            file_name=f"Official_CBP_3461_Entry_{st.session_state.saved_entry_num}.pdf",
                            mime="application/pdf",
                            key="true_government_pdf_download_button"
                        )
                        
                        if st.button("Proceed to Final Escrow Disbursement Milestone", key="move_to_step_6_final_action_btn"):
                            st.session_state.current_step = 6
                            st.session_state.pdf_generation_triggered = False 
                            st.rerun()

                except FileNotFoundError:
                    st.error("❌ **Critical Deployment Error:** The template file 'cbp_3461_blank.pdf' was not detected in your folder directory.")
                except Exception as e:
                    st.error(f"An unexpected document compiler error occurred: {e}")

            # ==============================================================================
            # 🌧️ INTEGRATED: PANEL 5 CONTINGENCY ARBITRATOR & COMPLETE VAULT LIST
            # ==============================================================================
            st.divider()
            col_left_exceptions, col_right_library = st.columns(2)

            with col_left_exceptions:
                st.subheader("🚨 Ocean Transit Contingency Control")
                st.write("Simulate real-world supply chain exceptions to present your platform arbitration logic:")
                
                btn_c1, btn_c2, btn_c3 = st.columns(3)
                if btn_c1.button("🌧️ Weather / Storm at Sea", key="p5_storm_contingency_btn"):
                    st.session_state.active_contingency = "Carrier Storm Delay"
                if btn_c2.button("🦠 Mold Found at Port", key="p5_mold_contingency_btn"):
                    st.session_state.active_contingency = "Biological Failure"
                if btn_c3.button("☀️ Clean Voyage Tracker", key="p5_clean_contingency_btn"):
                    st.session_state.active_contingency = "Clear Transit"
                    
                st.markdown("##### **Automated Platform Referee Response:**")
                if st.session_state.active_contingency == "Carrier Storm Delay":
                    st.warning("⚠️ **Schedule Disturbance Logged via Carrier Telemetry API**\n\n*Liability Ruling:* Under FOB terms, the Cooperative is not at fault. Escrow remains safely locked. Timeline adjustments automated.")
                elif st.session_state.active_contingency == "Biological Failure":
                    st.error("❌ **Hygiene Failure Exception Tripped**\n\n*Liability Ruling:* Target moisture threshold breached. **Escrow Payout Suspended.** Funds queued for 100% buyer repayment loop.")
                else:
                    st.success("🟢 **Telemetry Normal**\n\nContainer environment variables stable. Cargo routing smoothly.")

            with col_right_library:
                st.subheader("📂 Centralized Document Archive Vault")
                
                with st.expander("📄 Step 0: Origin Legal Framework"):
                    st.markdown(f"**Cooperative Tax Identifier:** `{w.get('coop_tax_id', 'Awaiting Upload')}`\n\n**Deed Reference ID:** `{active_coop.get('legal_gps_eudr', 'Awaiting Onboarding')}`")
                    
                with st.expander("🌾 Step 1: Crop Metric Logs"):
                    st.markdown(f"**Pre-Loading Moisture Value:** `{w.get('lot_moisture', 12.0)}%`\n\n**Sensory Quality Score:** `{w_data.get('cupping_score', 84.5)} Points`")
                    
                with st.expander("🔒 Step 2: Commercial Escrow Contract"):
                    escrow_condition = "🔒 Funds Fully Locked & Secured ($85,000.00)" if w.get("escrow_funded") else "⏳ Awaiting Buyer Escrow Funding Deposit"
                    st.markdown(f"**Transaction Settlement Condition:** `{escrow_condition}`")
                    st.markdown(f"**Governing Contract Trade Framework:** `Incoterm: FOB (Free On Board)`")
                    st.caption("💳 Financial Protection: Capital cannot clear to seller until all downstream border gates pass.")

                with st.expander("🔬 Step 3: Biosecurity Clearance"):
                    st.markdown(f"**Phytosanitary Serial:** `{w.get('phyto_serial', 'Awaiting Exporter Action')}`")
                    
                with st.expander("🚢 Step 4: Ocean Carrier Freight Manifest"):
                    st.markdown(f"**Assigned Ocean Container ID:** `{w.get('container_num', 'Awaiting Port Loading')}`")

        
        # --- PHASE 6: DISBURSEMENT SETTLEMENT ---
        elif st.session_state.current_step == 6:
            st.subheader("🎉 Phase 6: Smart Escrow Release & Settlement")
            st.balloons()
            st.success("🏆 Delivery Confirmed! The pipeline has completed with an unbroken data trail.")
            st.write("🟢 **$85,000.00 USD** transferred securely from Escrow directly to the Cooperative's banking profile.")
            
            if st.button("🔄 Reset Engine Pipeline for New Demo Session", key="p4_reset_pipeline_btn"):
                st.session_state.current_step = 0
                st.session_state.workflow_data = {
                    "coop_name": "Andean Coffee Co-Op", "coop_tax_id": "", "land_title_num": "", 
                    "lot_moisture": 12.0, "cupping_score": 84.5, "escrow_funded": False, "phyto_serial": "", 
                    "container_num": "", "carrier_scac": "", "bill_of_lading": "", "entry_num": "", "cbp_3461_status": "Locked"
                }
                st.rerun()

# ==============================================================================
# 🌧️ PANEL 5: CONTINGENCY ARBITRATOR & LIBRARY EXPANDERS
# ==============================================================================
# Only display this operational telemetry tracker if you are past the diagnostic onboarding view
if current_role != "1. Discovery & Diagnostic Panel":
    st.divider()
    col_left_exceptions, col_right_library = st.columns(2)

    with col_left_exceptions:
        st.subheader("🚨 Ocean Transit Contingency Control")
        st.write("Simulate real-world supply chain exceptions to present your platform arbitration logic:")
        
        btn_c1, btn_c2, btn_c3 = st.columns(3)
        if btn_c1.button("🌧️ Weather / Storm at Sea", key="p5_storm_contingency_btn"):
            st.session_state.active_contingency = "Carrier Storm Delay"
        if btn_c2.button("🦠 Mold Found at Port", key="p5_mold_contingency_btn"):
            st.session_state.active_contingency = "Biological Failure"
        if btn_c3.button("☀️ Clean Voyage Tracker", key="p5_clean_contingency_btn"):
            st.session_state.active_contingency = "Clear Transit"
            
        st.markdown("##### **Automated Platform Referee Response:**")
        if st.session_state.active_contingency == "Carrier Storm Delay":
            st.warning("⚠️ **Schedule Disturbance Logged via Carrier Telemetry API**\n\n*Liability Ruling:* Under FOB terms, the Cooperative is not at fault. Escrow remains safely locked. Timeline adjustments automated.")
        elif st.session_state.active_contingency == "Biological Failure":
            st.error("❌ **Hygiene Failure Exception Tripped**\n\n*Liability Ruling:* Target moisture threshold breached. **Escrow Payout Suspended.** Funds queued for 100% buyer repayment loop.")
        else:
            st.success("🟢 **Telemetry Normal**\n\nContainer environment variables stable. Cargo routing smoothly.")

    with col_right_library:
        st.subheader("📂 Centralized Document Archive Vault")
        w_data = st.session_state.workflow_data
        
        with st.expander("📄 Step 0: Origin Legal Framework"):
            st.markdown(f"**Cooperative Tax Identifier:** `{w_data.get('coop_tax_id', 'Awaiting Upload')}`\n\n**Deed Reference ID:** `{active_coop.get('legal_gps_eudr', 'Awaiting Onboarding')}`")
        with st.expander("🌾 Step 1: Crop Metric Logs"):
            st.markdown(f"**Pre-Loading Moisture Value:** `{w_data.get('lot_moisture', 12.0)}%`\n\n**Sensory Quality Score:** `{w_data.get('cupping_score', 0.0)} Points`")
        with st.expander("🔬 Step 3: Biosecurity Clearance"):
            st.markdown(f"**Phytosanitary Serial:** `{w_data.get('phyto_serial', 'Awaiting Exporter Action')}`")
        with st.expander("📋 Step 5: Border Documentation (CBP 3461)"):
            st.markdown(f"**Ocean Container Assignment ID:** `{w_data.get('container_num', 'Awaiting Loading')}`\n\n**ACE Transmit Status:** `{w_data.get('cbp_3461_status', 'Locked')}`")

# ==============================================================================
# 🏁 PANEL 6: INTERACTIVE COMPETITIVE MATRIX VIEWER & DATA PASSPORT EXPORT
# ==============================================================================
if current_role != "1. Discovery & Diagnostic Panel":
    st.divider()
    st.markdown("## 🏁 The Sovereign Competitive Advantage")

    competitor_grid = {
        "Capability / Feature Milestone": [
            "🚜 Land Title Verification & GPS Mapping (Step 0)", 
            "🌾 Crop Quality & Moisture Metrics Log (Step 1)", 
            "☕ Visual Marketing Lookbook for Premium Buyers", 
            "🔒 Secure Escrow Financial Checkout Backend", 
            "🔬 Local Exporter Side-by-Side Data Pre-Fills", 
            "🚢 Ocean Carrier Telemetry API Integration", 
            "📋 Automated US Customs Entry Processing (CBP 3461)"
        ],
        "Traditional Field Apps (AgUnity / TerraTrac / Mergdata)": [
            "✅ Yes (Excellent field tools)", 
            "✅ Yes (Agronomy focus)", 
            "❌ No (Strictly auditing tools)", 
            "❌ No (No built-in payment rails)", 
            "❌ No (Data trapped in silos)", 
            "❌ No (Blind to ocean transit)", 
            "❌ No (Manual email loops)"
        ],
        "Our Sovereign Pipeline Engine": [
            "✅ Yes (Enformed Gatekeeper)", 
            "✅ Yes (Bound to Lot Profile)", 
            "🚀 Included (Drives New Sales)", 
            "🚀 Included (Protects Capital)", 
            "🚀 Included (Zero-Typo Workspaces)", 
            "🚀 Included (Live Status Tracker)", 
            "🏆 Included (One-Click Pre-Fill)"
        ]
    }

    view_toggle = st.radio(
        "Select Matrix Evaluation Scope:", 
        ["Show Complete Ecosystem Grid", "Show Post-Farm Gate Gaps (Where Competitors Fail)"], 
        key="p6_matrix_view_toggle_radio"
    )

    if view_toggle == "Show Complete Ecosystem Grid":
        st.dataframe(pd.DataFrame(competitor_grid), use_container_width=True, hide_index=True)
    else:
        st.dataframe(pd.DataFrame(competitor_grid).iloc[2:], use_container_width=True, hide_index=True)
        st.warning("⚠️ **The Competitor Bottleneck:** Notice that traditional field apps stop entirely once the crop leaves the farm gate, dropping stakeholders back into the manual email mess.")

    # --- PART 6 SUB-NODE: LAST-MILE PASSPORT TEXT DATA EXPORT ---
    st.divider()
    st.markdown("### ### 🛂 Official Last-Mile Document Ingress Automation")
    st.info("🏢 Application Database Data Captured")

    # Safely unpack session variables or handle default calculations for fallback scenarios
    val_protected = st.session_state.get("total_exposure_mitigated", 4200.00)
    rev_unlocked = st.session_state.get("net_arbitrage_capital_won", 12500.00)

    st.markdown(f"""
    - **Logged Entry ID:** `{active_coop.get('coop_id', 'COOP-LN01')}`
    - **Producer Business Entity:** `{active_coop.get('entity_name', w_data['coop_name'])}`
    - **Calculated Harmonized System Tariff Tag:** `HS Code 0901.11 (Green Coffee)`
    - **Active Biological Safety Pass Token:** `{active_coop.get('phytosanitary_inspection', 'Failed ❌')}`
    """)

    # Pre-compile text string block data payload
    export_passport_payload = f"""==================================================
    BLACK ONYX COMPLIANCE PASSPORT COOP ID: {active_coop.get('coop_id', 'COOP-LN01')}
    ==================================================
    - Score: {st.session_state.current_step} / 6 Milestones Passed
    - Sourcing Risk Value Protected: ${val_protected:,.2f} USD
    - Trapped Revenue Unlocked : ${rev_unlocked:,.2f} USD
    =================================================="""

    # Clean single-click downloader execution (Fixed your nested button runtime crash bug)
    st.download_button(
        label="📥 Download Compiled CBP Form 3461 Text Passport Asset", 
        data=export_passport_payload, 
        file_name=f"BlackOnyx_Compliance_Passport_{active_coop.get('coop_id', 'COOP-LN01')}.txt", 
        mime="text/plain", 
        key="bottom_download_passport_button_clean_execution"
    )

    st.divider()
    st.caption("🔒 Black Onyx Advisory Core Terminal. Protected under international trade database encryption protocols.")




