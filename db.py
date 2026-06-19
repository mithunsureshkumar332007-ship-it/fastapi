from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker,declarative_base;
from dotenv import load_dotenv;
import os;

load_dotenv()
DB_URL=os.getenv("DB_URL")
engine  =create_engine(DB_URL)
sessionin = sessionmaker(bind=engine,autoflush=False)
base=declarative_base()
