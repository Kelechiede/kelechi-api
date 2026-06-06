from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kelechukwu Ede — Portfolio API",
    description="Public API serving portfolio data for recruiters and developers",
    version="1.0.0"
)

# ── Dependency ─────────────────────────────────────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ── Routes ─────────────────────────────────────────────
@app.get("/")
def root():
    return {
        "message": "Welcome to Kelechukwu's Portfolio API",
        "developer": "Kelechukwu Innocent Ede",
        "endpoints": ["/projects", "/skills", "/education", "/certifications"]
    }

@app.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    return [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "tech_stack": p.tech_stack.split(", "),
            "category": p.category,
            "live_url": p.live_url,
            "github_url": p.github_url
        }
        for p in projects
    ]

@app.get("/skills")
def get_skills(db: Session = Depends(get_db)):
    skills = db.query(models.Skill).all()
    result = {}
    for skill in skills:
        if skill.category not in result:
            result[skill.category] = []
        result[skill.category].append(skill.name)
    return result

@app.get("/education")
def get_education(db: Session = Depends(get_db)):
    education = db.query(models.Education).all()
    return [
        {
            "degree": e.degree,
            "institution": e.institution,
            "location": e.location,
            "year": e.year,
            "focus": e.focus
        }
        for e in education
    ]

@app.get("/certifications")
def get_certifications(db: Session = Depends(get_db)):
    certs = db.query(models.Certification).all()
    return [
        {
            "name": c.name,
            "issuer": c.issuer,
            "type": c.type
        }
        for c in certs
    ]