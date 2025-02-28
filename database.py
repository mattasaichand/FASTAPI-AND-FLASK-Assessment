from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ""

engine = create_engine(DATABASE_URL,connect_args={"check_sample":False})
SessionLocal = sessionmaker(autocommit=False,autoflush = False,bind=engine)
Base = declarative_base()