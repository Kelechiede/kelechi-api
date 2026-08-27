from pydantic import BaseModel
from typing import Optional

class ProjectCreate(BaseModel):
    title:          str
    description:    str
    tech_stack:     str
    category:       str
    live_url:       Optional[str] = "Coming_soon"
    github_url:     Optional[str] = "https://github.com/Kelechiede"
    

class ProjectUpdate(BaseModel):
    title:          Optional[str] = None
    description:    Optional[str] = None
    tech_stack:     Optional[str] = None
    category:       Optional[str] = None
    live_url:       Optional[str] = None
    github_url:     Optional[str] = None
    
class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    
class UserLogin(BaseModel):
    username: str
    password: str


class SkillCreate(BaseModel):
    category: str
    name:      str

class SkillUpdate(BaseModel):
    category: Optional[str] = None
    name:     Optional[str] = None


class EducationCreate(BaseModel):
    degree:      str
    institution: str
    location:    str
    year:        str
    focus:       str

class EducationUpdate(BaseModel):
    degree:      Optional[str] = None
    institution: Optional[str] = None
    location:    Optional[str] = None
    year:        Optional[str] = None
    focus:       Optional[str] = None


class CertificationCreate(BaseModel):
    name:   str
    issuer: str
    type:   str

class CertificationUpdate(BaseModel):
    name:   Optional[str] = None
    issuer: Optional[str] = None
    type:   Optional[str] = None
    
    