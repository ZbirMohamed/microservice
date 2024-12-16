from typing import Optional
from pydantic import BaseModel, Field , constr
from datetime import date
from enum import Enum

#### enumeration

class HealthStatus(str,Enum):
    healthy = "healthy"
    unhealthy = "unhealthy"

class MetaData(BaseModel):
    # for now we'll go with health only
    health:HealthStatus
    #region:str ## we suppose that maybe you'll have servers linked to multiple region or cities or whatever

class CreateService(BaseModel):
    service_name:str = Field(min_length=4) 
    address: int = constr(regex=r'^https:[a-zA-Z0-9_]+$')
    metadata:HealthStatus
