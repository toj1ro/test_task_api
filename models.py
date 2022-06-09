from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from db import Base


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String)
    uuid = Column(UUID(as_uuid=True))
