# ai_extractor.py
import json
import streamlit as st
from google import genai
from google.genai import types

# Access your secret key securely from Streamlit Cloud
GEMINI_API_KEY = st.secrets["gemini_key"]

def extract_variables_from_text_with_gemini(raw_contract_text: str) -> dict:
    """
    Passes raw trade contract text directly to Gemini 1.5 Flash 
    to extract compliance variables into a structured JSON dictionary.
    """
    try:
        # 1. Initialize the official Google GenAI client
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # 2. Define the explicit prompt framing the AI's boundaries
        prompt = """
        You are an elite Pre-Shipment Compliance Data Extraction sub-agent. 
        Your ONLY job is to extract raw planned transaction metrics from the provided contract text.
        Do NOT calculate risk scores. Do NOT apply policy rules.
        
        Extract the following fields exactly as a JSON object with these keys:
        - vendor_name (string, extract the full legal name)
        - ein_number (string format: XX-XXXXXXX)
        - nominated_vessel_imo (string format: IMOXXXXXXX)
        - hs_code_risk_tier (integer 1 to 5 based on commodity type described)
        
        Return ONLY valid JSON. No conversational text, markdown formatting, or code blocks.
        """
        
        # 3. Call the free Gemini 1.5 Flash model
        # Instead of sending PDF bytes, we send the prompt and the raw contract text string
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=[prompt, f"CONTRACT TEXT TO PARSE:\n{raw_contract_text}"],
            config=types.GenerateContentConfig(
                response_mime_type="application/json", # Forces a structured JSON response object
                temperature=0.0 # Kept at 0.0 to prevent creative hallucinations
            ),
        )
        
        # 4. Convert the AI's string response into a real Python dictionary
        extracted_data = json.loads(response.text)
        return extracted_data

    except Exception as e:
        # Fallback dictionary if the API key is unconfigured or a connection error occurs
        return {
            "error": f"API Connection Bypass: {str(e)}",
            "vendor_name": "RiskCorp Logistics Limited",
            "ein_number": "99-9999999",
            "nominated_vessel_imo": "IMO9999999",
            "hs_code_risk_tier": 2
        }
