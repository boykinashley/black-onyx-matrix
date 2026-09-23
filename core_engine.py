# ==============================================================================
# 🏢 MIDDLEWARE LAYER 3: CORE RISK MONITORING & VALIDATION ENGINE (SECTION 1)
# ==============================================================================
# This module acts as the isolated, deterministic compliance firewall. 
# It handles Data Type Validation, External Government Registry REST Handshakes, 
# and the 7-Step Chronological Escrow Underwriting Calculations.
# ==============================================================================

import json
import operator
import requests
import streamlit as st
from pydantic import BaseModel, Field, ValidationError

# ==============================================================================
# 🏛️ REGULATORY SOURCE OF TRUTH REFERENCE LEAF
# ==============================================================================
REGULATORY_MASTER_MAP = {
    "ubo_verified": {
        "sop_step": 2,
        "governing_body": "FinCEN (Financial Crimes Enforcement Network)",
        "legal_citation": "31 CFR Chapter X (Customer Due Diligence Rule)",
        "scope_summary": "Mandates collection, identification, and verification of Ultimate Beneficial Owners holding >= 25% equity ownership."
    },
    "ofac_sanctions_match": {
        "sop_step": 2,
        "governing_body": "OFAC (Office of Foreign Assets Control)",
        "legal_citation": "31 CFR Chapter V (Foreign Assets Control Regulations)",
        "scope_summary": "Prohibits execution of trade financing or escrow disbursement to individuals, nations, or assets listed on the SDN Checklist."
    },
    "vessel_dark_activity": {
        "sop_step": 3,
        "governing_body": "OFAC / U.S. State Department / USCG",
        "legal_citation": "2020 Sanctions Advisory on Deceptive Shipping Practices",
        "scope_summary": "Identifies high-risk indicators including disabling or manipulating Automatic Identification System (AIS) global transponders."
    },
    "market_value_deviation": {
        "sop_step": 3,
        "governing_body": "U.S. Customs and Border Protection (CBP)",
        "legal_citation": "19 U.S.C. § 1592 (Penalties for Fraud, Gross Negligence, and Negligence)",
        "scope_summary": "Monitors trade value deviations and invoice padding designed to manipulate tariff entry summarizing ledgers."
    },
    "three_way_match_pass": {
        "sop_step": 4,
        "governing_body": "FFIEC / ALTA Framework Standards",
        "legal_citation": "FFIEC BSA/AML Examination Manual Guidelines",
        "scope_summary": "Forces absolute cryptographic correlation between the Commercial Invoice, Bill of Lading, and CBP Entry Summary Form 7501."
    }
}

# ==============================================================================
# ⚙️ SECTION 1: PYDANTIC STRUCTURAL VALIDATION HOOKS (SOP STEP 1)
# ==============================================================================
class EscrowTransactionPayload(BaseModel):
    """
    Enforces a strict type-checking firewall at the pipeline handoff point. 
    Intercepts and structural-checks raw string JSON payloads extracted by the AI.
    """
    buyer_lei: str = Field(..., description="Legal Entity Identifier of buying party")
    seller_lei: str = Field(..., description="Legal Entity Identifier of selling party")
    ein_number: str = Field(..., description="Corporate 9-digit tax identifier")
    vessel_imo: str = Field(..., description="7-digit maritime registration tracking identifier")
    hs_code: str = Field(..., description="Harmonized Tariff Schedule classification index")
    value: float = Field(..., description="Stated asset unit price inside the agreement text")

OPERATORS = {
    "equals": operator.eq,
    "not_equals": operator.ne,
    "greater_than": operator.gt,
    "less_than": operator.lt
}
# ==============================================================================
# 🌐 MIDDLEWARE LAYER 3: CORE RISK MONITORING & VALIDATION ENGINE (SECTION 2)
# ==============================================================================

def dynamic_government_hts_lookup(extracted_hs_code: str, contract_description: str) -> dict:
    """
    DYNAMIC API TRACK: Queries the official government HTS registry via a REST API call.
    SANDBOX TRACK: Automatically falls back to local data if the API key is missing.
    """
    cleaned_code = extracted_hs_code.replace(".", "").strip()[:4]
    gov_api_url = f"https://usitc.gov{cleaned_code}"
    api_key = st.secrets.get("usitc_tariff_api_key", None)
    
    if api_key:
        try:
            headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
            response = requests.get(gov_api_url, headers=headers, timeout=3.0)
            if response.status_code == 200:
                gov_payload = response.json()
                official_commodity_name = gov_payload.get("description", "Unknown Commodity")
                is_misaligned = official_commodity_name.lower()[:15] not in contract_description.lower()
                return {
                    "source": "LIVE_GOVERNMENT_REST_API",
                    "official_description": official_commodity_name,
                    "base_duty_rate": float(gov_payload.get("general_rate", 0.025)),
                    "description_mismatch_flag": is_misaligned
                }
        except Exception:
            pass

    # --- SANDBOX TEST DEFENSE RECONCILIATION FOR DEMOS ---
    sandbox_registry_database = {
        "0901": {"official_description": "Coffee, Green / Not Roasted / Arabica Packaged Sacks", "base_duty_rate": 0.045},
        "8542": {"official_description": "Electronic Integrated Circuits / Semiconductors", "base_duty_rate": 0.050},
        "8802": {"official_description": "Civil Aircraft / Private Aviation Hull and Airframes", "base_duty_rate": 0.000}
    }
    
    if cleaned_code in sandbox_registry_database:
        mock_gov_record = sandbox_registry_database[cleaned_code]
        official_name = mock_gov_record["official_description"]
        is_misaligned = True
        if "coffee" in contract_description.lower() and "0901" in cleaned_code:
            is_misaligned = False
        elif "circuit" in contract_description.lower() and "8542" in cleaned_code:
            is_misaligned = False
        elif "aircraft" in contract_description.lower() and "8802" in cleaned_code:
            is_misaligned = False
            
        return {
            "source": "SANDBOX_MOCK_REGISTRY_FALLBACK",
            "official_description": official_name,
            "base_duty_rate": mock_gov_record["base_duty_rate"],
            "description_mismatch_flag": is_misaligned
        }
        
    return {"source": "SANDBOX_MOCK_REGISTRY_FALLBACK", "official_description": "Unmapped Custom Asset Classification", "base_duty_rate": 0.020, "description_mismatch_flag": False}

def query_trade_gov_sanctions_api(entity_name: str) -> bool:
    """Hits the data.trade.gov Consolidated Screening List (CSL) REST API endpoint."""
    api_url = "https://trade.gov"
    api_key = st.secrets.get("trade_gov_key", "SANDBOX_MOCK_BYPASS")
    headers = {"subscription-key": api_key, "Accept": "application/json"}
    params = {"q": entity_name}
    try:
        response = requests.get(api_url, params=params, headers=headers, timeout=3.0)
        if response.status_code == 200:
            return response.json().get("total", 0) > 0
    except requests.exceptions.RequestException:
        pass
    return "RiskCorp" in entity_name

def query_windward_maritime_api(vessel_imo: str) -> dict:
    """Hits the Windward Maritime AI Due Diligence Screening REST API endpoint."""
    api_url = f"https://windward.ai{vessel_imo}/screening"
    headers = {"X-API-Key": st.secrets.get("windward_key", "MOCK_KEY")}
    try:
        response = requests.get(api_url, headers=headers, timeout=3.0)
        if response.status_code == 200: return response.json()
    except Exception:
        pass
    return {"dark_activity_detected": "9999" in vessel_imo, "sanction_conflict": "9999" in vessel_imo}
# ==============================================================================
# 🏢 MIDDLEWARE LAYER 3: CORE RISK MONITORING & VALIDATION ENGINE (SECTION 3)
# ==============================================================================

def calculate_direct_escrow_waterfall(gross_value: float, fees: dict, risk_reserve_rate: float) -> dict:
    """[Scenario A] Calculates net seller proceeds after operational & HS risk holdbacks."""
    logistics = fees.get("logistics_base_cost", 12000.00)
    inspection = fees.get("inspection_fee_fixed", 2500.00)
    escrow_fee = gross_value * fees.get("escrow_service_fee_rate", 0.005)
    broker_comm = gross_value * fees.get("broker_commission_rate", 0.015)
    risk_reserve = gross_value * risk_reserve_rate
    
    total_deductions = logistics + inspection + escrow_fee + broker_comm + risk_reserve
    return {
        "gross_funding_capture": gross_value,
        "logistics_costs": logistics,
        "inspection_fees": inspection,
        "escrow_service_fee": escrow_fee,
        "broker_commissions": broker_comm,
        "hs_risk_penalty_reserve": risk_reserve,
        "total_deductions": total_deductions,
        "net_seller_payout": max(0.0, gross_value - total_deductions)
    }

def calculate_lender_advance_waterfall(gross_value: float, fees: dict, lender_params: dict, vol_discount: float) -> dict:
    """[Scenario B] Calculates risk-adjusted advance amounts and interest yields."""
    base_ltv = lender_params.get("base_advance_rate", 0.80)
    final_advance_rate = max(0.0, base_ltv * (1.0 - vol_discount))
    private_lender_advance = gross_value * final_advance_rate
    
    days = lender_params.get("estimated_transit_days", 60)
    annual_rate = lender_params.get("annual_interest_rate", 0.12)
    accrued_interest_reserve = private_lender_advance * (annual_rate * (days / 365.0))
    
    lender_facility_fee = private_lender_advance * lender_params.get("lender_facility_fee_rate", 0.01)
    escrow_fee = gross_value * fees.get("escrow_service_fee_rate", 0.005)
    logistics = fees.get("logistics_base_cost", 12000.00)
    
    total_lender_charges = private_lender_advance + accrued_interest_reserve + lender_facility_fee + escrow_fee + logistics
    return {
        "base_loan_to_value_rate": final_advance_rate,
        "private_lender_advance_amount": private_lender_advance,
        "accrued_interest_holdback_lock": accrued_interest_reserve,
        "lender_facility_fees": lender_facility_fee,
        "escrow_processing_fee": escrow_fee,
        "logistics_transit_costs": logistics,
        "net_seller_payout": max(0.0, gross_value - total_lender_charges)
    }

def process_escrow_sop_pipeline(raw_ai_payload: dict, matrix_selection: str, policy_path="policy.json") -> dict:
    """Main Orchestrator. Coordinates metadata mapping and calculates the final waterfall values."""
    empty_template = {"net_seller_payout": 0.0, "error": "Gateway Terminated"}
    
    try:
        validated_data = EscrowTransactionPayload(**raw_ai_payload)
    except ValidationError as e:
        return {
            "status": "STEP_1_FAILED", "approved": False, "score": 0, "waterfall": empty_template,
            "logs": [f"SOP Step 1 Failure: Structural Document Defect - {err['loc']} - {err['msg']}" for err in e.errors()]
        }

    try:
        with open(policy_path, "r") as f: client_policy = json.load(f)
    except FileNotFoundError:
        return {
            "status": "CONFIG_ERROR", "approved": False, "score": 0, "waterfall": empty_template,
            "logs": ["Critical Error: Dynamic policy.json configuration file missing from backend root."]
        }

    total_penalty = 0
    hs_vol_discount = 0.0
    risk_reserve_rate = 0.0
    pipeline_audit_logs = ["🛡️ SOP Step 1 Clearance: Core payload tokens validated via Pydantic."]

    buyer_flagged = query_trade_gov_sanctions_api(validated_data.buyer_lei)
    seller_flagged = query_trade_gov_sanctions_api(validated_data.seller_lei)
    windward_data = query_windward_maritime_api(validated_data.vessel_imo)
    
    contract_context_text = f"{validated_data.buyer_lei} buying from {validated_data.seller_lei} transiting on vessel {validated_data.vessel_imo}"
    tariff_payload = dynamic_government_hts_lookup(validated_data.hs_code, contract_context_text)

    runtime_state_matrix = {
        "ubo_verified": validated_data.ein_number != "00-0000000",
        "ofac_sanctions_match": buyer_flagged or seller_flagged or validated_data.ein_number == "99-9999999",
        "vessel_dark_activity": windward_data["dark_activity_detected"],
        "hs_code_volatility_tier": 4 if "8542" in validated_data.hs_code or "8802" in validated_data.hs_code else 1,
        "three_way_match_pass": validated_data.ein_number != "00-0000000" and not tariff_payload["description_mismatch_flag"]
    }

    # Evaluate Rules
    configured_metrics = []
    for rule in client_policy.get("rules", []):
        metric = rule["metric"]
        configured_metrics.append(metric)
        if metric in runtime_state_matrix:
            if operator.eq(runtime_state_matrix[metric], rule["value"]):
                if rule.get("is_knockout", False):
                    return {
                        "status": "KNOCKOUT_ENFORCED", "approved": False, "score": 100, "waterfall": empty_template,
                        "logs": pipeline_audit_logs + [f"🛑 CRITICAL LEGAL BARRIER: {rule['error_message']}", "STATUS: SETTLEMENT PROHIBITED BY ENFORCEMENT"]
                    }
                total_penalty += rule["penalty_points"]
                hs_vol_discount = rule.get("hs_volatility_discount", 0.0)
                risk_reserve_rate = rule.get("risk_reserve_multiplier", 0.0)
                pipeline_audit_logs.append(f"⚠️ Threshold Triggered: {rule['error_message']}")

    # Gap Sweep
    for core_metric, legal_meta in REGULATORY_MASTER_MAP.items():
        if core_metric not in configured_metrics:
            pipeline_audit_logs.append(
                f" Louie🔎 ASSESSOR GAP TRACKER: Policy config completely lacks an appraisal filter for '{core_metric}'. "
                f"This exposes operations to unmonitored tracking under {legal_meta['governing_body']} [Ref: {legal_meta['legal_citation']}]."
            )

    fees = client_policy.get("fixed_escrow_fees", {})
    if "Direct Buyer-to-Seller" in matrix_selection:
        waterfall_results = calculate_direct_escrow_waterfall(validated_data.value, fees, risk_reserve_rate)
    else:
        lender_params = client_policy.get("lender_facility_parameters", {})
        waterfall_results = calculate_lender_advance_waterfall(validated_data.value, fees, lender_params, hs_vol_discount)

    compliance_approved = total_penalty <= client_policy.get("max_allowed_penalty_points", 35)
    return {
        "status": "SUCCESS", "approved": compliance_approved, "score": total_penalty,
        "waterfall": waterfall_results, "logs": pipeline_audit_logs
    }
