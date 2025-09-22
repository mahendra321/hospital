from fastapi import FastAPI, Depends,HTTPException,status
from sqlalchemy.orm import Session
from .schemas import pydantic_schemas
from .hash_pwd import hashing,verification
from .core.database import get_db
from .db import models
from .gen_uuid import new_uuid
from datetime import datetime
from contextlib import asynccontextmanager
from app.core.cache import init_cache
from fastapi_cache.decorator import cache

@asynccontextmanager
async def lifespan_cache(app:FastAPI):
    await init_cache()
    yield

app = FastAPI(lifespan=lifespan_cache)



@app.get("/ping")
async def ping():
    return {"status":"ok"}

@app.get("/home")
def yoyo():
    return " welcome  back to fastapi"
@app.get("/test")
@cache(60)
async def testing():
    
    return "yoyo this a test!!!!!!!!!!!!!"
@app.post("/user_reg")
@cache(expire=60)
async def user_signup(data : pydantic_schemas.user, db: Session=Depends(get_db)):
    qry_user = db.query(models.User).filter(models.User.email == data.email).first()
    if qry_user:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Aleady user found")
    hash_pwd = hashing(data.password)
    uuid = new_uuid()
    data.password = hash_pwd
    data.id =uuid
    data.created_at = datetime.now()

    new_user = models.User(**data.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user")
@cache(expire=60)
async def get_user(user_data: pydantic_schemas.get_user, db:Session=Depends(get_db)):
    from_db_user = db.query(models.User).filter(models.User.email==user_data.email).first()
    if from_db_user:
        cred_check = verification(user_data.password,from_db_user.password)
        if cred_check:
            return from_db_user
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="bad credentials")
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="user not registered")