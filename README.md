# Kelechukwu Ede — Portfolio API

![FastAPI](https://img.shields.io/badge/FastAPI-0.136-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange)
![JWT](https://img.shields.io/badge/Auth-JWT-red)
![Render](https://img.shields.io/badge/Hosted-Render-purple)

A public REST API serving portfolio data for recruiters and developers.
Built with FastAPI, SQLAlchemy ORM, SQLite and JWT authentication.

---

## 🌐 Live Demo

| URL | Description |
|-----|-------------|
| [API Docs (Swagger)](https://kelechi-api.onrender.com/docs) | Interactive API documentation |
| [API Root](https://kelechi-api.onrender.com) | Welcome message and endpoints list |
| [Portfolio Website](https://kelechiede.dev) | Personal portfolio site |

---

## 🚀 Features

- Full CRUD operations across all four resources
- JWT Bearer token authentication — POST, PUT and DELETE are protected
- Public GET routes for recruiter access without authentication
- Auto-generated Swagger UI documentation at `/docs`
- SQLAlchemy ORM with SQLite database
- Bcrypt password hashing — passwords never stored as plain text
- Auto-deployment from GitHub via Render

---

## 📡 API Endpoints

### Public (no token required)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message and endpoint list |
| GET | `/projects` | All portfolio projects |
| GET | `/skills` | Skills grouped by category |
| GET | `/education` | Education history |
| GET | `/certifications` | Professional certifications |

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Create admin account |
| POST | `/auth/login` | Login and receive JWT token |

### Protected (JWT token required)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/projects` | Add a new project |
| PUT | `/projects/{id}` | Update a project |
| DELETE | `/projects/{id}` | Delete a project |
| POST | `/skills` | Add a new skill |
| PUT | `/skills/{id}` | Update a skill |
| DELETE | `/skills/{id}` | Delete a skill |
| POST | `/education` | Add education record |
| PUT | `/education/{id}` | Update education record |
| DELETE | `/education/{id}` | Delete education record |
| POST | `/certifications` | Add a certification |
| PUT | `/certifications/{id}` | Update a certification |
| DELETE | `/certifications/{id}` | Delete a certification |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | FastAPI 0.136 |
| Language | Python 3.13 |
| Database | SQLite via SQLAlchemy ORM |
| Authentication | JWT (python-jose + passlib bcrypt) |
| Server | Uvicorn |
| Hosting | Render (free tier) |

---

## 🏃 Run Locally

```bash
# Clone the repository
git clone https://github.com/Kelechiede/kelechi-api.git
cd kelechi-api

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Seed the database
python seed.py

# Start the server
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to explore the API locally.

---

## 📁 Project Structure

kelechi-api/
├── main.py # FastAPI routes and application
├── database.py # SQLite connection and session management
├── models.py # SQLAlchemy database models
├── schemas.py # Pydantic validation schemas
├── auth.py # JWT authentication and password hashing
├── seed.py # Database seeding script
├── requirements.txt # Python dependencies
└── render.yaml # Render deployment configuration


---

## 👨‍💻 Developer

**Kelechukwu Innocent Ede**
- 🌐 Portfolio: [kelechiede.dev](https://kelechiede.dev)
- 💼 GitHub: [github.com/Kelechiede](https://github.com/Kelechiede)
- ✉️ Primary Email: kelechukwuede@gmail.com
- ✉️ Secondary Email: info@kelechiededata.org
- 🎓 MSc Software Engineering — Memorial University of Newfoundland
- 🎓 MSc Data Science — Oslo Metropolitan University