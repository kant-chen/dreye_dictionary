import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

current_path = os.path.dirname(__file__)
db_path = os.path.join(current_path, "dict.db")
engine = create_engine(f"sqlite:///{db_path}", echo=False)


def get_session():
    session = None
    try:
        session = Session(engine)
        yield session
    finally:
        if session:
            session.close()
