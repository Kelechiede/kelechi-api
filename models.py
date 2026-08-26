from sqlalchemy import Column, Integer, String, Text
from database import Base 

class Project(Base):
    __tablename__ = "projects"
    
    id          = Column(Integer, primary_key=True, index=True) 
    title       = Column(String(200), nullable=False) 
    description = Column(Text, nullable=False)
    tech_stack  = Column(String(500), nullable=False)
    category    = Column(String(100), nullable=False)
    live_url    = Column(String(500), default="coming_soon")
    github_url  = Column(String(500), default="https://github.com/kelechiede")
    

class Skill(Base):
    __tablename__ = "skills"
    
    id          = Column(Integer, primary_key=True, index=True)
    category    = Column(String(100), nullable=False)
    name        = Column(String(100), nullable=False)
    
    
class Education(Base):
    __tablename__ = "education"
    
    id          = Column(Integer, primary_key=True, index=True)
    degree      = Column(String(200), nullable=False)
    institution = Column(String(200), nullable=False)
    location    = Column(String(100), nullable=False)
    year        = Column(String(50),  nullable=False)
    focus       = Column(String(500), nullable=False)
    
    
class Certification(Base):
    __tablename__ = "certifications"
    
    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(200), nullable=False)
    issuer      = Column(String(200), nullable=False)
    type        = Column(String(100), nullable=False)
    
class User(Base):
    __tablename__ = "users"
    
    id          = Column(Integer, primary_key=True, index=True)
    username    = Column(String(100), unique=True, nullable=False)
    email       = Column(String(200), unique=True, nullable=False)
    password    = Column(String(500), nullable=False)
    
