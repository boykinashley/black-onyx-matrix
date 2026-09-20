# ai_extractor.py
import json
import streamlit as st
from google import genai
from google.genai import types

GEMINI_API_KEY = st.secrets["gemini_key"]

def extract_pdf_variables_with_gemini(uploaded_file) -> dict:
    """
    Connects to free Gemini 1.5 Flash to pull pre-shipment trade intent variables.
    """
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        file_bytes = uploaded_file.read()
        
        prompt = """
        You are a Pre-Shipment Compliance Data Extraction sub-agent. 
        Your ONLY job is to extract raw planned transaction metrics from this Pro Forma Invoice or Draft Letter of Credit. 
        Do not calculate risk scores. Extract the following fields exactly as strings, numbers, or booleans:
        - vendor_name (string)
        - ein_number (string format: XX-XXXXXXX)
        - nominated_vessel_imo (string format: IMOXXXXXXX)
        - hs_code_risk_tier (integer 1 to 5 based on commodity type)
        """
        
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=[
                types.Part.from_bytes(data=file_bytes, mime_type="application/pdf"),
                prompt
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.0
            ),
        )
        return json.loads(response.text)

    except Exception as e:
        return {
            "error": f"API Connection Bypass: {str(e)}",
            "vendor_name": "RiskCorp Logistics Limited",
            "ein_number": "99-9999999",
            "nominated_vessel_imo": "IMO9999999",
            "hs_code_risk_tier": 2
        }
