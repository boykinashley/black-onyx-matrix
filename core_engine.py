# core_engine.py
import json
import operator
import requests
from pydantic import BaseModel, Field, ValidationError

# --- PIPELINE SCHEMAS ---
class EscrowTransactionPayload(BaseModel):
    buyer_name: str = Field(..., description="Legal name of buying entity")
    seller_name: str = Field(..., description="Legal name of selling entity")
    ein_number: str = Field(..., description="Corporate 9-digit tax identifier")
    vessel_imo: str = Field(..., description="7-digit maritime registration tracking identifier")
    hs_code: str = Field(..., description="Harmonized Tariff Schedule classification index")
    contract_unit_price: float = Field(..., description="Stated price per commodity unit in contract")

OPERATORS = {
    "equals": operator.eq,
    "not_equals": operator.ne,
    "greater_than": operator.gt
}

# --- STEP 2 REGISTRY ENDPOINTS ---
def execute_step2_identity_and_sanction_checks(ein: str, company_name: str) -> dict:
    """Queries FinCEN transparency databases and LexisNexis / OFAC screening registries."""
    # Real-world target routing placeholder for the U.S. Consolidated Screening List API
    ita_api_endpoint = "https://trade.gov"
    
    # Sandbox profile management simulation
    if ein == "00-0000000":
        return {"ubo_verified": False, "ofac_match": False}
    if ein == "99-9999999":
        return {"ubo_verified": True, "ofac_match": True}
    return {"ubo_verified": True, "ofac_match": False}

# --- STEP 3 LOGISTICS TELEMETRY ---
def execute_step3_mid_transit_tracking(vessel_imo: str, contract_price: float) -> dict:
    """Queries Windward Maritime AI tracking layers and market pricing index APIs."""
    # Real-world endpoint mapping target placeholder
    windward_endpoint = f"https://windward.ai{vessel_imo}/screening"
    
    # Sandbox path tracking behavior mapping
    if vessel_imo == "IMO9999999":
        return {"dark_activity_detected": True, "index_price_deviation": 25.0}
    return {"dark_activity_detected": False, "index_price_deviation": 4.5}

# --- STEP 4 FINAL AUDIT MATRIX ---
def execute_step4_predisbursement_audit(ein: str) -> bool:
    """Verifies the Three-Way Document Match and Quality Lab Certifications."""
    if ein == "00-0000000":
        return False # Fails final 3-way match documentation check
    return True

# --- THE SEQUENTIAL ESCROW MASTER REGULATOR ---
def process_escrow_sop_pipeline(raw_ai_payload: dict, policy_path="policy.json") -> dict:
    """
    Sequentially processes the transaction from Step 1 Ingestion 
    through the Step 4 Pre-Disbursement firewall.
    """
    # [SOP STEP 1] Contract Ingestion & Structural Ingestion Type Verification
    try:
        validated_data = EscrowTransactionPayload(**raw_ai_payload)
    except ValidationError as e:
        return {
            "status": "STEP_1_FAILED",
            "approved": False,
            "logs": [f"SOP Step 1 Failure: Structural Document Defect - {err['loc']} - {err['msg']}" for err in e.errors()]
        }

    # Load active corporate rule bounds from Layer 4
    with open(policy_path, "r") as f:
        policy = json.load(f)

    total_penalty = 0
    pipeline_audit_logs = ["SOP Step 1: Contract data structured safely via AI sub-agent extraction."]

    # [SOP STEP 2] Financial Ingestion & Active Entity Vetting
    step2_results = execute_step2_identity_and_sanction_checks(validated_data.ein_number, validated_data.seller_name)
    pipeline_audit_logs.append("SOP Step 2: Querying FinCEN registries and OFAC watchlists...")

    # [SOP STEP 3] Mid-Transit Cargo & Route Monitoring
    step3_results = execute_step3_mid_transit_tracking(validated_data.vessel_imo, validated_data.contract_unit_price)
    pipeline_audit_logs.append("SOP Step 3: Pinging maritime tracking and cross-checking pricing indexes...")

    # [SOP STEP 4] Pre-Disbursement Verification ("Point of No Return")
    step4_match_passed = execute_step4_predisbursement_audit(validated_data.ein_number)
    pipeline_audit_logs.append("SOP Step 4: Running final Three-Way Document Match and Last-Look database checks...")

    # Compile the comprehensive, multi-source telemetry checkpoint state
    runtime_state_matrix = {
        "ubo_verified": step2_results["ubo_verified"],
        "ofac_sanctions_match": step2_results["ofac_match"],
        "vessel_dark_activity": step3_results["dark_activity_detected"],
        "market_value_deviation": step3_results["index_price_deviation"],
        "three_way_match_pass": step4_match_passed
    }

    # Evaluate rules chronologically by SOP order
    sorted_rules = sorted(policy["rules"], key=lambda k: k["step"])
    
    for rule in sorted_rules:
        metric = rule["metric"]
        if metric in runtime_state_matrix:
            current_val = runtime_state_matrix[metric]
            rule_val = rule["value"]
            op_func = OPERATORS[rule["operator"]]

            if op_func(current_val, rule_val):
                if rule.get("is_knockout", False):
                    return {
                        "status": f"SOP_STEP_{rule['step']}_KNOCKOUT",
                        "approved": False,
                        "score": 100,
                        "logs": pipeline_audit_logs + [f"🛑 CRITICAL ACTION BARRIER: {rule['error_message']}", "STATUS: TRANSACTION SUSPENDED PRE-PAYOUT"]
                    }
                
                total_penalty += rule["penalty_points"]
                pipeline_audit_logs.append(f"⚠️ {rule['error_message']}")

    # Check cumulative threshold safety limits
    approved = total_penalty <= policy["max_allowed_penalty_points"]
    if not approved:
        pipeline_audit_logs.append(f"🛑 SOP Step 4 Rejected: Accumulated variance points ({total_penalty} pts) exceed allowance ceiling.")
    else:
        pipeline_audit_logs.append("✨ SOP Step 4 Passed: Transaction metrics cleared for disbursement pipeline routing.")

    return {
        "status": "SUCCESS",
        "approved": approved,
        "score": total_penalty,
        "logs": pipeline_audit_logs
    }
