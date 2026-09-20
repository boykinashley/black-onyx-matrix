import streamlit as st
import pandas as pd
import time
import uuid

# Force clean, enterprise page state architecture
st.set_page_config(
    page_title="Black Onyx Matrix — Control Room", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 🛡️ PLATFORM STATE MACHINE & IN-APP STORAGE INITIALIZATION
# ==============================================================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "trade_ledger" not in st.session_state:
    st.session_state.trade_ledger = [
        {
            "trade_id": "BOX-TX991",
            "timestamp": "2026-09-18 10:14:22",
            "buyer_lei": "LEI-US-550912834",
            "seller_lei": "LEI-CO-110293847",
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
            "hs_code": "8802.40",
            "value": 42000000.00,
            "escrow_status": "🚨 LOCKED / ARBITRATION",
            "risk_score": "HIGH"
        }
    ]

# Global Baseline HS Rule Book Layer
HS_RULEBOOK = {
    "0901.11": {"commodity": "Coffee, Green / Not Roasted", "max_variance_pct": 2.0},
    "8802.40": {"commodity": "Civil Aircraft / Private Aviation Hull", "max_variance_pct": 0.5}
}

# ==============================================================================
# 🔏 STANDALONE SECURITY AUTHENTICATION GATEWAY
# ==============================================================================
# ==============================================================================
# 🔏 STANDALONE SECURITY AUTHENTICATION GATEWAY (WITH BYPASS FOR DEMOS)
# ==============================================================================
if not st.session_state.authenticated:
    st.title("🔒 Black Onyx Middleware Authentication")
    st.write("Access Restricted: This terminal requires a verified permanent Private Lender security credential.")
    
    # ⚡ CONVENTION DEMO QUICK BYPASS (One-click unlock for testing)
    st.info("💡 **Presentation Shortcut:** Check 'Enable Demo Mode' below to instantly bypass this gate without typing credentials.")
    demo_bypass = st.checkbox("⚡ Enable Convention Demo Mode / Quick Unlock")
    
    if demo_bypass:
        st.session_state.authenticated = True
        st.success("Demo Mode Authorized. Unlocking terminal...")
        time.sleep(1)
        st.rerun()
        
    # Standard Manual Login Form Layout
    with st.form("lender_auth_gate"):
        username = st.text_input("Financier Login Identifier:", value="lender@blackonyx.com")
        password = st.text_input("Security Encryption Key:", value="blackonyx2026", type="password")
        submit_login = st.form_submit_button("Verify Identity & Unlock Middleware Core", use_container_width=True)
        
        if submit_login:
            # Explicit secure credential validation logic
            if username == "lender@blackonyx.com" and password == "blackonyx2026":
                st.session_state.authenticated = True
                st.success("Identity Authenticated. Mounting system cluster...")
                st.rerun()
            else:
                st.error("Access Denied: Invalid security configuration strings or key signature.")
    st.stop()

# app.py
import streamlit as st
import json

# Import your separated logic layers from your GitHub repository
from core_engine import run_trade_compliance_engine
from ai_extractor import extract_pdf_variables_with_gemini

# --- PAGE INITIALIZATION & STYLING ---
st.set_page_config(page_title="Trade Finance Compliance Sandbox", layout="wide")
st.title("🚢 AI Trade Finance & Risk Compliance Gateway")
st.caption("A $0 Budget Sandbox proving the deterministic separation of AI Data Extraction vs. Mathematical Risk Rubrics.")

# --- LAYER 4: DYNAMIC POLICY CONFIGURATION (ADMIN VIEW) ---
st.sidebar.header("⚙️ Compliance Officer Dashboard")
st.sidebar.write("Modify corporate risk thresholds and point thresholds dynamically without changing application source code.")

# Load active thresholds from your local policy text file
try:
    with open("policy.json", "r") as f:
        policy_config = json.load(f)
except FileNotFoundError:
    st.sidebar.error("Error: 'policy.json' file not found in your repository directory.")
    st.stop()

# Interactive Policy Threshold Sliders for the Admin Panel
max_penalty_limit = st.sidebar.slider(
    "Max Allowed Total Penalty Points", 
    0, 100, policy_config.get("max_allowed_penalty_points", 30)
)
hs_risk_threshold = st.sidebar.slider(
    "HS Code Risk Tier Threshold (Triggers Penalty if Greater)", 
    1, 5, 2
)

# Sync admin dashboard changes back into the session configuration mapping
policy_config["max_allowed_penalty_points"] = max_penalty_limit
for rule in policy_config["rules"]:
    if rule["metric"] == "hs_code_risk_tier":
        rule["value"] = hs_risk_threshold

with open("policy.json", "w") as f:
    json.dump(policy_config, f, indent=2)

st.sidebar.success("✅ Policy JSON synced successfully in active runtime memory.")

# --- LAYER 1 & 2: SCENARIO SELECTOR & MOCK AI LAYER ---
st.subheader("📋 Step 1: Document Processing & Variable Extraction")
mode = st.radio("Choose Input Processing Mechanism:", ["Run Sandbox Scenario Profiles (Instant Demo)", "Upload Live Document PDF (Requires Free Gemini Key)"])

extracted_ai_payload = None

if mode == "Run Sandbox Scenario Profiles (Instant Demo)":
    st.info("💡 Select an industry shipping manifest profile below to simulate the exact structured data payload an AI extraction agent pulls from a trade invoice.")
    
    # The interactive scenario dropdown menu
    scenario = st.selectbox(
        "Choose an Automated Trade Shipping Profile:",
        [
            "Select a profile...",
            "Scenario A: Bulk Coffee Shipping (Thailand to USA) - Low Risk Profile",
            "Scenario B: Electronics Hardware Freight (Shenzhen to Munich) - Moderate Risk Profile",
            "Scenario C: Industrial Machinery Parts (Restricted Port Route) - Critical Block Profile"
        ]
    )
    
    # Mapping the selected profile index to its deterministic simulated payload dict
    # app.py (Replace the profile dictionary section with this block)

    if scenario == "Scenario A: Bulk Coffee Shipping (Thailand to USA) - Low Risk Profile":
        extracted_ai_payload = {
            "vendor_name": "Global Coffee Traders Inc",
            "ein_number": "12-4455667", # Clean, active company registry lookup profile
            "is_sanctioned_port": False,
            "hs_code_risk_tier": 1
        }
    elif scenario == "Scenario B: Electronics Hardware Freight (Shenzhen to Munich) - Moderate Risk Profile":
        extracted_ai_payload = {
            "vendor_name": "Shenzhen Tech Parts",
            "ein_number": "00-0000000", # Explicitly flags as a SHELF/INACTIVE company in our resolver
            "is_sanctioned_port": False,
            "hs_code_risk_tier": 3
        }
    elif scenario == "Scenario C: Industrial Machinery Parts (Restricted Port Route) - Critical Block Profile":
        extracted_ai_payload = {
            "vendor_name": "RiskCorp Logistics Limited", # Matches our sandbox sanctions list resolver
            "ein_number": "99-9999999",
            "is_sanctioned_port": True,
            "hs_code_risk_tier": 2
        }

else:
    # Live Document Upload Route utilizing Free Cloud Processing
    uploaded_file = st.file_uploader("Upload Trade Invoice, Bill of Lading, or Letter of Credit (PDF)", type=["pdf"])
    if uploaded_file:
        with st.spinner("🤖 Triggering Google Gemini 1.5 Flash to read unstructured text contents..."):
            extracted_ai_payload = extract_pdf_variables_with_gemini(uploaded_file)

# --- LAYER 3: CORE COMPLIANCE ENGINE RUNTIME ---
if extracted_ai_payload:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("### 🤖 Structured Data Extracted by AI Sub-Agent")
        st.markdown("This payload represents the **untrusted text translation**. The AI layer ends here.")
        st.json(extracted_ai_payload)
        
    with col2:
        st.write("### ⚖️ Deterministic Mathematical Firewall Engine")
        st.markdown("The core code engine loads the Pydantic schemas, aggregates math criteria, and enforces final verdicts.")
        
        # Pass the AI dictionary payload directly into the independent mathematical function
        verdict = run_trade_compliance_engine(extracted_ai_payload)
        
        # Display the visual charts and metrics based on the pure python outcomes
        if verdict["status"] == "SUCCESS":
            if verdict["approved"]:
                st.success("🎉 TRANSACTION APPROVED BY PORT GATEWAY")
            else:
                st.error("🛑 TRANSACTION DENIED BY RISK COMPLIANCE")
                
            st.metric(
                label="Aggregated Matrix Penalty Score", 
                value=f"{verdict['score']} Points", 
                delta=f"Limit: {max_penalty_limit} Points", 
                delta_color="inverse"
            )
            
            # Use visual anchors to make log entries highly scannable
            st.write("#### 📊 Rule Evaluation Audit Log Logs:")
            for log_entry in verdict["logs"]:
                if "APPROVED" in log_entry:
                    st.info(f"✨ {log_entry}")
                elif "REJECTED" in log_entry or "CRITICAL" in log_entry or "DENIAL" in log_entry:
                    st.error(f"🛑 {log_entry}")
                else:
                    st.warning(f"⚠️ {log_entry}")
                    
        else:
            # Displays if Pydantic catches structural data corruption coming from the AI agent response
            st.error("🚨 CORRUPT AI TRANSACTION INJECTION DETECTED!")
            st.write("The validation engine intercepted bad formatting before code math calculations could execute:")
            for error_message in verdict["logs"]:
                st.code(error_message)


# ==============================================================================
# 🏛️ CORE DASHBOARD CONTROL ROOM (THE MAIN UI PANEL)
# ==============================================================================
st.title("💎 Core Dashboard Control Room")
st.write("Alternative Credit & Escrow Funds Transaction Telemetry Terminal.")

# 1. SIDEBAR IDENTITY BRANDING
with st.sidebar:
    st.markdown("## ⚙️ Middleware Matrix")
    st.caption("Target Persona: Private Lender / Financier")
    st.divider()
    st.markdown("### 🚦 Operator Identity Profile")
    st.success("Connected: Active Node Session")
    st.info("Role: Primary Funding Referee")
    if st.button("🔒 Log Out of Terminal", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

# 2. CROSS-BORDER RISK METRIC DISPLAYS
st.subheader("📊 Cross-Border Risk Analytics & Counterparty Exposure")
col_r1, col_r2, col_r3, col_r4 = st.columns(4)

with col_r1:
    st.metric(label="Global Active Capital Exposure", value="$43.25M USD", delta="+$2.1M This Week")
with col_r2:
    st.metric(label="Sovereign Risk Level (Origin Index)", value="Stable (Low)", delta="No Alerts")
with col_r3:
    st.metric(label="Counterparty LEI Match Accuracy", value="100.00%", delta="Verified via API")
with col_r4:
    st.metric(label="Active Escrow Violation Liquidity", value="$12.50M USD", delta="-4.2% Risk Deflection", delta_color="inverse")

st.divider()

# 3. ACTIVE TRADE PROFILE MONITORS
st.subheader("🚢 Active Trade Flow Pipeline & Ledger Records")
df_ledger = pd.DataFrame(st.session_state.trade_ledger)

# Render a clean, scannable data grid tracking global asset flows
st.dataframe(
    df_ledger,
    column_config={
        "trade_id": "Transaction Token Reference",
        "timestamp": "Audit Ingress Log Date",
        "buyer_lei": "Buyer Corporate LEI",
        "seller_lei": "Seller Corporate LEI",
        "hs_code": "Target HS Code",
        "value": st.column_config.NumberColumn("Contract Invoice Value", format="$%,.2f"),
        "escrow_status": "Escrow Condition Status",
        "risk_score": "System Risk Rating"
    },
    use_container_width=True,
    hide_index=True
)
# Append or merge this logic directly below Section 1's main dashboard rendering

# ==============================================================================
# 🎯 SECTION 2: THE INGESTION LAYER & ZERO-LOGIN DROP BOX GENERATOR
# ==============================================================================
st.divider()
st.subheader("📩 Step 2: Automated Seller Ingestion Workflow")
st.write("Generate a secure, single-use workspace URL token to allow external counterparties to upload verification files.")

# A. LENDER WORKSPACE: LINK GENERATOR COMPONENT
col_gen_1, col_gen_2 = st.columns([1.2, 2])

with col_gen_1:
    st.markdown("#### **Generate Token Link**")
    target_trade_id = st.selectbox(
        "Select Active Transaction Reference:", 
        [t["trade_id"] for t in st.session_state.trade_ledger if "RELEASED" not in t["escrow_status"]]
    )
    
    if st.button("⚡ Generate One-Time Secure Token Link", use_container_width=True):
        # Generate an absolute cryptographic reference string
        unique_secure_token = f"TOKEN-{str(uuid.uuid4())[:8].upper()}"
        
        # Save structural tracking mapping into session memory
        st.session_state.active_drop_token = unique_secure_token
        st.session_state.token_trade_target = target_trade_id
        st.session_state.token_used = False
        st.success("Token generated in platform cache memory!")

# Render link output if it exists in state
if "active_drop_token" in st.session_state and not st.session_state.token_used:
    with col_gen_2:
        st.markdown("#### **Generated Secure URL Manifest**")
        # Simulating a live cloud application domain URL string
        simulated_secure_url = f"https://streamlit.io{st.session_state.active_drop_token}"
        st.info(f"📧 **Emailed Target Link Payload to Seller:**\n\n`{simulated_secure_url}`")
        
        # Simulated shortcut action for testing on your single-screen app environment
        st.write("---")
        st.caption("📱 Presentation Shortcut: Click to simulate the Seller opening that email link:")
        if st.button("👉 Simulate Seller Clicking Email URL Link"):
            st.session_state.simulated_query_param = st.session_state.active_drop_token
            st.rerun()

st.divider()

# ==============================================================================
# B. PUBLIC WORKSPACE: BARE UN-AUTHENTICATED SELLER DROP BOX INTERFACE
# ==============================================================================
# Simulate a URL parameter trigger check at the bottom layer of the main loop
if "simulated_query_param" in st.session_state and st.session_state.simulated_query_param != "":
    current_token = st.session_state.simulated_query_param
    
    # Verify token matching state
    if current_token == st.session_state.get("active_drop_token") and not st.session_state.get("token_used", False):
        
        # Completely block the regular UI view, showing only the public drop window
        st.empty() 
        st.markdown("---")
        st.title("📥 Secure Document Drop Box Terminal")
        st.write(f"Authorized Node Workspace Profile Link ID: `{current_token}`")
        st.caption(f"Linked Transaction Reference: **{st.session_state.token_trade_target}**")
        st.warning("🔒 Confidential: You do not need a password. This secure file gateway authorizes your upload directly.")

        # Single Upload Form Interface
        with st.form("public_seller_drop_box_form"):
            st.markdown("### **📤 Ingest Official Verification Assets**")
            st.write("Please drop your official third-party Certificate of Inspection PDF file below to update the lender:")
            
            uploaded_inspection_file = st.file_uploader(
                "Select Certificate of Inspection (PDF/JSON Data Format)", 
                type=["pdf", "json"]
            )
            
            submit_upload = st.form_submit_button("Verify & Finalize Document Ingress", use_container_width=True)
            
            if submit_upload:
                if uploaded_inspection_file is not None:
                    # Ingress complete. Mutate state flags to protect single-use stability
                    st.session_state.token_used = True
                    st.session_state.simulated_query_param = "" # Clear temporary query parameters
                    
                    # Lock data state updates into the corresponding master ledger record row index
                    for trade in st.session_state.trade_ledger:
                        if trade["trade_id"] == st.session_state.token_trade_target:
                            trade["escrow_status"] = "⏳ PENDING AUTOMATED CROSS-CHECK"
                    
                    # Present clean termination success banner instructions
                    st.balloons()
                    st.success("🎉 Success! Your Certificate of Inspection has been securely ingested into the platform's verification array.")
                    st.info("ℹ️ System Update: This secure session token has expired. Your workflow is complete. Please close this browser tab safely.")
                    
                    time.sleep(4)
                    st.rerun()
                else:
                    st.error("⚠️ All file uploads are mandatory to complete document cross-checking workflows.")
        st.stop() # Freeze view execution context to block the remaining app layer panels
# Append or merge this logic directly below Section 2's components

# ==============================================================================
# 🏢 SECTION 3: AUTOMATED INGESTION LAYER (THE BUYER LAYER)
# ==============================================================================
st.divider()
st.subheader("🏢 Day 0 Initial Contract Ingestion Layer")
st.write("Bypass manual counterparty data entry. Initialize a trade contract parameter check to trigger automated background LEI validation.")

# Simulated External LEI Global API Database (No manual login required)
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

# Day 0 Ingestion Interface
col_ingest_1, col_ingest_2 = st.columns([1.2, 2])

with col_ingest_1:
    st.markdown("#### **Day 0 Parameter Ingestion**")
    with st.form("day_0_ingestion_form"):
        # Select target pre-vetted corporate nodes to simulate automated lookup triggers
        buyer_node_key = st.selectbox(
            "Select Target Importer Node:", 
            options=list(LEI_GLOBAL_REGISTRY.keys()),
            format_func=lambda x: LEI_GLOBAL_REGISTRY[x]["legal_name"]
        )
        
        seller_lei_manual = st.text_input("Seller Identity Identifier / LEI:", value="LEI-CO-110293847")
        target_hs_code = st.selectbox("Target HS Commodity Code:", options=list(HS_RULEBOOK.keys()))
        invoice_value = st.number_input("Escrow Contract Value ($ USD):", min_value=10000, value=500000)
        
        submit_ingestion = st.form_submit_button("🚀 Ingest Contract & Pull LEI Metrics", use_container_width=True)

if submit_ingestion:
    with col_ingest_2:
        st.markdown("#### **⚙️ Background API Telemetry Log**")
        
        # 1. Trigger automated simulated API background call to pull global registry metrics
        with st.spinner("Pinging Global GLEIF API Database for corporate entity telemetry..."):
            time.sleep(1) # Simulating network latency
            fetched_lei_profile = LEI_GLOBAL_REGISTRY[buyer_node_key]
            
        st.success(f"✅ Background Handshake Success! Fetched Profile for {fetched_lei_profile['legal_name']}")
        
        # Display the fetched API telemetry components to the Lender inside the control room
        st.json({
            "API_Status": "200 OK",
            "Fetched_LEI_String": fetched_lei_profile["lei_id"],
            "Corporate_Jurisdiction": fetched_lei_profile["jurisdiction"],
            "GLEIF_Verification_Status": fetched_lei_profile["entity_status"],
            "Institutional_Credit_Rating": fetched_lei_profile["credit_risk_rating"]
        })
        
        # 2. Automatically map and compile the structural record packet directly into the backend database ledger
        new_trade_packet = {
            "trade_id": f"BOX-{str(uuid.uuid4())[:5].upper()}",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "buyer_lei": fetched_lei_profile["lei_id"], # Map pulled metrics directly
            "seller_lei": seller_lei_manual,
            "hs_code": target_hs_code,
            "value": float(invoice_value),
            "escrow_status": "⏳ AWAITING SELLER DROPBOX UPLOAD",
            "risk_score": "LOW" if fetched_lei_profile["credit_risk_rating"] == "AA+" else "MEDIUM"
        }
        
        # Push cleanly to our primary state database layer
        st.session_state.trade_ledger.append(new_trade_packet)
        st.toast("New Contract Successfully Ingested with LEI Mapping!", icon="🏢")
        
        time.sleep(2)
        st.rerun()
# Append or merge this logic directly below Section 3's components

# ==============================================================================
# 🚢 SECTION 4: OCEAN CARRIER API INTEGRATION (THE LOGISTICS LAYER)
# ==============================================================================
st.divider()
st.subheader("🚢 Automated Ocean Carrier API Webhook Gateway")
st.write("Simulate server-to-server middleware webhooks. This removes human broker entry by tracking containers directly from carrier networks.")

# Mock Ocean Carrier Telemetry API Payload Data Structure
CARRIER_WEBHOOK_SIMULATOR = {
    "BOX-TX991": {
        "container_id": "MSKU9918234",
        "carrier_scac": "MAEU (Maersk Line)",
        "vessel_name": "MAERSK MC-KINNEY MOLLER",
        "telemetry_status": "ARRIVED_AT_DESTINATION_PORT",
        "container_temp_c": 19.5,
        "gps_coordinates": "40.6892, -74.0445", # Port of NY/NJ
        "system_alert_flags": "NONE"
    },
    "BOX-FL442": {
        "container_id": "MSKU4421109",
        "carrier_scac": "MAEU (Maersk Line)",
        "vessel_name": "MAERSK ELEONORA",
        "telemetry_status": "EN_ROUTE_SEA_TRANSIT",
        "container_temp_c": 28.2, # Warning: Temperature spike detected
        "gps_coordinates": "24.8607, 67.0011",
        "system_alert_flags": "BIOLOGICAL_HUMIDITY_ALERT"
    }
}

col_ship_1, col_ship_2 = st.columns([1.2, 2])

with col_ship_1:
    st.markdown("#### **Simulate Webhook Trigger**")
    st.write("Select an active transaction tracking token to mimic an automated server update push from Maersk API endpoints:")
    
    # Target trades currently tracked in system memory
    active_tracking_choices = [t["trade_id"] for t in st.session_state.trade_ledger]
    selected_tracking_id = st.selectbox("Select Target Container Pipeline To Ping:", options=active_tracking_choices, key="carrier_api_select_box")
    
    trigger_webhook = st.button("📡 Ingest Automated Carrier Webhook Payload", use_container_width=True)

if trigger_webhook:
    with col_ship_2:
        st.markdown("#### **🛠️ Server-to-Server JSON Payload Parsing**")
        
        # Pull mock telemetric records matching selected trade token
        if selected_tracking_id in CARRIER_WEBHOOK_SIMULATOR:
            telemetry_payload = CARRIER_WEBHOOK_SIMULATOR[selected_tracking_id]
            
            with st.spinner("Parsing asynchronous webhook data stream..."):
                time.sleep(1) # Simulating API latency
                
            st.code(f"""
            // POST /api/v1/logistics/webhook HTTP/1.1
            // Host: ://blackonyx.com
            // X-Carrier-Signature: sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
            
            {str(telemetry_payload).replace("'", '"')}
            """, language="json")
            
            # 2. Mutate active ledger profiles dynamically based on the webhook status data flags
            for trade in st.session_state.trade_ledger:
                if trade["trade_id"] == selected_tracking_id:
                    # Update status maps according to container alert values
                    if telemetry_payload["system_alert_flags"] == "BIOLOGICAL_HUMIDITY_ALERT":
                        trade["escrow_status"] = "🚨 LOCKED / BIOLOGICAL ANOMALY DETECTED"
                        trade["risk_score"] = "HIGH"
                        st.error(f"❌ **Risk Flag Raised:** Biological anomaly detected on Container {telemetry_payload['container_id']}. Escrow lock engaged automatically.")
                    else:
                        trade["escrow_status"] = "🚢 EN-ROUTE / TELEMETRY NORMAL"
                        trade["risk_score"] = "LOW"
                        st.success(f"✔️ **Transit Stream Normal:** Container {telemetry_payload['container_id']} is tracking cleanly inside structural parameters.")
                        
            st.toast("Trade state updated via Carrier Webhook!", icon="🚢")
            time.sleep(2)
            st.rerun()
        else:
            # Fallback dynamic packet generator for freshly ingested user custom entries
            st.info("🔄 Initializing carrier channel matching for newly compiled entry records...")
            for trade in st.session_state.trade_ledger:
                if trade["trade_id"] == selected_tracking_id:
                    trade["escrow_status"] = "🚢 EN-ROUTE / TELEMETRY NORMAL"
            st.success("New default carrier tracking stream established for this transaction token.")
            time.sleep(1)
            st.rerun()


# ==============================================================================
# 🎛️ UNDERWRITING RISK ENGINE CORE FUNCTION
# ==============================================================================
def calculate_risk_profile(data, value):
    score = 0
    covenants = []
    
    # 1. Tariff & Margin Drag Evaluation
    total_tariff_exposure = data["base_duty_rate"] + data["section_301_tariff"]
    if total_tariff_exposure > 20.0:
        score += 40
        covenants.append("💰 **Duty Escrow Required:** High tariff exposure detected. Borrower must pre-fund duty cash buffer.")
    elif total_tariff_exposure > 5.0:
        score += 20
    else:
        score += 5

    # 2. Operational / Regulatory Delay Evaluation (PGA Flagger)
    if data["has_pga_flag"]:
        score += 35
        agencies_str = ", ".join(data["pga_agencies"])
        covenants.append(f"⏳ **PGA Hold Mitigation:** Goods subject to {agencies_str} oversight. Verify pre-clearance filings.")
    else:
        score += 10

    # 3. Collateral Marketability Evaluation
    if data["liquidity_classification"] == "High":
        score += 5
        base_advance = 0.85
    elif data["liquidity_classification"] == "Moderate":
        score += 20
        base_advance = 0.75
    else:
        score += 45
        base_advance = 0.55
        covenants.append("📉 **Alternative Recourse:** Low collateral liquidity. Require parent corporate guarantee.")

    # 4. Final Risk Tier and Capital Limits Matrix
    # Max possible raw points = 120
    normalized_score = int((score / 120) * 100)
    
    if normalized_score <= 35:
        tier = "🟢 Low Risk Profile"
        final_advance_rate = base_advance
    elif normalized_score <= 65:
        tier = "🟡 Moderate Risk Profile"
        final_advance_rate = base_advance - 0.05
    else:
        tier = "🔴 High Risk Profile"
        final_advance_rate = base_advance - 0.15

    max_capital_outlay = value * final_advance_rate

    return normalized_score, tier, final_advance_rate, max_capital_outlay, covenants


# ==============================================================================
# 📊 CONTROL ROOM INTERFACE LAYER
# ==============================================================================
st.subheader("📊 Black Onyx Active Trade Ledger")
df_ledger = pd.DataFrame(st.session_state.trade_ledger)
st.dataframe(df_ledger, use_container_width=True)

st.markdown("---")

# Split layout for Risk Evaluation and Sourcing Mock Repository
st.subheader("🔍 Lender Risk Underwriting Panel")
col_panel, col_results = st.columns(2)

with col_panel:
    st.markdown("#### 🛠️ Risk Parameter Assignment")
    
    # Let user pick a trade transaction from your state machine ledger
    selected_trade_id = st.selectbox(
        "Select Active Ledger ID to Underwrite:", 
        options=[tx["trade_id"] for tx in st.session_state.trade_ledger]
    )
    
    # Retrieve active trade data from ledger
    active_tx = next(item for item in st.session_state.trade_ledger if item["trade_id"] == selected_trade_id)
    
    # Match against global baseline rulebook layer if available
    rulebook_info = HS_RULEBOOK.get(active_tx["hs_code"], {"commodity": "Unknown Item", "max_variance_pct": 1.0})
    
    # Sidebar or Panel Overrides matching our mock data parameters
    country_of_origin = st.selectbox("Sourcing Country of Origin:", ["Thailand", "China", "Taiwan", "Germany", "Mexico"], index=0)
    
    # Context-aware mock variables setup based on active HS Code
    if active_tx["hs_code"] == "0901.11":
        base_duty = 0.0
        pga_flag = True
        pga_list = ["FDA", "USDA"]
        liquidity = "High"
    elif active_tx["hs_code"] == "8802.40":
        base_duty = 5.0
        pga_flag = True
        pga_list = ["FAA", "BIS"]
        liquidity = "Low"
    else:
        base_duty = 2.5
        pga_flag = False
        pga_list = []
        liquidity = "Moderate"

    # Encapsulate parameters into engine payload format
    simulated_payload = {
        "htsus": active_tx["hs_code"],
        "base_duty_rate": base_duty,
        "section_301_tariff": 25.0 if country_of_origin == "China" else 0.0,
        "has_pga_flag": pga_flag,
        "pga_agencies": pga_list,
        "liquidity_classification": liquidity
    }
    
    st.caption(f"**Associated Rulebook Entity:** {rulebook_info['commodity']} (Max Allowed Variance: {rulebook_info['max_variance_pct']}%)")

with col_results:
    st.markdown("#### 🧮 Automated Risk Analysis Metrics")
    
    # Execute Underwriting Matrix Scoring
    risk_score, risk_tier, advance_rate, max_outlay, dynamic_cps = calculate_risk_profile(
        simulated_payload, active_tx["value"]
    )
    
    # Score metrics rendering layer
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric(label="Calculated Matrix Score", value=f"{risk_score} / 100", delta=risk_tier, delta_color="inverse")
        st.metric(label="Target Contract Advance", value=f"{advance_rate * 100:.1f}%")
    with metric_col2:
        st.metric(label="Transaction Value Evaluated", value=f"${active_tx['value']:,.2f}")
        st.metric(label="Max Capital Limit Allocation", value=f"${max_outlay:,.2f}")
        
    st.markdown("##### 📋 Generated Conditions Precedent (CPs)")
    if dynamic_cps:
        for cp in dynamic_cps:
            st.markdown(cp)
    else:
        st.markdown("✅ **Standard Framework Verification:** Asset parameters meet target structural margins.")

# =====================================================================
# 🚀 ADDED TO THE BOTTOM: TRADE CONTRACT AI PARSER & LEDGER ROUTER TOOL
# =====================================================================
# =====================================================================
# 🚀 UPGRADED: NATIVE GEMINI TRADE COMPLIANCE CONTROL ROOM (100% FREE)
# =====================================================================
import json
import io
import streamlit as st

# PASTE THIS EXACT CLEAN REPLACEMENT HERE:
import pypdf
from google import genai
from google.genai import types
from pydantic import BaseModel

st.write("---") 

# This opens the compliance control room drawer immediately on page refresh
with st.expander("🛡️ OPEN TRADE COMPLIANCE SYSTEM CONTROL ROOM", expanded=True):

        
        # Hardcoded Matrix Lookups
        HS_ROUTING_MATRIX = {
            "0901": {
                "commodity_group": "Agricultural Resources",
                "item_name": "Coffee / Tea Commodities",
                "debit_account": "1410-Inventory-Raw-Agricultural-Materials",
                "primary_agency": "FDA",
                "compliance_pipeline": "FDA_PRIOR_NOTICE_AND_PHYTOSANITARY_RELEASE",
                "base_duty_rate": 0.045
            },
            "8802": {
                "commodity_group": "Aerospace Capital Goods",
                "item_name": "Commercial Aircraft",
                "debit_account": "1230-Fixed-Assets-Aircraft-Equipment",
                "primary_agency": "FAA / BIS",
                "compliance_pipeline": "FAA_AIRWORTHINESS_AND_EXPORT_CONTROL",
                "base_duty_rate": 0.000
            },
            "8803": {
                "commodity_group": "Aviation Parts",
                "item_name": "Aerospace Components",
                "debit_account": "1420-Inventory-Maintenance-Parts",
                "primary_agency": "BIS",
                "compliance_pipeline": "COMMERCE_CONTROL_LIST_DUAL_USE_SCREENING",
                "base_duty_rate": 0.025
            }
        }

        class TradeContractSchema(BaseModel):
            extracted_hs_code: str
            contract_value_fob: float
            counterparty_country: str
            payment_terms: str
            risk_rubric_score: int
            rubric_compliance_notes: list[str]

        # -----------------------------------------------------------------
        # CONTROL ROOM CONFIGURATION BAR
        # -----------------------------------------------------------------
        st.markdown("### ⚙️ System Ingestion Links")
        cfg_col1, cfg_col2 = st.columns([1, 2])
        with cfg_col1:
            gemini_key = st.text_input("Gemini Node Key", type="password", key="ctrl_gemini_key")
        with cfg_col2:
            uploaded_file = st.file_uploader("Ingest Trade Contract manifest (PDF)", type=["pdf"], key="ctrl_pdf_uploader")
            
        if not gemini_key:
            st.info("💡 Input your free Gemini API key to activate the Control Center link pathways.")

        if uploaded_file and gemini_key:
            if st.button("🔴 INITIALIZE TRANSACTION SCAN SEQUENCE", key="ctrl_trigger_btn", use_container_width=True):
                with st.spinner("Executing system scanning parameters..."):
                    try:
                        # PASTE THIS EXACT CLEAN REPLACEMENT HERE:
                        extracted_text = ""
                        pdf_reader = pypdf.PdfReader(io.BytesIO(uploaded_file.getvalue()))
                        for page in pdf_reader.pages:
                            text = page.extract_text()
                            if text:
                                extracted_text += text + "\n"

                        if not extracted_text.strip():
                            st.error("SYSTEM CRITICAL: Terminal read failed. PDF text layers blank.")
                            st.stop()

                        client = genai.Client(api_key=gemini_key)
                        prompt = f"Extract target HS Code, FOB asset value, country, payment structural bounds, and apply the strict risk rubric schema matrix:\n{extracted_text}"

                        response = client.models.generate_content(
                            model='gemini-3.6-flash',
                            contents=prompt,
                            config=types.GenerateContentConfig(
                                response_mime_type="application/json",
                                response_schema=TradeContractSchema,
                            ),
                        )
                        ai_output = json.loads(response.text)
                        
                        raw_code = ai_output.get("extracted_hs_code", "").strip()
                        heading_key = raw_code.replace(".", "")[:4]
                        
                        # -----------------------------------------------------------------
                        # CONTROL ROOM OPERATIONS DASHBOARD INTERFACE
                        # -----------------------------------------------------------------
                        st.subheader("🖥️ Live Operations Grid")
                        
                        # Row 1: System Health Status & Main Gates
                        stat_col1, stat_col2, stat_col3 = st.columns(3)
                        with stat_col1:
                            st.metric("COMMODITY PROFILE", ai_output.get("counterparty_country", "UNKNOWN").upper())
                            st.caption("Origin Node Verified")
                        with stat_col2:
                            risk_val = ai_output.get("risk_rubric_score", 0)
                            st.metric("AGGREGATED RISK METRIC", f"{risk_val} / 100")
                            if risk_val > 45:
                                st.error("🛑 ESCALATED RISK EXPOSURE DETECTED")
                            else:
                                st.success("🟢 SECURITY BOUNDS NOMINAL")
                        with stat_col3:
                            if heading_key in HS_ROUTING_MATRIX:
                                st.metric("CUSTOMS CONSOLE GATEWAY", f"HS {heading_key}")
                                st.info(f"PGA Pipeline: {HS_ROUTING_MATRIX[heading_key]['primary_agency']}")
                            else:
                                st.metric("CUSTOMS CONSOLE GATEWAY", "UNMAPPED")
                                st.error("❌ ROUTING FAULT: HS UNKNOWN")

                        st.divider()

                        # Row 2: Financial Routing Registers vs System Audit Log
                        data_col1, data_col2 = st.columns([4, 5])
                        with data_col1:
                            st.markdown("#### 📊 Dynamic Ledger Register Adjustment")
                            if heading_key in HS_ROUTING_MATRIX:
                                rule = HS_ROUTING_MATRIX[heading_key]
                                fob_val = ai_output.get("contract_value_fob", 0.0)
                                duties_calculated = fob_val * rule["base_duty_rate"]
                                
                                st.code(f"""
[DEBIT REGISTERED]
Account:  {rule['debit_account']}
Amount:   ${fob_val:,.2f}

[DEBIT REGISTERED]
Account:  5120-Import-Taxes-and-Duties
Amount:   ${duties_calculated:,.2f}

[CREDIT CLEARING]
Account:  2100-Accounts-Payable-Trade
Amount:   ${fob_val + duties_calculated:,.2f}
                                """, language="text")
                            else:
                                st.write("Ledger generation paused. Correct classification code required.")

                        with data_col2:
                            st.markdown("#### 🗒️ Automated Risk Matrix Audit Logs")
                            for index, note in enumerate(ai_output.get("rubric_compliance_notes", [])):
                                st.info(f"Log Item [{index+1}]: {note}")
                                
                            if heading_key in HS_ROUTING_MATRIX:
                                st.warning(f"Compliance Release Target: Run system validation task pipeline [{HS_ROUTING_MATRIX[heading_key]['compliance_pipeline']}]")

                    except Exception as e:
                        st.error(f"SYSTEM FAULT IN CONSOLE: {str(e)}")
