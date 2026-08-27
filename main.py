from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
import auth


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
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db), current_user: str = Depends(auth.verify_token)):
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
    db: Session = Depends(get_db), current_user: str = Depends(auth.verify_token)
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
def delete_project(project_id: int, db: Session = Depends(get_db), current_user: str = Depends(auth.verify_token)):
    project = db.query(models.Project).filter(
        models.Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()
    return {"message": f"Project '{project.title}' deleted successfully"}

# ── AUTH ROUTES ───────────────────────────────────────

@app.post("/auth/register")
def register(user: schemas.UserRegister, db: Session = Depends(get_db)):
    # Check if username already exists
    existing = db.query(models.User).filter(
        models.User.username == user.username
    ).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    # Hash the password before storing
    new_user = models.User(
        username=user.username,
        email=user.email,
        password=auth.hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": f"Account created successfully for {user.username}",
        "username": user.username,
        "email": user.email
    }


@app.post("/auth/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # Find user by username
    user = db.query(models.User).filter(
        models.User.username == form_data.username
    ).first()
    # Verify user exists and password is correct
    if not user or not auth.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    # Create and return JWT token
    access_token = auth.create_access_token(
        data={"sub": user.username}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
        "message": "Login successful"
    }
    
# ── SKILLS CRUD ───────────────────────────────────────

@app.post("/skills")
def create_skill(
    skill: schemas.SkillCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    new_skill = models.Skill(
        category=skill.category,
        name=skill.name
    )
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


@app.put("/skills/{skill_id}")
def update_skill(
    skill_id: int,
    updates: schemas.SkillUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    skill = db.query(models.Skill).filter(
        models.Skill.id == skill_id
    ).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    if updates.category is not None:
        skill.category = updates.category
    if updates.name is not None:
        skill.name = updates.name
    db.commit()
    db.refresh(skill)
    return skill


@app.delete("/skills/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    skill = db.query(models.Skill).filter(
        models.Skill.id == skill_id
    ).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    db.delete(skill)
    db.commit()
    return {"message": f"Skill '{skill.name}' deleted successfully"}


# ── EDUCATION CRUD ────────────────────────────────────

@app.post("/education")
def create_education(
    edu: schemas.EducationCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    new_edu = models.Education(
        degree=edu.degree,
        institution=edu.institution,
        location=edu.location,
        year=edu.year,
        focus=edu.focus
    )
    db.add(new_edu)
    db.commit()
    db.refresh(new_edu)
    return new_edu


@app.put("/education/{edu_id}")
def update_education(
    edu_id: int,
    updates: schemas.EducationUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    edu = db.query(models.Education).filter(
        models.Education.id == edu_id
    ).first()
    if not edu:
        raise HTTPException(status_code=404, detail="Education record not found")
    if updates.degree is not None:
        edu.degree = updates.degree
    if updates.institution is not None:
        edu.institution = updates.institution
    if updates.location is not None:
        edu.location = updates.location
    if updates.year is not None:
        edu.year = updates.year
    if updates.focus is not None:
        edu.focus = updates.focus
    db.commit()
    db.refresh(edu)
    return edu


@app.delete("/education/{edu_id}")
def delete_education(
    edu_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    edu = db.query(models.Education).filter(
        models.Education.id == edu_id
    ).first()
    if not edu:
        raise HTTPException(status_code=404, detail="Education record not found")
    db.delete(edu)
    db.commit()
    return {"message": f"Education record '{edu.degree}' deleted successfully"}


# ── CERTIFICATIONS CRUD ───────────────────────────────

@app.post("/certifications")
def create_certification(
    cert: schemas.CertificationCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    new_cert = models.Certification(
        name=cert.name,
        issuer=cert.issuer,
        type=cert.type
    )
    db.add(new_cert)
    db.commit()
    db.refresh(new_cert)
    return new_cert


@app.put("/certifications/{cert_id}")
def update_certification(
    cert_id: int,
    updates: schemas.CertificationUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    cert = db.query(models.Certification).filter(
        models.Certification.id == cert_id
    ).first()
    if not cert:
        raise HTTPException(status_code=404, detail="Certification not found")
    if updates.name is not None:
        cert.name = updates.name
    if updates.issuer is not None:
        cert.issuer = updates.issuer
    if updates.type is not None:
        cert.type = updates.type
    db.commit()
    db.refresh(cert)
    return cert


@app.delete("/certifications/{cert_id}")
def delete_certification(
    cert_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    cert = db.query(models.Certification).filter(
        models.Certification.id == cert_id
    ).first()
    if not cert:
        raise HTTPException(status_code=404, detail="Certification not found")
    db.delete(cert)
    db.commit()
    return {"message": f"Certification '{cert.name}' deleted successfully"}