from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas


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
    
@app.post("/projects")
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    new_project = models.Project(
        title=project.title,
        description=project.description,
        tech_stack=project.tech_stack,
        category=project.category,
        live_url=project.live_url,
        github_url=project.github_url
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@app.put("/projects/{project_id}")
def update_project(
    project_id: int,
    updates: schemas.ProjectUpdate,
    db: Session = Depends(get_db)
):
    project = db.query(models.Project).filter(
        models.Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if updates.title is not None:
        project.title = updates.title
    if updates.description is not None:
        project.description = updates.description
    if updates.tech_stack is not None:
        project.tech_stack = updates.tech_stack
    if updates.category is not None:
        project.category = updates.category
    if updates.live_url is not None:
        project.live_url = updates.live_url
    if updates.github_url is not None:
        project.github_url = updates.github_url

    db.commit()
    db.refresh(project)
    return project

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(
        models.Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()
    return {"message": f"Project '{project.title}' deleted successfully"}