from sqlalchemy import Column, Integer, String
from utils.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    auth_token = Column(String, unique=True, index=True)
    name = Column(String)

    def __init__(self, auth_token: str, name: str):
        self.auth_token = auth_token
        self.name = name
