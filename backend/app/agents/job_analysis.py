from app.services.llm import get_llm


SYSTEM_PROMPT = """
You are a Job Description Analysis Agent.

Your job is to analyze a job description and identify:

1. Job title
2. Required technical skills
3. Preferred technical skills
4. Required experience
5. Education requirements
6. Certifications
7. Location
8. Employment type
9. Key responsibilities
10. Important eligibility requirements

Do not invent information that is not present in the job description.

Clearly distinguish between required and preferred requirements.
"""


def analyze_job(job_description: str) -> str:
    llm = get_llm()

    prompt = f"""
{SYSTEM_PROMPT}

Analyze the following job description:

--- JOB DESCRIPTION ---
{job_description}
--- END JOB DESCRIPTION ---

Return a clear structured analysis.
"""

    response = llm.invoke(prompt)

    return response.content