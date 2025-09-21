import re

def extract_skills(jd_text):
    # Simple keyword extraction (can be expanded with spaCy or SkillNER)
    skills = re.findall(r'\b[A-Za-z]+\b', jd_text.lower())
    return set(skills)
