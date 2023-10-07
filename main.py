from fastapi import FastAPI
from web.v1 import hello as hello1
from web.v2 import hello as hello2
from web.endpoints import auth, user
from utils.database import engine
from utils.redis import redis_client
from fastapi.staticfiles import StaticFiles
from utils.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class MyPSQL:
    def __init__(self):
        self.database = {
            1 : dict(name="Jack", email="jack@gmail.com"),
            2 : dict(name="Joe", email="joe@gmail.com")
        }

    async def getUser(self, user_id:int) -> dict:
        return self.database.get(user_id, {})

    async def setUser(self, user_id:int, user_payload:dict) -> bool:
        if user_id in self.database:
            self.database[user_id].update(user_payload)
            return True
        return False

class MyRedis:
    def __init__(self):
        self.redis = {}  # Simulate a Redis-like in-memory database

    async def get(self, key: str) -> str:
        return self.redis.get(key, None)

    async def set(self, key: str, value: str) -> bool:
        self.redis[key] = value
        return True

    async def delete(self, key: str) -> bool:
        if key in self.redis:
            del self.redis[key]
            return True
        return False

    async def keys(self) -> list:
        return list(self.redis.keys())


# include v1 router
app.include_router(hello1.router)

# include v2 router
app.include_router(hello2.router)
