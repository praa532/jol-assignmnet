from fastapi import APIRouter, Depends, Header,HTTPException
from utils.database import SessionLocal
from utils.redis import redis
import uuid
from passlib.context import CryptContext
from models import User
from utils.database import SessionLocal
import jwt
from datetime import datetime, timedelta


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_username(username):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    return user

router = APIRouter()

@router.post("/login/")
def login(username: str, password: str):
    user = get_user_by_username(username)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create a JSON Web Token (JWT) for authentication
    access_token_expires = timedelta(minutes=30)
    access_token_data = {
        "sub": user.username,
        "exp": datetime.utcnow() + access_token_expires,
    }
    access_token = jwt.encode(access_token_data, "your-secret-key", algorithm="HS256")

    return {"access_token": access_token, "token_type": "bearer"}
