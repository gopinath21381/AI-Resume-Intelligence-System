import re

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'(\+91[\s-]?)?[6-9]\d{9}', text)
    return match.group(0) if match else None

def extract_name(text):
    lines = text.split("\n")
    for line in lines:
        if len(line.strip()) > 2:
            return line.strip()
    return None

def extract_skills(text):
    skills_list = [
        "python", "java", "c", "c++", "html", "css",
        "javascript", "sql", "mysql", "machine learning",
        "data science", "fastapi", "django", "flask",
        "excel", "power bi", "git", "github"
    ]

    found_skills = []
    lower_text = text.lower()

    for skill in skills_list:
        if skill in lower_text:
            found_skills.append(skill)

    return found_skills

def extract_linkedin(text):
    match = re.search(r'https?://(?:www\.)?linkedin\.com/[^\s]+', text)
    return match.group(0) if match else None

def extract_github(text):
    match = re.search(r'https?://(?:www\.)?github\.com/[^\s]+', text)
    return match.group(0) if match else None