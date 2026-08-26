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