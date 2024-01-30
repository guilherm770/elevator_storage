from pydantic import BaseModel
from typing import Optional


class DemandCreate(BaseModel):
    from_floor: int
    to_floor: int

class DemandResponse(BaseModel):
    id: int
    from_floor: int
    to_floor: int
    timestamp: str
    status: str
