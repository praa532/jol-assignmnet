from fastapi import APIRouter, Depends, Header,HTTPException
from utils.database import SessionLocal
from utils.redis import redis_client
from models import User

router = APIRouter()

@router.post("/setName/")
def set_user_name(new_name: str, auth_token: str = Header(None)):
    # Check authentication using the auth_token and Redis cache
    if not redis_client.exists(auth_token):
        return {"message": "Authentication failed"}

    # Fetch the user record from the database based on auth_token
    db = SessionLocal()
    user = db.query(User).filter(User.auth_token == auth_token).first()
    if not user:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    try:
        # Update the user's name
        user.name = new_name

        # Commit the changes to the database
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update user name")

    db.close()

    return {"message": "User name updated successfully"}

@router.get("/getName/")
def get_user_name(auth_token: str = Header(None)):
    # Check authentication using the auth_token and Redis cache
    if not redis_client.exists(auth_token):
        return {"message": "Authentication failed"}

    # Fetch the user's name from the database based on auth_token
    db = SessionLocal()
    user = db.query(User).filter(User.auth_token == auth_token).first()
    db.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user_name": user.name}
