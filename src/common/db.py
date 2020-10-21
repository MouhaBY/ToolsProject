from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# use session_factory() to get a new Session
_Session_factory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(bind=engine)
    return _Session_factory()
