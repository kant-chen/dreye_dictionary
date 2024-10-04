from sqlalchemy.orm import declarative_base, declared_attr
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    String,
    Text,
    event,

)
from sqlalchemy import Column, DateTime, text
from sqlalchemy.sql import func

class CustomBase:
    """
    Abstract base class model.

    Abstract base class model provides self updating ``created_at`` and
    ``updated_at`` fields.
    """

    @declared_attr
    def __tablename__(cls):
        """Tablename in lower case."""
        return cls.__name__.lower()

    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        server_default=text("NOW()::timestamp"),
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        server_default=text("NOW()::timestamp"),
        onupdate=func.now(),
    )


DefaultBase = declarative_base()
Base = declarative_base(cls=CustomBase)

class Vocabulary(Base):
    __tablename__ = "vocabulary"
    __table_args__ = (PrimaryKeyConstraint("name"),)
    name = Column(String, primary_key=True, nullable=False)
    pronunciation = Column(String, nullable=True)
    content_zh = Column(String, nullable=True)
    content_en = Column(String, nullable=True)
    variant = Column(String, nullable=True)