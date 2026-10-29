import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# For local MySQL, set DATABASE_URL in your environment.
# Example: mysql+pymysql://username:password@localhost/fastapi_project
# The default SQLite database makes the project runnable without MySQL.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./course_catalog.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
