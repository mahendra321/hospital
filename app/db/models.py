from sqlalchemy import Integer, Column,String,Float,Text,Date,DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID,JSONB,TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import base,get_db
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Patients(base):
    __tablename__ = "patients"
    id= Column(UUID(as_uuid=True),nullable=False,primary_key=True)
    tenant_id=Column(UUID(as_uuid=True),nullable=False)
    mrn=Column(String,nullable=False)
    given_name=Column(String,nullable=False)
    dob=Column(Date,nullable=True)
    gender=Column(String,nullable=True)
    phone=Column(String,nullable=True)
    email=Column(String,nullable=True)
    identifiers=Column(JSONB,nullable=True)
    consents=Column(JSONB,nullable=True)
    created_at=Column(TIMESTAMP,nullable=True)
        
    encounters = relationship("Encounter", back_populates="patient")


class User(base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String,nullable=True)
    password = Column(String,nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Encounter(base):
    __tablename__ = "encounters"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    encounter_type = Column(String(50), nullable=False)  # e.g., OPD, IPD, Emergency
    start_time = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    end_time = Column(DateTime, nullable=True)
    notes = Column(Text)

    patient = relationship("Patients", back_populates="encounters")
    