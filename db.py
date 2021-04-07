import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(os.environ['DATABASE_URL']))
session = scoped_session(Session)