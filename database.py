from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates/connects to a SQLite file called portfolio.db 
DATABASE_URL = "sqlite:///./portfolio.db"

# The engine is the actual connection to the database 
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SessionLocal is what we use to interact with or talk to the database 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

# Base is the foundation all our table models will inherit from
Base = declarative_base()