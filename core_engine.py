# core_engine.py
import json
import operator
from pydantic import BaseModel, Field, ValidationError

# --- STEP 1: PRE-SHIPMENT TRANSACTION SCHEMA ---
class PreShipmentPayload(BaseModel):
    vendor_name: str = Field(..., description="Target vendor company name listed on contract")
    ein_number: str = Field(..., description="Corporate identity tax ID number")
    nominated_vessel_imo: str = Field(..., description="The planned maritime container vessel assignment number")
    hs_code_risk_tier: int = Field(..., description="Tariff restriction level of intended commodities")

OPERATORS = {
    "equals": operator.eq,
    "not_equals": operator.ne,
    "greater_than": operator.gt
}

# --- STEP 2: SIMULATED THIRD-PARTY REGISTRY VERIFICATION FEEDS ---
def fetch_lexisnexis_pre_shipment_status(ein: str, name: str) -> dict:
    """Mock integration for LexisNexis KYB registry search."""
    if ein == "00-0000000":
        return {"status": "SHELF_COMPANY_ALERT", "watchlist": False}
    if ein == "99-9999999" or "RiskCorp" in name:
        return {"status": "ACTIVE_ENTITY", "watchlist": True}
    return {"status": "VERIFIED_ACTIVE_ENTITY", "watchlist": False}

def fetch_windward_pre_shipment_vessel_risk(imo: str) -> dict:
    """Mock integration for Windward Maritime AI vessel profile checks."""
    if imo == "IMO9999999":
        return {"deceptive_practice_flag": True, "safety_rating": 22}
    return {"deceptive_practice_flag": False, "safety_rating": 95}

# --- STEP 3: CORE EVALUATION SYSTEM ---
def run_pre_shipment_compliance_engine(raw_ai_payload: dict, policy_path="policy.json") -> dict:
    """
    Validates data, checks external API registries, and runs threshold compliance math.
    """
    # 1. Enforce type-checking validation using our schema
    try:
        validated_data = PreShipmentPayload(**raw_ai_payload)
    except ValidationError as e:
        return {
            "status": "VALIDATION_ERROR",
            "approved": False,
            "logs": [f"Malformed Element: {err['loc']} - {err['msg']}" for err in e.errors()]
        }

    # 2. Query external truth sources before calculating rules
    lexis_record = fetch_lexisnexis_pre_shipment_status(validated_data.ein_number, validated_data.vendor_name)
    windward_record = fetch_windward_pre_shipment_vessel_risk(validated_data.nominated_vessel_imo)

    # 3. Ingest compliance policy settings from Layer 4
    with open(policy_path, "r") as f:
        policy = json.load(f)

    total_penalty_points = 0
    generated_audit_logs = []

    # Map our incoming variables and API records to our evaluation keys
    evaluation_map = {
        "corporate_registry_status": lexis_record["status"],
        "is_entity_sanctioned": lexis_record["watchlist"],
        "is_vessel_sanctioned": windward_record["deceptive_practice_flag"],
        "hs_code_risk_tier": validated_data.hs_code_risk_tier
    }

    # 4. Math processing loop
    for rule in policy["rules"]:
        metric = rule["metric"]
        if metric in evaluation_map:
            current_value = evaluation_map[metric]
            rule_value = rule["value"]
            op_func = OPERATORS[rule["operator"]]

            if op_func(current_value, rule_value):
                # Enforce immediate knockout rejections
                if rule.get("is_knockout", False):
                    return {
                        "status": "SUCCESS",
                        "approved": False,
                        "score": 100,
                        "lexis_status": lexis_record["status"],
                        "windward_flag": windward_record["deceptive_practice_flag"],
                        "logs": [
                            f"🛑 CRITICAL BARRIER OVERRIDE: {rule['error_message']}",
                            "VERDICT: CONTRACT CANCELLED PRE-FUNDING (Zero Capital Exposure Enforced)"
                        ]
                    }
                
                total_penalty_points += rule["penalty_points"]
                generated_audit_logs.append(rule["error_message"])

    # 5. Aggregate final risk metric scoring
    approved = total_penalty_points <= policy["max_allowed_penalty_points"]
    if not approved:
        generated_audit_logs.append(f"VERDICT: FINANCING REJECTED. Risks accumulated ({total_penalty_points} pts) exceed ceiling limit.")
    else:
        generated_audit_logs.append("VERDICT: CONTRACT SIGNING APPROVED. Risk vectors clear acceptable guidelines.")

    return {
        "status": "SUCCESS",
        "approved": approved,
        "score": total_penalty_points,
        "lexis_status": lexis_record["status"],
        "windward_flag": windward_record["deceptive_practice_flag"],
        "logs": generated_audit_logs
    }
