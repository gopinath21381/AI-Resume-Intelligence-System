from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from app.database.db_connection import engine

def save_candidate(full_name, email, phone, skills,
                   resume_file, linkedin, github,
                   suitability_score):

    skills_text = ", ".join(skills)

    query = text("""
        INSERT INTO candidates
        (full_name, email, phone, skills,
         resume_file, linkedin, github,
         suitability_score)
        VALUES
        (:full_name, :email, :phone, :skills,
         :resume_file, :linkedin, :github,
         :suitability_score)
    """)

    try:
        with engine.connect() as connection:
            connection.execute(query, {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "skills": skills_text,
                "resume_file": resume_file,
                "linkedin": linkedin,
                "github": github,
                "suitability_score": suitability_score
            })
            connection.commit()

        return "Candidate saved successfully"

    except IntegrityError:
        return "Duplicate candidate: email already exists"