from fastapi import FastAPI, UploadFile, File
import shutil
import os
import re

from app.parser.resume_parser import extract_text_from_pdf
from app.parser.data_extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    extract_linkedin,
    extract_github
)
from app.database.insert_candidate import save_candidate
from app.ai_engine.gemini_ai import analyze_resume_with_gemini

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

required_skills = ["python", "machine learning", "html", "css", "git"]

def calculate_basic_score(skills):
    matched = 0
    for skill in required_skills:
        if skill in skills:
            matched += 1
    return int((matched / len(required_skills)) * 100)

@app.get("/")
def home():
    return {"message": "AI Resume Intelligence System Running"}

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    name = extract_name(resume_text)
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    skills = extract_skills(resume_text)
    linkedin = extract_linkedin(resume_text)
    github = extract_github(resume_text)

    basic_score = calculate_basic_score(skills)

    try:
        ai_analysis = analyze_resume_with_gemini(resume_text)
        ai_status = "AI analysis completed"
    except Exception as e:
        ai_analysis = "AI failed, basic skill score used instead"
        ai_status = str(e)

    db_message = save_candidate(
        full_name=name,
        email=email,
        phone=phone,
        skills=skills,
        resume_file=file.filename,
        linkedin=linkedin,
        github=github,
        suitability_score=basic_score
    )

    return {
        "message": "Resume uploaded, parsed, saved, and analyzed by AI",
        "database_message": db_message,
        "filename": file.filename,
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "linkedin": linkedin,
        "github": github,
        "basic_suitability_score": basic_score,
        "ai_status": ai_status,
        "ai_analysis": ai_analysis
    }
from sqlalchemy import text
from app.database.db_connection import engine

@app.get("/top-candidates/")
def top_candidates():

    query = text("""
        SELECT full_name,
               email,
               skills,
               suitability_score
        FROM candidates
        ORDER BY suitability_score DESC
        LIMIT 10
    """)

    with engine.connect() as connection:
        result = connection.execute(query)

        candidates = []

        for row in result:
            candidates.append({
                "name": row[0],
                "email": row[1],
                "skills": row[2],
                "score": row[3]
            })

    return candidates