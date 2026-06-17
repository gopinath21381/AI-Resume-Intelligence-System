import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def analyze_resume_with_gemini(resume_text):
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are an HR AI resume screening assistant.

Analyze this resume and give:
1. Candidate Summary
2. Recommended Role
3. Suitability Score out of 100
4. Strengths
5. Reason for selection

Resume:
{resume_text}
"""

    response = model.generate_content(prompt)
    return response.text