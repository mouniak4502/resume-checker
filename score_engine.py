from fuzzywuzzy import fuzz

def calculate_score(resume_text, jd_text, jd_skills):
    resume_text = resume_text.lower()
    matches = sum(1 for skill in jd_skills if skill in resume_text)
    total = len(jd_skills)
    hard_score = (matches / total * 100) if total > 0 else 0

    # Soft score using fuzzy match
    soft_score = fuzz.partial_ratio(resume_text, jd_text) / 2
    final_score = int((hard_score * 0.6) + (soft_score * 0.4))
    return final_score

def verdict(score):
    if score >= 70:
        return "✅ High Fit"
    elif score >= 40:
        return "⚠️ Medium Fit"
    else:
        return "❌ Low Fit"
