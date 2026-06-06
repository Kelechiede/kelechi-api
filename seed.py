from database import SessionLocal, engine
import models

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# ── PROJECTS ──────────────────────────────────────────
projects = [
    models.Project(
        title="VLC Research Simulation",
        description="Interactive simulation of Visible Light Communication systems — BER vs SNR curves and modulation scheme comparisons",
        tech_stack="Python, FastAPI, Plotly, NumPy",
        category="Research",
        live_url="coming_soon",
        github_url="https://github.com/Kelechiede"
    ),
    models.Project(
        title="Canadian Real Estate Visualiser",
        description="Animated choropleth maps of Canadian housing market trends by province using D3.js and Plotly",
        tech_stack="Python, Plotly, D3.js, pandas",
        category="Data Visualisation",
        live_url="coming_soon",
        github_url="https://github.com/Kelechiede"
    ),
    models.Project(
        title="Clinic Management System",
        description="Full-stack clinic MVP with patient registration, appointment management and REST API with JWT auth",
        tech_stack="FastAPI, SQLite, Python, REST API",
        category="Full Stack",
        live_url="coming_soon",
        github_url="https://github.com/Kelechiede"
    ),
    models.Project(
        title="Sudoku Solver CLI",
        description="Constraint propagation solver using the MRV heuristic — solves any valid Sudoku from the command line",
        tech_stack="Python, Constraint propagation, MRV heuristic",
        category="Algorithms",
        live_url="coming_soon",
        github_url="https://github.com/Kelechiede"
    ),
    models.Project(
        title="ARIMA Cold-Start Predictor",
        description="ML-enhanced predictive pre-warming for serverless functions using ARIMA time-series forecasting",
        tech_stack="Python, ARIMA, scikit-learn, Cloud",
        category="Machine Learning",
        live_url="coming_soon",
        github_url="https://github.com/Kelechiede"
    ),
    models.Project(
        title="Public CV + Project Showcase API",
        description="A live JSON REST API serving portfolio data — projects, skills, education and certifications for recruiters",
        tech_stack="FastAPI, SQLite, SQLAlchemy, Python",
        category="Full Stack",
        live_url="https://kelechi-api.onrender.com",
        github_url="https://github.com/Kelechiede"
    ),
]

# ── SKILLS ────────────────────────────────────────────
skills = [
    models.Skill(category="Languages", name="Python"),
    models.Skill(category="Languages", name="JavaScript"),
    models.Skill(category="Languages", name="SQL"),
    models.Skill(category="Languages", name="TypeScript"),
    models.Skill(category="Languages", name="HTML/CSS"),
    models.Skill(category="Data Analytics", name="Power BI"),
    models.Skill(category="Data Analytics", name="Tableau"),
    models.Skill(category="Data Analytics", name="pandas"),
    models.Skill(category="Data Analytics", name="DAX"),
    models.Skill(category="Frameworks", name="FastAPI"),
    models.Skill(category="Frameworks", name="React"),
    models.Skill(category="Frameworks", name="Plotly"),
    models.Skill(category="Frameworks", name="D3.js"),
    models.Skill(category="Databases", name="PostgreSQL"),
    models.Skill(category="Databases", name="SQLite"),
    models.Skill(category="Databases", name="MySQL"),
    models.Skill(category="Databases", name="SQLAlchemy"),
    models.Skill(category="Cloud & Tools", name="Git"),
    models.Skill(category="Cloud & Tools", name="Docker"),
    models.Skill(category="Cloud & Tools", name="Vercel"),
    models.Skill(category="Cloud & Tools", name="Render"),
]

# ── EDUCATION ─────────────────────────────────────────
education = [
    models.Education(
        degree="MSc Software Engineering",
        institution="Memorial University of Newfoundland",
        location="Canada",
        year="2024 - Present",
        focus="Digital Communications, VLC research, Software Design"
    ),
    models.Education(
        degree="MSc Data Science",
        institution="Oslo Metropolitan University",
        location="Norway",
        year="Completed 2023",
        focus="Machine Learning, Statistical Modelling, Data Visualisation"
    ),
    models.Education(
        degree="BSc Computer Science",
        institution="Benson Idahosa University",
        location="Benin City, Nigeria",
        year="Graduated 2018",
        focus="Software development, Algorithms, Systems"
    ),
]

# ── CERTIFICATIONS ────────────────────────────────────
certifications = [
    models.Certification(
        name="Oracle Certified — Data Analytics",
        issuer="Oracle Corporation",
        type="Professional Certification"
    ),
    models.Certification(
        name="IBM Certified — Data Analytics",
        issuer="IBM",
        type="Professional Certification"
    ),
]

# Add everything to the database
db.add_all(projects)
db.add_all(skills)
db.add_all(education)
db.add_all(certifications)
db.commit()
db.close()

print("✅ Database created and seeded successfully!")
print(f"   Projects:       {len(projects)}")
print(f"   Skills:         {len(skills)}")
print(f"   Education:      {len(education)}")
print(f"   Certifications: {len(certifications)}")