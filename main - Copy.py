from fastapi import FastAPI

app = FastAPI(
    title="Kelechukwu Ede - Portfolio API",
    description="Public API serving portfolio data for recruiters and developers",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Kelechukwu's Portfolio API",
        "developer": "Kelechukwu Innocent Ede",
        "endpoints": ["/projects", "/skills", "/education", "/certifications"]
        }

@app.get("/projects")
def get_projects():
    return [
        {
            "id": 1,
            "title": "VLC Research Simulation",
            "description": "Interactive simulation of Visible Light Communication systems — BER vs SNR curves and modulation scheme comparisons",
            "tech_stack": ["Python", "FastAPI", "Plotly", "NumPy"],
            "category": "Research",
            "live_url": "coming_soon",
            "github_url": "https://github.com/Kelechiede"
        },
        {
            "id": 2,
            "title": "Canadian Real Estate Visualiser",
            "description": "Animated choropleth maps of Canadian housing market trends by province using D3.js and Plotly",
            "tech_stack": ["Python", "Plotly", "D3.js", "pandas"],
            "category": "Data Visualisation",
            "live_url": "coming_soon",
            "github_url": "https://github.com/Kelechiede"
        },
        {
            "id": 3,
            "title": "Clinic Management System",
            "description": "Full-stack clinic MVP with patient registration, appointment management and REST API with JWT auth",
            "tech_stack": ["FastAPI", "SQLite", "Python", "REST API"],
            "category": "Full Stack",
            "live_url": "coming_soon",
            "github_url": "https://github.com/Kelechiede"
        },
        {
            "id": 4,
            "title": "Sudoku Solver CLI",
            "description": "Constraint propagation solver using the MRV heuristic — solves any valid Sudoku from the command line",
            "tech_stack": ["Python", "Constraint propagation", "MRV heuristic"],
            "category": "Algorithms",
            "live_url": "coming_soon",
            "github_url": "https://github.com/Kelechiede"
        }
    ]


@app.get("/skills")
def get_skills():
    return {
        "languages": ["Python", "JavaScript", "SQL", "TypeScript", "HTML", "CSS", "Bash"],
        "data_analytics": ["Power BI", "Tableau", "pandas", "Excel", "DAX", "Data storytelling"],
        "frameworks": ["FastAPI", "React", "Next.js", "Plotly", "D3.js", "scikit-learn"],
        "databases": ["PostgreSQL", "SQLite", "MySQL", "SQLAlchemy"],
        "cloud_and_tools": ["Git", "GitHub", "Docker", "Vercel", "Render", "Linux"],
        "research_areas": ["Visible Light Communications", "Digital Communications", "Cloud Computing", "ML pipelines"]
    }


@app.get("/education")
def get_education():
    return [
        {
            "degree": "MSc Software Engineering",
            "institution": "Memorial University of Newfoundland",
            "location": "Canada",
            "year": "2024 - Present",
            "focus": "Digital Communications, VLC research, Software Design"
        },
        {
            "degree": "MSc Data Science",
            "institution": "Oslo Metropolitan University",
            "location": "Norway",
            "year": "Completed 2023",
            "focus": "Machine Learning, Statistical Modelling, Data Visualisation"
        },
        {
            "degree": "BSc Computer Science",
            "institution": "Benson Idahosa University",
            "location": "Benin City, Nigeria",
            "year": "Graduated 2018",
            "focus": "Software development, Algorithms, Systems"
        }
    ]


@app.get("/certifications")
def get_certifications():
    return [
        {
            "name": "Oracle Certified — Data Analytics",
            "issuer": "Oracle Corporation",
            "type": "Professional Certification"
        },
        {
            "name": "IBM Certified — Data Analytics",
            "issuer": "IBM",
            "type": "Professional Certification"
        }
    ]
    