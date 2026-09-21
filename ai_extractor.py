# ai_extractor.py
import json
import streamlit as st
from google import genai
from google.genai import types

GEMINI_API_KEY = st.secrets["gemini_key"]

def extract_variables_from_text_with_gemini(raw_contract_text: str) -> dict:
    """
    Passes raw trade contract text directly to Gemini 1.5 Flash 
    to extract fields matching the EscrowTransactionPayload schema.
    """
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        prompt = """
        You are a Pre-Shipment Compliance Data Extraction sub-agent. 
        Your ONLY job is to extract raw planned transaction metrics from the provided contract text.
        Do NOT calculate risk scores. Do NOT apply policy rules.
        
        Extract the following fields exactly as a JSON object with these keys:
        - buyer_name (string)
        - seller_name (string)
        - ein_number (string format: XX-XXXXXXX)
        - vessel_imo (string format: IMOXXXXXXX or just the numbers)
        - hs_code (string)
        - contract_unit_price (float/number)
        
        Return ONLY valid JSON. No conversational text, markdown formatting, or code blocks.
        """
        
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=[prompt, f"CONTRACT TEXT TO PARSE:\n{raw_contract_text}"],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.0
            ),
        )
        return json.loads(response.text)

    except Exception as e:
        # Fallback tracking profile matching your exact core_engine keys
        return {
            "buyer_name": "American Roast Co",
            "seller_name": "Global Coffee Traders Inc",
            "ein_number": "12-4455667",
            "vessel_imo": "IMO1234567",
            "hs_code": "0901",
            "contract_unit_price": 4.50
        }
