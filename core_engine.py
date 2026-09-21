# core_engine.py
import json
import operator
from pydantic import BaseModel, Field, ValidationError

# --- PIPELINE SCHEMAS ---
class EscrowTransactionPayload(BaseModel):
    buyer_name: str = Field(..., description="Legal name of buying entity")
    seller_name: str = Field(..., description="Legal name of selling entity")
    ein_number: str = Field(..., description="Corporate 9-digit tax identifier")
    vessel_imo: str = Field(..., description="7-digit maritime registration tracking identifier")
    hs_code: str = Field(..., description="Harmonized Tariff Schedule classification index")
    contract_unit_price: float = Field(..., description="Stated price per commodity unit in contract")
    invoice_value: float = Field(..., description="Total contract value in USD")

OPERATORS = {
    "equals": operator.eq,
    "not_equals": operator.ne,
    "greater_than": operator.gt,
    "less_than": operator.lt
}

# --- EXTERNAL REGISTRY SIMULATIONS ---
def execute_step2_identity_and_sanction_checks(ein: str) -> dict:
    """Queries FinCEN registries and OFAC screening watchlists."""
    if ein == "00-0000000":
        return {"ubo_verified": False, "ofac_match": False}
    if ein == "99-9999999":
        return {"ubo_verified": True, "ofac_match": True}
    return {"ubo_verified": True, "ofac_match": False}

def execute_step3_mid_transit_tracking(vessel_imo: str) -> dict:
    """Queries Windward Maritime AI tracking layers and market pricing index APIs."""
    if vessel_imo == "IMO9999999":
        return {"dark_activity_detected": True, "index_price_deviation": 25.0}
    return {"dark_activity_detected": False, "index_price_deviation": 4.5}

def execute_step4_predisbursement_audit(ein: str) -> bool:
    """Verifies the Three-Way Document Match and Quality Lab Certifications."""
    if ein == "00-0000000":
        return False
    return True

# --- UNDERWRITING FORMULA CORE ---
def calculate_credit_underwriting(hs_code: str, invoice_value: float, vessel_dark: bool) -> dict:
    """
    Evaluates tariff exposure, operational risk, and asset liquidity 
    to calculate advance rates and maximum capital outlay.
    """
    score = 0
    covenants = []
    
    # 1. Tariff & Margin Drag Evaluation based on HS Code Risk
    if hs_code == "8542": # Electronics / Dual Use
        base_duty = 5.0
        section_301 = 25.0 # High Tariff
        liquidity_class = "Moderate"
        has_pga_flag = True
        pga_list = ["BIS"]
    elif hs_code == "8479": # Heavy Machinery
        base_duty = 3.5
        section_301 = 0.0
        liquidity_class = "Low"
        has_pga_flag = False
        pga_list = []
    else: # Default 0901 Coffee / Clean Track
        base_duty = 0.0
        section_301 = 0.0
        liquidity_class = "High"
        has_pga_flag = True
        pga_list = ["FDA", "USDA"]

    total_tariff_exposure = base_duty + section_301
    if total_tariff_exposure > 20.0:
        score += 40
        covenants.append("💰 **Duty Escrow Required:** High tariff exposure detected. Pre-fund duty cash buffer.")
    elif total_tariff_exposure > 5.0:
        score += 20
    else:
        score += 5

    # 2. Operational / Regulatory Delay Evaluation (PGA Flagger)
    if has_pga_flag:
        score += 35
        covenants.append(f"⏳ **PGA Hold Mitigation:** Goods subject to {', '.join(pga_list)} oversight.")
    else:
        score += 10

    # 3. Collateral Marketability Evaluation
    if liquidity_class == "High":
        score += 5
        base_advance = 0.85
    elif liquidity_class == "Moderate":
        score += 20
        base_advance = 0.75
    else:
        score += 45
        base_advance = 0.55
        covenants.append("📉 **Alternative Recourse:** Low collateral liquidity. Require parent guarantee.")

    # Inject logistics risk from live middleware tracking
    if vessel_dark:
        score += 20
        covenants.append("🚢 **Logistics Premium:** Active dark fleet alert. Advance rate penalized by 5%.")

    # 4. Final Risk Tier Mapping
    normalized_score = int((score / 140) * 100) # Normalized across max possible score
    if normalized_score <= 35:
        tier = "🟢 Low Risk Profile"
        final_advance_rate = base_advance
    elif normalized_score <= 65:
        tier = "🟡 Moderate Risk Profile"
        final_advance_rate = base_advance - 0.05
    else:
        tier = "🔴 High Risk Profile"
        final_advance_rate = base_advance - 0.15

    max_capital_outlay = invoice_value * final_advance_rate

    return {
        "underwriting_score": normalized_score,
        "risk_tier": tier,
        "advance_rate": final_advance_rate,
        "max_capital_outlay": max_capital_outlay,
        "covenants": covenants
    }

# --- THE SEQUENTIAL ESCROW MASTER REGULATOR ---
def process_escrow_sop_pipeline(raw_ai_payload: dict, policy_path="policy.json") -> dict:
    """
    Sequentially processes compliance constraints and executes underwriting logic.
    """
    # [SOP STEP 1] Structural Parameter Validation Firewall
    try:
        validated_data = EscrowTransactionPayload(**raw_ai_payload)
    except ValidationError as e:
        return {
            "status": "STEP_1_FAILED",
            "approved": False,
            "logs": [f"SOP Step 1 Failure: Structural Defect - {err['loc']} - {err['msg']}" for err in e.errors()]
        }

    # Load policy metrics from Layer 4
    with open(policy_path, "r") as f:
        policy = json.load(f)

    total_penalty = 0
    pipeline_audit_logs = ["SOP Step 1: Contract data structured safely via AI sub-agent extraction."]

    # [SOP STEP 2] Entity Vetting (LexisNexis/OFAC)
    step2_results = execute_step2_identity_and_sanction_checks(validated_data.ein_number)
    pipeline_audit_logs.append("SOP Step 2: Querying FinCEN registries and OFAC watchlists...")

    # [SOP STEP 3] Mid-Transit Cargo Monitoring (Windward)
    step3_results = execute_step3_mid_transit_tracking(validated_data.vessel_imo)
    pipeline_audit_logs.append("SOP Step 3: Pinging maritime telemetry tracking networks...")

    # [SOP STEP 4] Pre-Disbursement Verification
    step4_match_passed = execute_step4_predisbursement_audit(validated_data.ein_number)
    pipeline_audit_logs.append("SOP Step 4: Running final Three-Way Document Match balances...")

    # Build verification metrics ledger mapping
    runtime_state_matrix = {
        "ubo_verified": step2_results["ubo_verified"],
        "ofac_sanctions_match": step2_results["ofac_match"],
        "vessel_dark_activity": step3_results["dark_activity_detected"],
        "market_value_deviation": step3_results["index_price_deviation"],
        "three_way_match_pass": step4_match_passed
    }

    # Process Compliance Rules Chronologically
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
                        "underwriting": {},
                        "logs": pipeline_audit_logs + [f"🛑 CRITICAL ACTION BARRIER: {rule['error_message']}", "STATUS: TRANSACTION TERMINATED BY MIDDLEWARE GATEWAY"]
                    }
                total_penalty += rule["penalty_points"]
                pipeline_audit_logs.append(f"⚠️ {rule['error_message']}")

    compliance_approved = total_penalty <= policy["max_allowed_penalty_points"]
    
    # Run Underwriting Calculations if the transaction is clear of compliance barriers
    underwriting_results = calculate_credit_underwriting(
        validated_data.hs_code, 
        validated_data.invoice_value, 
        runtime_state_matrix["vessel_dark_activity"]
    )
    
    if not compliance_approved:
        pipeline_audit_logs.append(f"🛑 SOP Step 4 Rejected: Combined risk points ({total_penalty} pts) exceed compliance allowance.")
    else:
        pipeline_audit_logs.append("✨ SOP Step 4 Passed: Transaction metrics cleared for disbursement parameters.")

    return {
        "status": "SUCCESS",
        "approved": compliance_approved,
        "score": total_penalty,
        "underwriting": underwriting_results,
        "logs": pipeline_audit_logs
    }
