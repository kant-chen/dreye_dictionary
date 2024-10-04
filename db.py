import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
current_path = os.getcwd()
db_path = os.path.join(current_path, "dict.db")
engine = create_engine(f"sqlite:///{db_path}", echo=True)


def get_session():
    session = None
    try:
        session = Session(engine)
        yield session
    finally:
        if session:
            session.close()
