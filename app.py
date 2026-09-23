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
from core_engine import process_escrow_sop_pipeline, REGULATORY_MASTER_MAP

# Global Baseline HS Rule Book Layer Reference Configuration Mapping
HS_RULEBOOK = {
    "0901.11": {"commodity": "Coffee, Green / Not Roasted", "max_variance_pct": 2.0},
    "8542.40": {"commodity": "Electronic Integrated Circuits / Semiconductors", "max_variance_pct": 1.5},
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
            "buyer_lei": "LEI-US-550912834",
            "seller_lei": "LEI-CO-110293847",
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
            "buyer_lei": "LEI-US-992318451",
            "seller_lei": "LEI-TH-883210943",
            "ein_number": "00-0000000",
            "vessel_imo": "IMO1234567",
            "hs_code": "8542.40",
            "value": 42000000.00,
            "escrow_status": "🚨 LOCKED / ARBITRATION",
            "risk_score": "HIGH"
        }
    ]

# --- STANDALONE SECURITY AUTHENTICATION GATEWAY (WITH BYPASS FOR DEMOS) ---
if not st.session_state.authenticated:
    st.set_page_config(page_title="Black Onyx Matrix — Authentication", layout="centered")
    st.markdown("<h2 style='text-align: center;'>⬛ Black Onyx Fiduciary Portal</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # CONVENTION DEMO QUICK BYPASS (One-click unlock for fast testing)
    st.info("💡 **Presentation Shortcut:** Check 'Enable Demo Mode' below to instantly unlock the platform dashboard without entering passwords.")
    demo_bypass = st.checkbox("⚡ Enable Convention Demo Mode / Quick Unlock", key="gate_demo_bypass_widget_id")
    
    if demo_bypass:
        st.session_state.authenticated = True
        st.success("Identity Authorized via Bypass. Mounting system cluster...")
        time.sleep(0.5)
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
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Access Denied: Invalid security configuration strings or key signature.")
    st.stop()
# ==============================================================================
# 💎 LAYER 1 VIEW ORCHESTRATOR: PORTAL CONTROL ROOM (SECTION 2 OF 3)
# ==============================================================================
# Paste this block immediately below Section 1. It configures layouts,
# sidebar profile inputs, and maps the active ledger telemetry tracking data.
# ==============================================================================

# Force clean, enterprise page state architecture
st.set_page_config(page_title="Black Onyx Matrix — Control Room", layout="wide", initial_sidebar_state="expanded")

# --- SIDEBAR IDENTITY BRANDING & COMPLIANCE MATRIX ADJUSTER ---
with st.sidebar:
    st.markdown("## ⚙️ Middleware Matrix")
    st.caption("Target Persona: Private Lender / Escrow Agent")
    st.divider()
    st.markdown("### 🚦 Operator Identity Profile")
    st.success("Connected: Active Node Session")
    st.info("Role: Primary Funding Referee")
    
    if st.button("🔒 Log Out of Terminal", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()
        
    st.divider()
    
    # LAYER 4 AGNOSTIC INGESTION: DYNAMIC CLIENT POLICY PROFILE FILE UPLOADER
    st.markdown("### 📥 Load Agnostic Client Profile")
    uploaded_policy_file = st.file_uploader("Upload Corporate Policy Profile (JSON)", type=["json"], key="agnostic_policy_uploader_element_key")
    if uploaded_policy_file is not None:
        try:
            custom_policy_data = json.load(uploaded_policy_file)
            with open("policy.json", "w") as f: json.dump(custom_policy_data, f, indent=2)
            st.sidebar.success(f"✔️ Connected to Profile: {custom_policy_data['client_metadata']['client_id']}")
        except Exception as e:
            st.sidebar.error(f"Invalid Format: {str(e)}")
            
    st.divider()
    st.markdown("### 🎛️ Policy Gate Configuration Overrides")
    try:
        with open("policy.json", "r") as f: policy_config = json.load(f)
    except FileNotFoundError:
        policy_config = {"max_allowed_penalty_points": 35}
        
    # This single slider handles your active risk ceiling threshold with a strict explicit key tracking system
    max_penalty_limit = st.sidebar.slider(
        "Maximum Risk Point Threshold", 
        0, 100, 
        policy_config.get("max_allowed_penalty_points", 35),
        key="master_compliance_gate_slider_key"
    )
    policy_config["max_allowed_penalty_points"] = max_penalty_limit
    with open("policy.json", "w") as f: json.dump(policy_config, f, indent=2)

# --- 1. CORE DASHBOARD CONTROL ROOM (THE MAIN UI PANEL) ---
st.title("💎 Core Dashboard Control Room")
st.write("Alternative Credit & Escrow Funds Transaction Telemetry Terminal.")

# --- 2. CROSS-BORDER RISK METRIC DISPLAYS ---
st.subheader("📊 Cross-Border Risk Analytics & Counterparty Exposure")
col_r1, col_r2, col_r3, col_r4 = st.columns(4)
with col_r1: st.metric(label="Global Active Capital Exposure", value=r"\$43.25M USD", delta=r"+\$2.1M This Week")
with col_r2: st.metric(label="Sovereign Risk Level (Origin Index)", value="Stable (Low)", delta="No Alerts")
with col_r3: st.metric(label="Counterparty LEI Match Accuracy", value="100.00%", delta="Verified via API")
with col_r4: st.metric(label="Active Escrow Violation Liquidity", value=r"\$12.50M USD", delta="-4.2% Risk Deflection", delta_color="inverse")

st.divider()

# --- 3. ACTIVE SYSTEM TELEMETRY DATA GRID ---
st.subheader("🚢 Active Trade Flow Pipeline & Ledger Records")
df_ledger = pd.DataFrame(st.session_state.trade_ledger)

st.dataframe(
    df_ledger,
    column_config={
        "trade_id": "Transaction Token Reference",
        "timestamp": "Audit Ingress Log Date",
        "buyer_lei": "Buyer Corporate LEI",
        "seller_lei": "Seller Corporate LEI",
        "hs_code": "Target HS Code",
        "value": st.column_config.NumberColumn("Contract Invoice Value", format=r"\$%,.2f"),
        "escrow_status": "Escrow Condition Status",
        "risk_score": "System Risk Rating"
    },
    width="stretch",
    hide_index=True
)

# --- 4. SECTION 2: THE INGESTION LAYER & ZERO-LOGIN DROP BOX GENERATOR ---
st.divider()
st.subheader("📩 Step 2: Automated Seller Ingestion Workflow")
st.write("Generate a secure, single-use workspace URL token to allow external counterparties to upload verification files.")

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
        simulated_secure_url = f"https://streamlit.io{st.session_state.active_drop_token}"
        st.info(f"📧 **Emailed Target Link Payload to Seller:**\n\n`{simulated_secure_url}`")
        
        st.write("---")
        st.caption("📱 Presentation Shortcut: Click to simulate the Seller opening that email link:")
        if st.button("👉 Simulate Seller Clicking Email URL Link"):
            st.session_state.simulated_query_param = st.session_state.active_drop_token
            st.rerun()

# --- 5. BARE UN-AUTHENTICATED SELLER DROP BOX INTERFACE OVERLAY ---
if "simulated_query_param" in st.session_state and st.session_state.simulated_query_param != "":
    current_token = st.session_state.simulated_query_param
    
    if current_token == st.session_state.get("active_drop_token") and not st.session_state.get("token_used", False):
        st.empty() 
        st.markdown("---")
        st.title("📥 Secure Document Drop Box Terminal")
        st.write(f"Authorized Node Workspace Profile Link ID: `{current_token}`")
        st.caption(f"Linked Transaction Reference: **{st.session_state.token_trade_target}**")
        st.warning("🔒 Confidential: You do not need a password. This secure file gateway authorizes your upload directly.")

        with st.form("public_seller_drop_box_form"):
            st.markdown("### **📤 Ingest Official Verification Assets**")
            st.write("Please drop your official third-party Certificate of Inspection PDF file below to update the lender:")
            uploaded_inspection_file = st.file_uploader("Select Certificate of Inspection (PDF/JSON Data Format)", type=["pdf", "json"])
            submit_upload = st.form_submit_button("Verify & Finalize Document Ingress", use_container_width=True)
            
            if submit_upload and uploaded_inspection_file is not None:
                st.session_state.token_used = True
                st.session_state.simulated_query_param = "" 
                
                for trade in st.session_state.trade_ledger:
                    if trade["trade_id"] == st.session_state.token_trade_target:
                        trade["escrow_status"] = " PENDING AUTOMATED CROSS-CHECK"
                st.balloons()
                st.success("🎉 Success! Your Certificate of Inspection has been securely ingested into the platform's verification array.")
                time.sleep(2)
                st.rerun()
        st.stop()
# ==============================================================================
# 💎 LAYER 1 VIEW ORCHESTRATOR: PORTAL CONTROL ROOM (SECTION 3 OF 3)
# ==============================================================================
# Paste this final block at the absolute end of app.py. It connects logistics
# trackers and executes your automated Layer 3 multi-source audit matrices.
# ==============================================================================

# --- 6. SECTION 3: AUTOMATED INGESTION LAYER (THE BUYER LAYER) ---
st.divider()
st.subheader("🏢 Section 3: Day 0 Automated Parameter Ingestion")
st.write("Bypass manual counterparty data entry. Initialize a trade contract parameter check to trigger automated background LEI validation.")

LEI_GLOBAL_REGISTRY = {
    "US-COMMODITIES-99": {"lei_id": "LEI-US-992318451", "legal_name": "US Commodity Distribution LLC", "jurisdiction": "United States (Delaware)", "entity_status": "ACTIVE / VERIFIED", "credit_risk_rating": "AA+"},
    "EURO-GRAIN-88": {"lei_id": "LEI-EU-883471029", "legal_name": "Euro-Grain Wholesale NV", "jurisdiction": "Belgium (Brussels)", "entity_status": "ACTIVE / VERIFIED", "credit_risk_rating": "A-"}
}

col_ingest_1, col_ingest_2 = st.columns([1.2, 2])

with col_ingest_1:
    st.markdown("#### **Day 0 Parameter Ingestion**")
    with st.form("day_0_ingestion_form"):
        buyer_node_key = st.selectbox("Select Target Importer Node:", options=list(LEI_GLOBAL_REGISTRY.keys()), format_func=lambda x: LEI_GLOBAL_REGISTRY[x]["legal_name"])
        seller_lei_manual = st.text_input("Seller Identity Identifier / LEI:", value="LEI-CO-110293847")
        target_hs_code = st.selectbox("Target HS Commodity Code:", options=list(HS_RULEBOOK.keys()))
        invoice_value = st.number_input(r"Escrow Contract Value ($ USD):", min_value=10000, value=500000)
        submit_ingestion = st.form_submit_button("🚀 Ingest Contract & Pull LEI Metrics", use_container_width=True)

if submit_ingestion:
    with col_ingest_2:
        st.markdown("#### **⚙️ Background API Telemetry Log**")
        with st.spinner("Pinging Global GLEIF API Database for corporate entity telemetry..."):
            time.sleep(1)
            fetched_lei_profile = LEI_GLOBAL_REGISTRY[buyer_node_key]
            
        st.success(f" Background Handshake Success! Fetched Profile for {fetched_lei_profile['legal_name']}")
        st.json({
            "API_Status": "200 OK",
            "Fetched_LEI_String": fetched_lei_profile["lei_id"],
            "Corporate_Jurisdiction": fetched_lei_profile["jurisdiction"],
            "GLEIF_Verification_Status": fetched_lei_profile["entity_status"],
            "Institutional_Credit_Rating": fetched_lei_profile["credit_risk_rating"]
        })
        
        new_trade_packet = {
            "trade_id": f"BOX-{str(uuid.uuid4())[:5].upper()}",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "buyer_lei": fetched_lei_profile["lei_id"],
            "seller_lei": seller_lei_manual,
            "hs_code": target_hs_code,
            "value": float(invoice_value),
            "escrow_status": " AWAITING SELLER DROPBOX UPLOAD",
            "risk_score": "LOW" if fetched_lei_profile["credit_risk_rating"] == "AA+" else "MEDIUM"
        }
        st.session_state.trade_ledger.append(new_trade_packet)
        st.toast("New Contract Successfully Ingested with LEI Mapping!", icon="🏢")
        time.sleep(1)
        st.rerun()

# --- 7. SECTION 4: OCEAN CARRIER API INTEGRATION (THE LOGISTICS LAYER) ---
st.divider()
st.subheader("🚢 Section 4: Automated Ocean Carrier API Webhook Gateway")
st.write("Simulate server-to-server middleware webhooks. This removes human broker entry by tracking containers directly from carrier networks.")

CARRIER_WEBHOOK_SIMULATOR = {
    "BOX-TX991": {"container_id": "MSKU9918234", "carrier_scac": "MAEU (Maersk Line)", "vessel_name": "MAERSK MC-KINNEY MOLLER", "telemetry_status": "ARRIVED_AT_DESTINATION_PORT", "container_temp_c": 19.5, "gps_coordinates": "40.6892, -74.0445", "system_alert_flags": "NONE"},
    "BOX-FL442": {"container_id": "MSKU4421109", "carrier_scac": "MAEU (Maersk Line)", "vessel_name": "MAERSK ELEONORA", "telemetry_status": "EN_ROUTE_SEA_TRANSIT", "container_temp_c": 28.2, "gps_coordinates": "24.8607, 67.0011", "system_alert_flags": "BIOLOGICAL_HUMIDITY_ALERT"}
}

col_ship_1, col_ship_2 = st.columns([1.2, 2])

with col_ship_1:
    st.markdown("#### **Simulate Webhook Trigger**")
    selected_tracking_id = st.selectbox("Select Target Container Pipeline To Ping:", options=[t["trade_id"] for t in st.session_state.trade_ledger], key="carrier_api_select_box")
    trigger_webhook = st.button(" Ingest Automated Carrier Webhook Payload", use_container_width=True)

if trigger_webhook:
    with col_ship_2:
        st.markdown("#### **🛠️ Server-to-Server JSON Payload Parsing**")
        if selected_tracking_id in CARRIER_WEBHOOK_SIMULATOR:
            telemetry_payload = CARRIER_WEBHOOK_SIMULATOR[selected_tracking_id]
            with st.spinner("Parsing asynchronous webhook data stream..."): time.sleep(0.5)
                
            st.code(f"// POST /api/v1/logistics/webhook HTTP/1.1\n// Host: ://blackonyx.com\n// X-Carrier-Signature: sha256_verified\n\n{str(telemetry_payload).replace("'", '"')}", language="json")
            
            for trade in st.session_state.trade_ledger:
                if trade["trade_id"] == selected_tracking_id:
                    if telemetry_payload["system_alert_flags"] == "BIOLOGICAL_HUMIDITY_ALERT":
                        trade["escrow_status"] = "🚨 LOCKED / BIOLOGICAL ANOMALY DETECTED"
                        trade["vessel_imo"] = "IMO9999999" # Map to trigger Layer 3 dark fleet penalties
                        st.error(f"❌ **Risk Flag Raised:** Biological anomaly detected on Container {telemetry_payload['container_id']}. Escrow lock engaged automatically.")
                    else:
                        trade["escrow_status"] = "🚢 EN-ROUTE / TELEMETRY NORMAL"
                        st.success(f"✔️ **Transit Stream Normal:** Container {telemetry_payload['container_id']} tracks inside parameters.")
            st.toast("Trade state updated via Carrier Webhook!", icon="🚢")
            time.sleep(1)
            st.rerun()
        else:
            st.info("🔄 Initializing carrier channel matching for newly compiled entry records...")
            for trade in st.session_state.trade_ledger:
                if trade["trade_id"] == selected_tracking_id:
                    trade["escrow_status"] = "🚢 EN-ROUTE / TELEMETRY NORMAL"
            st.success("New default carrier tracking stream established.")
            time.sleep(1)
            st.rerun()

# --- 8. SECTION 5: DISBURSEMENT WATERFALL RECONCILIATION COUPLING GATEWAY ---
st.divider()
st.subheader("⚖️ Step 5: Master Compliance & Financial Payout Waterfall")

ingestion_vector = st.radio("Choose Ingestion Input Processing Vector:", ["Use Sandbox Scenario Profiles (Instant Demo)", "Custom Ad-hoc Input Text Area (Live Ingestion Mode)"], horizontal=True, key="master_eval_ingest_radio")
active_extracted_payload = None

if "Profiles" in ingestion_vector:
    profile = st.selectbox("Select a Target Pre-Shipment Escrow Transaction File Profile:", ["Select a folder profile...", "Folder Profile 01: Standard Arabica Coffee Trade - Clear Compliance Pass", "Folder Profile 02: Dual-Use Transit Freight - Suspicious Corporate Identity Track", "Folder Profile 03: Heavy Sourcing Sacks Route - Logistics Variance Route Track"])
    if "Coffee" in profile:
        active_extracted_payload = {"buyer_lei": "LEI-US-550912834", "seller_lei": "LEI-CO-110293847", "ein_number": "12-4455667", "vessel_imo": "IMO1234567", "hs_code": "0901.11", "value": 1250000.00}
    elif "Dual-Use" in profile:
        active_extracted_payload = {"buyer_lei": "LEI-US-550912834", "seller_lei": "LEI-TH-883210943", "ein_number": "00-0000000", "vessel_imo": "IMO1234567", "hs_code": "8542.40", "value": 42000000.00}
    elif "Heavy Sourcing" in profile:
        active_extracted_payload = {"buyer_lei": "LEI-US-992318451", "seller_lei": "LEI-TH-883210943", "ein_number": "99-9999999", "vessel_imo": "IMO9999999", "hs_code": "8542.40", "value": 500000.00}
else:
    live_input_text = st.text_area("Interactive Ad-hoc Text Entry Window:", value="Draft: Buyer LEI-US-550912834, Seller LEI-CO-110293847, EIN: 12-4455667, Vessel IMO1234567, HS Code: 0901.11, Value: 500000")
    if st.button("🔮 Step 1: Trigger Live Gemini Text Extraction Layer"):
        with st.spinner("🤖 Requesting Gemini..."):
            active_extracted_payload = extract_variables_from_text_with_gemini(live_input_text)
            st.session_state.ad_hoc_cache = active_extracted_payload

if "ad_hoc_cache" in st.session_state and "Custom Ad-hoc" in ingestion_vector:
    active_extracted_payload = st.session_state.ad_hoc_cache

if active_extracted_payload:
    if st.button("🔥 Run Comprehensive Layer 3 Matrix Audit", width="stretch", key="run_sop_master_audit_btn"):
        c1, c2 = st.columns(2)
        with c1:
            st.write("### 🤖 Compliance Pipeline Ingestion Logs")
            
            # Pipe compiled payload dictionary variables directly into Layer 3
            verdict = process_escrow_sop_pipeline(active_extracted_payload, matrix_selection)
            for log in verdict["logs"]:
                if "SOP" in log or "ASSESSOR" in log: st.info(log)
                elif "🛑" in log or "CRITICAL" in log: st.error(log)
                elif "⚠️" in log: st.warning(log)
                else: st.success(log)
        with c2:
            st.write("### 🧮 Cash Distribution Settlement Matrix")
            w = verdict["waterfall"]
            if verdict["approved"]:
                st.success("🎉 FIDUCIARY CLEARANCE GRANTED: ACCOUNT SAFE TO RECONCILE")
                if "Scenario A" in matrix_selection:
# ==============================================================================
# 💎 LAYER 1 VIEW ORCHESTRATOR: PORTAL CONTROL ROOM (SECTION 3 OF 3)
# ==============================================================================
# Paste this final block at the absolute end of app.py. It connects logistics
# trackers and executes your automated Layer 3 multi-source audit matrices.
# ==============================================================================

# --- 6. SECTION 3: AUTOMATED INGESTION LAYER (THE BUYER LAYER) ---
st.divider()
st.subheader("🏢 Section 3: Day 0 Automated Parameter Ingestion")
st.write("Bypass manual counterparty data entry. Initialize a trade contract parameter check to trigger automated background LEI validation.")

LEI_GLOBAL_REGISTRY = {
    "US-COMMODITIES-99": {
        "lei_id": "LEI-US-992318451", 
        "legal_name": "US Commodity Distribution LLC", 
        "jurisdiction": "United States (Delaware)", 
        "entity_status": "ACTIVE / VERIFIED", 
        "credit_risk_rating": "AA+"
    },
    "EURO-GRAIN-88": {
        "lei_id": "LEI-EU-883471029", 
        "legal_name": "Euro-Grain Wholesale NV", 
        "jurisdiction": "Belgium (Brussels)", 
        "entity_status": "ACTIVE / VERIFIED", 
        "credit_risk_rating": "A-"
    }
}

col_ingest_1, col_ingest_2 = st.columns([1.2, 2])

with col_ingest_1:
    st.markdown("#### **Day 0 Parameter Ingestion**")
    with st.form("day_0_ingestion_form"):
        buyer_node_key = st.selectbox(
            "Select Target Importer Node:", 
            options=list(LEI_GLOBAL_REGISTRY.keys()), 
            format_func=lambda x: LEI_GLOBAL_REGISTRY[x]["legal_name"]
        )
        seller_lei_manual = st.text_input("Seller Identity Identifier / LEI:", value="LEI-CO-110293847")
        target_hs_code = st.selectbox("Target HS Commodity Code:", options=list(HS_RULEBOOK.keys()))
        invoice_value = st.number_input(r"Escrow Contract Value ($ USD):", min_value=10000, value=500000)
        submit_ingestion = st.form_submit_button("🚀 Ingest Contract & Pull LEI Metrics", use_container_width=True)

if submit_ingestion:
    with col_ingest_2:
        st.markdown("#### **⚙️ Background API Telemetry Log**")
        with st.spinner("Pinging Global GLEIF API Database for corporate entity telemetry..."):
            time.sleep(1)
            fetched_lei_profile = LEI_GLOBAL_REGISTRY[buyer_node_key]
            
        st.success(f" Background Handshake Success! Fetched Profile for {fetched_lei_profile['legal_name']}")
        st.json({
            "API_Status": "200 OK",
            "Fetched_LEI_String": fetched_lei_profile["lei_id"],
            "Corporate_Jurisdiction": fetched_lei_profile["jurisdiction"],
            "GLEIF_Verification_Status": fetched_lei_profile["entity_status"],
            "Institutional_Credit_Rating": fetched_lei_profile["credit_risk_rating"]
        })
        
        new_trade_packet = {
            "trade_id": f"BOX-{str(uuid.uuid4())[:5].upper()}",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "buyer_lei": fetched_lei_profile["lei_id"],
            "seller_lei": seller_lei_manual,
            "hs_code": target_hs_code,
            "value": float(invoice_value),
            "escrow_status": " AWAITING SELLER DROPBOX UPLOAD",
            "risk_score": "LOW" if fetched_lei_profile["credit_risk_rating"] == "AA+" else "MEDIUM"
        }
        st.session_state.trade_ledger.append(new_trade_packet)
        st.toast("New Contract Successfully Ingested with LEI Mapping!", icon="🏢")
        time.sleep(1)
        st.rerun()

# --- 7. SECTION 4: OCEAN CARRIER API INTEGRATION (THE LOGISTICS LAYER) ---
st.divider()
st.subheader("🚢 Section 4: Automated Ocean Carrier API Webhook Gateway")
st.write("Simulate server-to-server middleware webhooks. This removes human broker entry by tracking containers directly from carrier networks.")

CARRIER_WEBHOOK_SIMULATOR = {
    "BOX-TX991": {"container_id": "MSKU9918234", "carrier_scac": "MAEU (Maersk Line)", "vessel_name": "MAERSK MC-KINNEY MOLLER", "telemetry_status": "ARRIVED_AT_DESTINATION_PORT", "container_temp_c": 19.5, "gps_coordinates": "40.6892, -74.0445", "system_alert_flags": "NONE"},
    "BOX-FL442": {"container_id": "MSKU4421109", "carrier_scac": "MAEU (Maersk Line)", "vessel_name": "MAERSK ELEONORA", "telemetry_status": "EN_ROUTE_SEA_TRANSIT", "container_temp_c": 28.2, "gps_coordinates": "24.8607, 67.0011", "system_alert_flags": "BIOLOGICAL_HUMIDITY_ALERT"}
}

col_ship_1, col_ship_2 = st.columns([1.2, 2])

with col_ship_1:
    st.markdown("#### **Simulate Webhook Trigger**")
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
            with st.spinner("Parsing asynchronous webhook data stream..."): 
                time.sleep(0.5)
                
            st.code(f"// POST /api/v1/logistics/webhook HTTP/1.1\n// Host: ://blackonyx.com\n// X-Carrier-Signature: sha256_verified\n\n{str(telemetry_payload).replace("'", '"')}", language="json")
            
            for trade in st.session_state.trade_ledger:
                if trade["trade_id"] == selected_tracking_id:
                    if telemetry_payload["system_alert_flags"] == "BIOLOGICAL_HUMIDITY_ALERT":
                        trade["escrow_status"] = "🚨 LOCKED / BIOLOGICAL ANOMALY DETECTED"
                        trade["vessel_imo"] = "IMO9999999" # Map to trigger Layer 3 dark fleet penalties
                        st.error(f"❌ **Risk Flag Raised:** Biological anomaly detected on Container {telemetry_payload['container_id']}. Escrow lock engaged automatically.")
                    else:
                        trade["escrow_status"] = "🚢 EN-ROUTE / TELEMETRY NORMAL"
                        st.success(f"✔️ **Transit Stream Normal:** Container {telemetry_payload['container_id']} tracks inside parameters.")
            st.toast("Trade state updated via Carrier Webhook!", icon="🚢")
            time.sleep(1)
            st.rerun()
        else:
            st.info("🔄 Initializing carrier channel matching for newly compiled entry records...")
            for trade in st.session_state.trade_ledger:
                if trade["trade_id"] == selected_tracking_id:
                    trade["escrow_status"] = "🚢 EN-ROUTE / TELEMETRY NORMAL"
            st.success("New default carrier tracking stream established.")
            time.sleep(1)
            st.rerun()

# --- 8. SECTION 5: DISBURSEMENT WATERFALL RECONCILIATION COUPLING GATEWAY ---
st.divider()
st.subheader("⚖️ Step 5: Master Compliance & Financial Payout Waterfall")

ingestion_vector = st.radio(
    "Choose Ingestion Input Processing Vector:", 
    ["Use Sandbox Scenario Profiles (Instant Demo)", "Custom Ad-hoc Input Text Area (Live Ingestion Mode)"], 
    horizontal=True, 
    key="master_eval_ingest_radio"
)
active_extracted_payload = None

if "Profiles" in ingestion_vector:
    profile = st.selectbox(
        "Select a Target Pre-Shipment Escrow Transaction File Profile:", 
        ["Select a folder profile...", "Folder Profile 01: Standard Arabica Coffee Trade - Clear Compliance Pass", "Folder Profile 02: Dual-Use Transit Freight - Suspicious Corporate Identity Track", "Folder Profile 03: Heavy Sourcing Sacks Route - Logistics Variance Route Track"]
    )
    if "Coffee" in profile:
        active_extracted_payload = {"buyer_lei": "LEI-US-550912834", "seller_lei": "LEI-CO-110293847", "ein_number": "12-4455667", "vessel_imo": "IMO1234567", "hs_code": "0901.11", "value": 1250000.00}
    elif "Dual-Use" in profile:
        active_extracted_payload = {"buyer_lei": "LEI-US-550912834", "seller_lei": "LEI-TH-883210943", "ein_number": "00-0000000", "vessel_imo": "IMO1234567", "hs_code": "8542.40", "value": 42000000.00}
    elif "Heavy Sourcing" in profile:
        active_extracted_payload = {"buyer_lei": "LEI-US-992318451", "seller_lei": "LEI-TH-883210943", "ein_number": "99-9999999", "vessel_imo": "IMO9999999", "hs_code": "8542.40", "value": 500000.00}
else:
    live_input_text = st.text_area("Interactive Ad-hoc Text Entry Window:", value="Draft: Buyer LEI-US-550912834, Seller LEI-CO-110293847, EIN: 12-4455667, Vessel IMO1234567, HS Code: 0901.11, Value: 500000")
    if st.button("🔮 Step 1: Trigger Live Gemini Text Extraction Layer"):
        with st.spinner("🤖 Requesting Gemini..."):
            active_extracted_payload = extract_variables_from_text_with_gemini(live_input_text)
            st.session_state.ad_hoc_cache = active_extracted_payload

if "ad_hoc_cache" in st.session_state and "Custom Ad-hoc" in ingestion_vector:
    active_extracted_payload = st.session_state.ad_hoc_cache

if active_extracted_payload:
    if st.button("🔥 Run Comprehensive Layer 3 Matrix Audit", key="run_sop_master_audit_btn", width="stretch"):
        c1, c2 = st.columns(2)
        with c1:
            st.write("### 🤖 Compliance Pipeline Ingestion Logs")
            
            # Pipe compiled payload dictionary variables directly into Layer 3
            verdict = process_escrow_sop_pipeline(active_extracted_payload, matrix_selection)
            for log in verdict["logs"]:
                if "SOP" in log or "ASSESSOR" in log: st.info(log)
                elif "🛑" in log or "CRITICAL" in log: st.error(log)
                elif "⚠️" in log: st.warning(log)
                else: st.success(log)
        with c2:
        with c2:
            st.write("### 🧮 Cash Distribution Settlement Matrix")
            w = verdict["waterfall"]
            
            if verdict["approved"]:
                st.success("🎉 FIDUCIARY CLEARANCE GRANTED: ACCOUNT SAFE TO RECONCILE")
                
                # Render the distinct math outputs dynamically based on the selected financial chart path
                if "Scenario A" in matrix_selection:
                    st.markdown("#### **Scenario A: Direct Seller Disbursement Splits**")
                    st.metric("Net Remainder Seller Payout", f"${w['net_seller_payout']:,.2f}")
                    st.write(f"• **Gross Funding Captured:** ${w['gross_funding_capture']:,.2f}")
                    st.write(f"• **Logistics Transit Base Surcharge:** -${w['logistics_costs']:,.2f}")
                    st.write(f"• **Third-Party Lab Inspection:** -${w['inspection_fees']:,.2f}")
                    st.write(f"• **Escrow Agency Fee:** -${w['escrow_service_fee']:,.2f}")
                    st.write(f"• **HS Code Risk Reserve Holdback:** -${w['hs_risk_penalty_reserve']:,.2f}")
                else:
                    st.markdown("#### **Scenario B: Private Lender Advance Splits**")
                    st.metric("Net Capital Advance Amount", f"${w['private_lender_advance_amount']:,.2f}", f"Risk LTV advance Rate: {w['base_loan_to_value_rate'] * 100:.1f}%")
                    st.write(f"• **Lender Interest Reserve Lock:** ${w['accrued_interest_holdback_lock']:,.2f}")
                    st.write(f"• **Lender Facility Processing Fee:** ${w['lender_facility_fees']:,.2f}")
                    st.write(f"• **Escrow Agency Processing Fee:** ${w['escrow_processing_fee']:,.2f}")
                    st.write(f"• **Remaining Seller Payout Spread:** ${w['net_seller_payout']:,.2f}")
                
                st.markdown("---")
                st.caption("🔓 Manual Post-Disbursement Verification Checklist [SOP Steps 5-7]:")
                st.checkbox("🟩 SOP Step 5: Customs Clearance logged under declared HS Code.", value=True, key="cbp_clear_box")
                st.checkbox("⬜ SOP Step 6: Individual Escrow Ledger balances to exactly $0.00.", value=False, key="zero_balance_box")
                st.checkbox("⬜ SOP Step 7: Immutable Archival Profile package locked for 5 years.", value=False, key="archive_box")
            else:
                st.error("🛑 DISBURSEMENT PROHIBITED: Compliance gateway has locked calculation execution loops.")
