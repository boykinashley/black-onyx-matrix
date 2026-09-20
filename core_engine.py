# core_engine.py
import json
import operator
from pydantic import BaseModel, Field, ValidationError

# --- STEP 1: VALIDATION SCHEMA ---
class TradeFinancePayload(BaseModel):
    is_sanctioned_port: bool = Field(..., description="True if any port on the route is on a sanctions list")
    has_inspection_certificate: bool = Field(..., description="True if a third-party inspection document was provided")
    hs_code_risk_tier: int = Field(..., description="Risk ranking of the HS code ledger (1-5, where 5 is highest restriction)")
    vessel_compliance_score: int = Field(..., description="Carrier compliance or historical safety rating from 0-100")

OPERATORS = {
    "equals": operator.eq,
    "less_than": operator.lt,
    "greater_than": operator.gt
}

# --- STEP 2: THE MATHEMATICAL COMPONENT ---
def run_trade_compliance_engine(raw_ai_payload: dict, policy_path="policy.json") -> dict:
    """
    Pure Python math layer. Evaluates trade data against dynamic thresholds.
    """
    # 1. Enforce strict data types before any calculations run
    try:
        validated_data = TradeFinancePayload(**raw_ai_payload)
    except ValidationError as e:
        return {
            "status": "VALIDATION_ERROR",
            "approved": False,
            "score": 0,
            "logs": [f"Schema Mismatch: {err['loc'][0]} - {err['msg']}" for err in e.errors()]
        }

    # 2. Load policy variables
    with open(policy_path, "r") as f:
        policy = json.load(f)

    total_penalty = 0
    triggered_logs = []

    # Convert the validated Pydantic model into a workable dictionary
    data_dict = validated_data.model_dump()

    # 3. Dynamic evaluation loop
    for rule in policy["rules"]:
        metric = rule["metric"]
        if metric in data_dict:
            current_value = data_dict[metric]
            rule_value = rule["value"]
            op_func = OPERATORS[rule["operator"]]

            # Execute comparison mathematically
            if op_func(current_value, rule_value):
                # Handle Knockouts instantly
                if rule.get("is_knockout", False):
                    return {
                        "status": "SUCCESS",
                        "approved": False,
                        "score": 100,
                        "logs": [rule["error_message"], "VERDICT: IMMEDIATE DENIAL (Knockout Rule Triggered)"]
                    }
                
                # Accumulate linear penalty points
                total_penalty += rule["penalty_points"]
                triggered_logs.append(rule["error_message"])

    # 4. Final aggregation check
    approved = total_penalty <= policy["max_allowed_penalty_points"]
    
    if not approved:
        triggered_logs.append(f"VERDICT: REJECTED. Accumulated penalty ({total_penalty} pts) exceeds limit ({policy['max_allowed_penalty_points']} pts).")
    else:
        triggered_logs.append("VERDICT: APPROVED. Risk profile falls within acceptable lending parameters.")

    return {
        "status": "SUCCESS",
        "approved": approved,
        "score": total_penalty,
        "logs": triggered_logs
    }

