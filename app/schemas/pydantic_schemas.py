from pydantic import BaseModel, EmailStr, json
from datetime import datetime, date
from typing import Optional

class user(BaseModel):
    id : Optional[int] = None
    username : str
    email : EmailStr
    password : str
    role : str
    created_at : Optional[datetime] = None

class patient(BaseModel):
    id : str
    tenat_id : str
    mrn : str
    give_name : str
    dob : date
    gender : str
    phone : str
    email : str
    identifiers : dict | None
    consents : dict | None
    created_at : datetime | None

class get_user(BaseModel):
    email:EmailStr
    password : str