# ==============================================================================
# 💎 LAYER 1 VIEW ORCHESTRATOR: PORTAL CONTROL ROOM (SECTION 1 OF 3)
# ==============================================================================
# This module drives the user interface. It manages state memory, catches 
# webhook triggers, and pipes data payloads into the Layer 3 core math engine.
# ==============================================================================

import streamlit as st
import pandas as pd
import json
import uuid
import time

# Absolute path mapping imports from your independent repository modules
from core_engine import process_escrow_sop_pipeline, HS_ROUTING_MATRIX
from ai_extractor import extract_variables_from_pdf_binary, extract_variables_from_text_with_gemini

# Global Baseline HS Rule Book Layer Reference Configuration Mapping
HS_RULEBOOK = {
    "0901.11": {"commodity": "Coffee, Green / Not Roasted", "max_variance_pct": 2.0},
    "8802.40": {"commodity": "Civil Aircraft / Private Aviation Hull", "max_variance_pct": 0.5}
}

# --- PLATFORM STATE MACHINE & IN-APP STORAGE INITIALIZATION ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "trade_ledger" not in st.session_state:
    st.session_state.trade_ledger = [
        {
            "trade_id": "BOX-TX991",
            "timestamp": "2026-09-18 10:14:22",
            "buyer_name": "US Commodity Distribution LLC",
            "seller_name": "Global Coffee Traders Inc",
            "ein_number": "12-4455667",
            "vessel_imo": "IMO1234567",
            "hs_code": "0901.11",
            "value": 1250000.00,
            "escrow_status": "🟢 RELEASED / CLEARED",
            "risk_score": "LOW"
        },
        {
            "trade_id": "BOX-FL442",
            "timestamp": "2026-09-18 14:32:05",
            "buyer_name": "Euro-Grain Wholesale NV",
            "seller_name": "Shenzhen Tech Parts Ltd",
            "ein_number": "00-0000000",
            "vessel_imo": "IMO1234567",
            "hs_code": "8802.40",
            "value": 42000000.00,
            "escrow_status": "🚨 LOCKED / ARBITRATION",
            "risk_score": "HIGH"
        }
    ]

# --- STANDALONE SECURITY AUTHENTICATION GATEWAY (WITH BYPASS FOR DEMOS) ---
if not st.session_state.authenticated:
    st.set_page_config(page_title="Black Onyx Matrix — Authentication", layout="centered")
    st.title("⬛ Black Onyx Middleware Authentication")
    st.write("Access Restricted: This terminal requires a verified Private Lender security credential.")
    
    # CONVENTION DEMO QUICK BYPASS (One-click unlock for fast testing)
    st.info("💡 **Presentation Shortcut:** Check 'Enable Demo Mode' below to instantly unlock the platform dashboard without entering passwords.")
    demo_bypass = st.checkbox("⚡ Enable Convention Demo Mode / Quick Unlock", key="gate_demo_bypass_widget_id")
    
    if demo_bypass:
        st.session_state.authenticated = True
        st.success("Identity Authorized via Bypass. Mounting system cluster...")
        time.sleep(1)
        st.rerun()
        
    # Standard Manual Login Form Layout
    with st.form("lender_auth_gate"):
        username = st.text_input("Financier Login Identifier:", value="lender@blackonyx.com")
        password = st.text_input("Security Encryption Key:", value="blackonyx2026", type="password")
        submit_login = st.form_submit_button("Verify Identity & Unlock Middleware Core", use_container_width=True)
        
        if submit_login:
            if username == "lender@blackonyx.com" and password == "blackonyx2026":
                st.session_state.authenticated = True
                st.success("Identity Authenticated. Mounting system cluster...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Access Denied: Invalid security configuration strings or key signature.")
    st.stop()
# ==============================================================================
# 💎 LAYER 1 VIEW ORCHESTRATOR: PORTAL CONTROL ROOM (SECTION 2 OF 3)
# ==============================================================================
# Paste this block immediately below Section 1. It configures page styles,
# sidebar policy controls, and handles multi-channel transaction input fields.
# ==============================================================================

# Force clean, enterprise page state architecture
st.set_page_config(page_title="Black Onyx Matrix — Control Room", layout="wide", initial_sidebar_state="expanded")

# --- SIDEBAR CONTROL PANEL & LAYER 4 COUPLING ---
with st.sidebar:
    st.markdown("## ⚙️ Middleware Matrix")
    st.caption("Target Persona: Private Lender / Financier")
    st.success("Connected: Active Operational Node")
    
    if st.button("🔒 Log Out of Terminal", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()
        
    st.divider()
    st.markdown("### 🎛️ Policy Threshold Tuning")
    
    try:
        with open("policy.json", "r") as f:
            policy = json.load(f)
    except FileNotFoundError:
        policy = {"max_allowed_penalty_points": 35}
        
    # Fixed Explicit Key assigns a unique ID preventing duplication crashes
    max_penalty = st.slider(
        "Maximum Risk Point Threshold", 
        0, 100, 
        policy.get("max_allowed_penalty_points", 35),
        key="master_sidebar_policy_slider_element_id"
    )
    policy["max_allowed_penalty_points"] = max_penalty
    with open("policy.json", "w") as f:
        json.dump(policy, f, indent=2)

# --- 1. CROSS-BORDER RISK METRIC DISPLAYS ---
st.subheader("📊 Cross-Border Risk Analytics & Counterparty Exposure")
col_r1, col_r2, col_r3, col_r4 = st.columns(4)
with col_r1:
    st.metric(label="Global Active Capital Exposure", value="\$43.25M USD", delta="+\$2.1M This Week")
with col_r2:
    st.metric(label="Sovereign Risk Level (Origin Index)", value="Stable (Low)", delta="No Alerts")
with col_r3:
    st.metric(label="Counterparty LEI Match Accuracy", value="100.00%", delta="Verified via API")
with col_r4:
    st.metric(label="Active Escrow Violation Liquidity", value="\$12.50M USD", delta="-4.2% Risk Deflection", delta_color="inverse")

st.divider()

# --- 2. ACTIVE SYSTEM TELEMETRY DATA GRID ---
st.subheader("🚢 Active Trade Flow Pipeline & Ledger Records")
df_ledger = pd.DataFrame(st.session_state.trade_ledger)

st.dataframe(
    df_ledger,
    column_config={
        "trade_id": "Transaction Token Reference",
        "timestamp": "Audit Ingress Log Date",
        "buyer_name": "Buyer Corporate Name",
        "seller_name": "Seller Corporate Name",
        "ein_number": "Tax EIN Identification",
        "vessel_imo": "Nominated Vessel IMO",
        "hs_code": "Target HS Code",
        "value": st.column_config.NumberColumn("Contract Invoice Value", format="\$%,.2f"),
        "escrow_status": "Escrow Condition Status",
        "risk_score": "System Risk Rating"
    },
    use_container_width=True,
    hide_index=True
)

# --- 3. SECTION 2: AUTOMATED SELLER DROP BOX WORKFLOW ---
st.divider()
st.subheader("📩 Step 2: Automated Seller Ingestion Workflow")
st.write("Generate a secure, single-use workspace URL token to allow external counterparties to upload verification files password-free.")

col_gen_1, col_gen_2 = st.columns([1.2, 2])

with col_gen_1:
    st.markdown("#### **Generate Token Link**")
    target_trade_id = st.selectbox(
        "Select Active Transaction Reference:", 
        options=[t["trade_id"] for t in st.session_state.trade_ledger if "RELEASED" not in t["escrow_status"]],
        key="dropbox_target_selector_key"
    )
    
    if st.button("⚡ Generate One-Time Secure Token Link", use_container_width=True):
        unique_secure_token = f"TOKEN-{str(uuid.uuid4())[:8].upper()}"
        st.session_state.active_drop_token = unique_secure_token
        st.session_state.token_trade_target = target_trade_id
        st.session_state.token_used = False
        st.success("Token generated in platform cache memory!")

if "active_drop_token" in st.session_state and not st.session_state.token_used:
    with col_gen_2:
        st.markdown("#### **Generated Secure URL Manifest**")
        simulated_secure_url = f"https://blackonyx.app{st.session_state.active_drop_token}"
        st.info(f"📧 **Emailed Target Link Payload to Seller:**\n\n`{simulated_secure_url}`")
        
        st.caption("📱 Presentation Shortcut: Click to simulate the foreign exporter opening that secure web link:")
        if st.button("👉 Simulate Seller Clicking Email URL Link"):
            st.session_state.simulated_query_param = st.session_state.active_drop_token
            st.rerun()

# --- 4. SELLER DROPBOX EMBEDDED WORKSPACE OVERVOTE ---
if "simulated_query_param" in st.session_state and st.session_state.simulated_query_param != "":
    current_token = st.session_state.simulated_query_param
    
    if current_token == st.session_state.get("active_drop_token") and not st.session_state.get("token_used", False):
        st.empty() 
        st.markdown("---")
        st.title("📥 Secure Document Drop Box Terminal")
        st.write(f"Authorized Node Workspace Profile Link ID: `{current_token}`")
        st.warning("🔒 Confidential Gateway: No password required. This cryptographically verified token validates your entry identity.")

        with st.form("public_seller_drop_box_form"):
            uploaded_inspection_file = st.file_uploader("Select Certificate of Inspection (PDF/JSON Data Format)", type=["pdf", "json"])
            submit_upload = st.form_submit_button("Verify & Finalize Document Ingress", use_container_width=True)
            
            if submit_upload and uploaded_inspection_file is not None:
                st.session_state.token_used = True
                st.session_state.simulated_query_param = "" 
                
                for trade in st.session_state.trade_ledger:
                    if trade["trade_id"] == st.session_state.token_trade_target:
                        trade["escrow_status"] = "⏳ PENDING AUTOMATED CROSS-CHECK"
                st.balloons()
                st.success("Success! Document safely ingested into verification array.")
                time.sleep(2)
                st.rerun()
        st.stop()

# --- 5. SECTION 3: AUTOMATED DAY 0 CONTRACT PARAMETER INGESTION ---
st.divider()
st.subheader("🏢 Day 0 Initial Contract Ingestion Layer")
st.write("Bypass manual data entry. Initialize a trade contract parameter check to trigger automated background validation mappings.")

# Simulated External Global API Registry Map
LEI_GLOBAL_REGISTRY = {
    "US-COMMODITIES-99": {"lei_id": "LEI-US-992318451", "legal_name": "US Commodity Distribution LLC", "jurisdiction": "United States (Delaware)", "entity_status": "ACTIVE / VERIFIED", "credit_risk_rating": "AA+"},
    "EURO-GRAIN-88": {"lei_id": "LEI-EU-883471029", "legal_name": "Euro-Grain Wholesale NV", "jurisdiction": "Belgium (Brussels)", "entity_status": "ACTIVE / VERIFIED", "credit_risk_rating": "A-"}
}

col_ingest_1, col_ingest_2 = st.columns([1.2, 2])

with col_ingest_1:
    with st.form("day_0_ingestion_form"):
        buyer_node_key = st.selectbox("Select Target Importer Node:", options=list(LEI_GLOBAL_REGISTRY.keys()), format_func=lambda x: LEI_GLOBAL_REGISTRY[x]["legal_name"])
        seller_name_manual = st.text_input("Seller Corporate Name:", value="Global Coffee Traders Inc")
        seller_lei_manual = st.text_input("Seller Identity Identifier / Tax EIN:", value="12-4455667")
        vessel_manual = st.text_input("Nominated Shipping Vessel IMO:", value="IMO1234567")
        target_hs_code = st.selectbox("Target HS Commodity Code:", options=list(HS_RULEBOOK.keys()))
        invoice_value = st.number_input("Escrow Contract Value (\$ USD):", min_value=10000, value=500000)
        submit_ingestion = st.form_submit_button("🚀 Ingest Contract & Pull LEI Metrics", use_container_width=True)

if submit_ingestion:
    with col_ingest_2:
        st.markdown("#### **⚙️ Background API Telemetry Log**")
        with st.spinner("Pinging Global GLEIF API Database for corporate entity data..."):
            time.sleep(1)
            fetched_lei_profile = LEI_GLOBAL_REGISTRY[buyer_node_key]
            
        st.json({
            "API_Status": "200 OK",
            "Fetched_LEI_String": fetched_lei_profile["lei_id"],
            "GLEIF_Verification_Status": fetched_lei_profile["entity_status"],
            "Institutional_Credit_Rating": fetched_lei_profile["credit_risk_rating"]
        })
        
        new_trade_packet = {
            "trade_id": f"BOX-{str(uuid.uuid4())[:5].upper()}",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "buyer_name": fetched_lei_profile["legal_name"],
            "seller_name": seller_name_manual,
            "ein_number": seller_lei_manual,
            "vessel_imo": vessel_manual,
            "hs_code": target_hs_code,
            "contract_unit_price": 4.50,
            "value": float(invoice_value),
            "escrow_status": "⏳ AWAITING SELLER DROPBOX UPLOAD",
            "risk_score": "LOW" if fetched_lei_profile["credit_risk_rating"] == "AA+" else "MEDIUM"
        }
        st.session_state.trade_ledger.append(new_trade_packet)
        st.toast("New Contract Successfully Ingested!", icon="🏢")
        time.sleep(1)
        st.rerun()
# ==============================================================================
# 💎 LAYER 1 VIEW ORCHESTRATOR: PORTAL CONTROL ROOM (SECTION 3 OF 3)
# ==============================================================================
# Paste this final block at the absolute end of app.py. It connects logistics
# trackers and executes your automated Layer 3 multi-source audit matrices.
# ==============================================================================

# --- 6. SECTION 4: ASYNCHRONOUS MARITIME CARRIER WEBHOOKS ---
st.divider()
st.subheader("🚢 Automated Ocean Carrier API Webhook Gateway")
st.write("Simulate server-to-server middleware webhooks. This removes human data entry by tracking containers directly from carrier network telemetry feeds.")

CARRIER_WEBHOOK_SIMULATOR = {
    "BOX-TX991": {"container_id": "MSKU9918234", "carrier_scac": "MAEU (Maersk Line)", "vessel_name": "MAERSK MC-KINNEY MOLLER", "telemetry_status": "ARRIVED_AT_DESTINATION_PORT", "system_alert_flags": "NONE"},
    "BOX-FL442": {"container_id": "MSKU4421109", "carrier_scac": "MAEU (Maersk Line)", "vessel_name": "MAERSK ELEONORA", "telemetry_status": "EN_ROUTE_SEA_TRANSIT", "system_alert_flags": "BIOLOGICAL_HUMIDITY_ALERT"}
}

col_ship_1, col_ship_2 = st.columns([1.2, 2])

with col_ship_1:
    selected_tracking_id = st.selectbox(
        "Select Active Container Pipeline To Ping:", 
        options=[t["trade_id"] for t in st.session_state.trade_ledger], 
        key="carrier_api_select_box_unique_element_key"
    )
    trigger_webhook = st.button("📡 Ingest Automated Carrier Webhook Payload", use_container_width=True)

if trigger_webhook:
    with col_ship_2:
        st.markdown("#### **🛠️ Server-to-Server JSON Payload Parsing**")
        
        if selected_tracking_id in CARRIER_WEBHOOK_SIMULATOR:
            telemetry_payload = CARRIER_WEBHOOK_SIMULATOR[selected_tracking_id]
            time.sleep(0.5)
            
            st.code(f"// POST /api/v1/logistics/webhook HTTP/1.1\n// X-Carrier-Signature: verified_sha256\n\n{str(telemetry_payload).replace("'", '"')}", language="json")
            
            for trade in st.session_state.trade_ledger:
                if trade["trade_id"] == selected_tracking_id:
                    if telemetry_payload["system_alert_flags"] == "BIOLOGICAL_HUMIDITY_ALERT":
                        trade["escrow_status"] = "🚨 LOCKED / BIOLOGICAL ANOMALY DETECTED"
                        trade["vessel_imo"] = "IMO9999999" # Re-route to trigger sandbox dark fleet penalty
                        st.error(f"❌ **Risk Flag Raised:** Biological anomaly detected on Container {telemetry_payload['container_id']}. Escrow lock engaged automatically.")
                    else:
                        trade["escrow_status"] = "🚢 EN-ROUTE / TELEMETRY NORMAL"
                        st.success(f"✔️ **Transit Stream Normal:** Container {telemetry_payload['container_id']} is tracking cleanly inside operational parameters.")
            st.toast("Ledger state updated via Webhook!", icon="🚢")
            time.sleep(1)
            st.rerun()
        else:
            st.info("🔄 Initializing carrier channel matching for newly compiled record tokens...")
            for trade in st.session_state.trade_ledger:
                if trade["trade_id"] == selected_tracking_id:
                    trade["escrow_status"] = "🚢 EN-ROUTE / TELEMETRY NORMAL"
            st.success("New default carrier tracking stream established for this transaction token.")
            time.sleep(1)
            st.rerun()

# --- 7. SECTION 5: MASTER COMPLIANCE EVALUATION & PIPELINE COUPLING ---
st.divider()
st.subheader("🔍 Step 5: Master Middleware Evaluation Audit Panel")
st.write("This layer bridges your interactive frontend monitoring widgets with your Layer 3 Core Mathematical Matrix Engine.")

ingestion_vector = st.radio(
    "Choose Active Data Evaluation Source Material:", 
    ["1. Evaluate Active System Ledger Records (Sandbox Profiles)", "2. Ingest Custom Ad-Hoc Text Paragraph (Live Ingestion Mode Selection)"],
    horizontal=True,
    key="master_evaluation_source_material_radio_element"
)

active_extracted_payload = None

if "Ledger Records" in ingestion_vector:
    target_audit_id = st.selectbox("Select Target Ledger ID to Execute Audit Engine:", options=[t["trade_id"] for t in st.session_state.trade_ledger], key="final_audit_ledger_target_dropdown_box_key")
    active_extracted_payload = next(item for item in st.session_state.trade_ledger if item["trade_id"] == target_audit_id)
else:
    st.markdown("✍️ **Live Presentation Mode:** Ingest a custom text paragraph string to watch Gemini extract variables and execute your math rules live.")
    live_input_text = st.text_area(
        "⌨️ Interactive Raw Text Entry Window:",
        value="Draft Agreement: We intend to purchase freight units from Global Coffee Traders Inc (EIN: 12-4455667). Sourcing Importer: US Commodity Distribution LLC. Logistics route requires cargo transport liner ship IMO1234567. Goods metric: HS Code 0901.11. Total deal invoice valuation pricing rates evaluate to $500000.00",
        height=120
    )
    if st.button("🔮 Step 1: Trigger Live Gemini Text Extraction Layer", use_container_width=True):
        with st.spinner("🤖 Communicating with Google Gemini 1.5 Flash cloud instances..."):
            active_extracted_payload = extract_variables_from_text_with_gemini(live_input_text)
            st.session_state.ad_hoc_cache = active_extracted_payload

if "ad_hoc_cache" in st.session_state and "Live Ingestion" in ingestion_vector:
    active_extracted_payload = st.session_state.ad_hoc_cache

# --- FINALIZE LAYER 3 MATRIX EVALUATION EXECUTION ---
if active_extracted_payload:
    if st.button("🔥 Run Comprehensive Layer 3 Matrix Audit", use_container_width=True, key="trigger_master_layer3_matrix_audit_btn_element"):
        col_out_1, col_out_2 = st.columns(2)
        
        with col_out_1:
            st.write("### 🤖 Compliance Pipeline Ingestion Logs")
            
            # Map ledger variables smoothly to match your precise core_engine names
            remapped_payload = {
                "buyer_name": active_extracted_payload.get("buyer_name", "US Commodity Distribution LLC"),
                "seller_name": active_extracted_payload.get("seller_name", active_extracted_payload.get("vendor_name", "Global Coffee Traders Inc")),
                "ein_number": active_extracted_payload.get("ein_number", "12-4455667"),
                "vessel_imo": active_extracted_payload.get("vessel_imo", "IMO1234567"),
                "hs_code": "0901" if "0901" in str(active_extracted_payload.get("hs_code")) else "8542",
                "contract_unit_price": float(active_extracted_payload.get("contract_unit_price", 4.50)),
                "invoice_value": float(active_extracted_payload.get("invoice_value", active_extracted_payload.get("value", 500000.00)))
            }
            
            # Execute the unified chronological pipeline evaluation logic function
            verdict = process_escrow_sop_pipeline(remapped_payload)
            
            for log in verdict["logs"]:
                if "SOP" in log: st.info(log)
                elif "🛑" in log or "CRITICAL" in log: st.error(log)
                elif "⚠️" in log: st.warning(log)
                else: st.success(log)
                
        with col_out_2:
            st.write("### 🧮 Credit Underwriting Analytics")
            if verdict["status"] == "SUCCESS" and verdict["approved"]:
                uw = verdict["underwriting"]
                st.metric("Risk Assessment Tier", uw["risk_tier"])
                st.metric("Calculated Capital Outlay Limit", f"${uw['max_capital_outlay']:,.2f}", f"Advance Rate: {uw['advance_rate']*100}%")
                
                st.write("#### Required Funding Covenants:")
                for cov in uw["covenants"]:
                    st.markdown(cov)
                    
                st.markdown("---")
                st.caption("🔓 Manual Post-Disbursement Settlement Operations:")
                st.checkbox("🟩 SOP Step 5: Dual-Auth Four-Eyes Sign-off complete.", value=True, key="manual_sop_step_5_box")
                st.checkbox("⬜ SOP Step 6: Zero-Balancing Ledger Settlement complete.", value=False, key="manual_sop_step_6_box")
                st.checkbox("⬜ SOP Step 7: Immutable Archival Log locked (5-Year Retain).", value=False, key="manual_sop_step_7_box")
            else:
                st.error("🛑 UNDERWRITING UNAVAILABLE: Compliance firewall has suspended this transaction profile due to structural or legal safety failures.")
