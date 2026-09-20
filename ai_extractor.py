# ai_extractor.py
import json
import streamlit as st # Import streamlit to access secret variables
from google import genai
from google.genai import types

# Streamlit Cloud looks for a secret called "gemini_key" automatically
GEMINI_API_KEY = st.secrets["gemini_key"]

def extract_pdf_variables_with_gemini(uploaded_file) -> dict:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        file_bytes = uploaded_file.read()
        
        prompt = """
        You are an AI data extraction sub-agent. Your ONLY job is to extract raw metrics 
        from this document. Do not calculate scores. Do not apply policy. 
        Extract the following fields exactly as numbers or booleans:
        - credit_score (integer)
        - tax_liens (integer)
        - years_in_business (integer)
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
            "error": f"API Error: {str(e)}",
            "credit_score": 550, 
            "tax_liens": 1, 
            "years_in_business": 1
        }

