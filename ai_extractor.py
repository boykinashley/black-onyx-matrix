# ai_extractor.py
import json
import streamlit as st
from google import genai
from google.genai import types

# Access your free API key securely from Streamlit Cloud Secrets
GEMINI_API_KEY = st.secrets["gemini_key"]

# --- MASTER EXTRACTION PROMPT TEMPLATE ---
# Centralizing the prompt ensures both text and PDF extractions output identical keys
PROMPT_SCHEMA_INSTRUCTIONS = """
You are a specialized Trade Finance Compliance Extraction Sub-Agent.
Your ONLY job is to extract raw planned transaction metrics from the provided source document or text.
Do NOT calculate risk scores. Do NOT apply corporate policy rules.

Extract the following fields exactly as a JSON object with these precise keys:
- buyer_name (string)
- seller_name (string)
- ein_number (string format: XX-XXXXXXX)
- vessel_imo (string format: IMOXXXXXXX)
- hs_code (string representation of the commodity classification)
- contract_unit_price (float/number representing price per item unit)
- invoice_value (float/number representing the total gross transaction value)

Return ONLY valid JSON. Do not include any conversational text, markdown formatting, or code blocks.
"""

def extract_variables_from_pdf_with_gemini(uploaded_pdf_file) -> dict:
    """
    Ingests a raw PDF file from a Streamlit file uploader,
    passes it directly to Gemini 1.5 Flash, and extracts structured fields.
    """
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # 1. Read the uploaded PDF file straight into raw binary bytes
        pdf_bytes = uploaded_pdf_file.read()
        
        # 2. Package the binary bytes and send them alongside the extraction rules
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=[
                types.Part.from_bytes(
                    data=pdf_bytes,
                    mime_type="application/pdf"
                ),
                PROMPT_SCHEMA_INSTRUCTIONS
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.0 # Kept at absolute 0 to stop creative hallucinations
            ),
        )
        return json.loads(response.text)

    except Exception as e:
        return {"error": f"PDF API Ingestion Bypass: {str(e)}", **get_fallback_mock_data()}


def extract_variables_from_text_with_gemini(raw_contract_text: str) -> dict:
    """
    Ingests an ad-hoc unformatted text string or email draft from a text window,
    passes it to Gemini 1.5 Flash, and extracts identical structured fields.
    """
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # Pass the string payload directly to the model text channel
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=[PROMPT_SCHEMA_INSTRUCTIONS, f"SOURCE TEXT UNSTRUCTURED DATA:\n{raw_contract_text}"],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.0
            ),
        )
        return json.loads(response.text)

    except Exception as e:
        return {"error": f"Text API Ingestion Bypass: {str(e)}", **get_fallback_mock_data()}


def get_fallback_mock_data() -> dict:
    """Helper fallback dictionary matching your exact core_engine keys if keys or networks drop."""
    return {
        "buyer_name": "American Roast Co",
        "seller_name": "Global Coffee Traders Inc",
        "ein_number": "12-4455667",
        "vessel_imo": "IMO1234567",
        "hs_code": "0901",
        "contract_unit_price": 4.50,
        "invoice_value": 500000.0
    }

import pypdf
import io
from google import genai
from google.genai import types
from pydantic import BaseModel

# --- YOUR ORIGINAL Pydantic Contract Schema ---
class TradeContractSchema(BaseModel):
    extracted_hs_code: str
    contract_value_fob: float
    counterparty_country: str
    payment_terms: str
    risk_rubric_score: int
    rubric_compliance_notes: list[str]

def extract_variables_from_pdf_binary(uploaded_file, gemini_key: str) -> dict:
    """
    Your original text layer parsing mechanics transferred from app.py.
    """
    try:
        extracted_text = ""
        pdf_reader = pypdf.PdfReader(io.BytesIO(uploaded_file.getvalue()))
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
        
        if not extracted_text.strip():
            return {"error": "SYSTEM CRITICAL: Terminal read failed. PDF text layers blank."}

        client = genai.Client(api_key=gemini_key)
        prompt = f"Extract target HS Code, FOB asset value, country, payment structural bounds, and apply the strict risk rubric schema matrix:\n{extracted_text}"
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=TradeContractSchema,
                temperature=0.0
            ),
        )
        import json
        return json.loads(response.text)
    except Exception as e:
        return {"error": f"SYSTEM FAULT IN CONSOLE: {str(e)}"}
