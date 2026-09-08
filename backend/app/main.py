from fastapi import FastAPI
from pydantic import BaseModel

from app.agents.job_analysis import analyze_job


app = FastAPI(
    title="AI Job Agent",
    version="0.1.0",
)


class JobRequest(BaseModel):
    job_description: str


@app.get("/")
def root():
    return {
        "message": "AI Job Agent is running"
    }


@app.post("/analyze-job")
def analyze_job_endpoint(request: JobRequest):
    result = analyze_job(request.job_description)

    return {
        "analysis": result
    }