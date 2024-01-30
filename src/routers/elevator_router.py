from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.repository import DemandRepository, ElevatorRepository, FloorRepository
from src.routers.schemas.elevator_schema import ElevatorCreate, ElevatorResponse
from src.routers.schemas.demand_schema import DemandCreate, DemandResponse
from src.routers.schemas.floor_schema import FloorCreate, FloorResponse
from src.models import Demand, Elevator, Floor
from src.database import get_db


import logging
logger = logging.getLogger()

router = APIRouter(
    prefix="/elevator",
    tags=['Elevator']
)

def get_elevator_repository(db: Session = Depends(get_db)):
    return ElevatorRepository(db)

def get_floor_repository(db: Session = Depends(get_db)):
    return FloorRepository(db)

def get_demand_repository(db: Session = Depends(get_db)):
    return DemandRepository(db)

@router.post("/elevator/", response_model=ElevatorResponse)
def create_elevator(elevator: ElevatorCreate, repo: ElevatorRepository = Depends(get_elevator_repository)):
    elevator_model = Elevator(**elevator.dict())
    return repo.add(elevator_model)

@router.get("/elevator/{elevator_id}", response_model=ElevatorResponse)
def read_elevator(elevator_id: int, repo: ElevatorRepository = Depends(get_elevator_repository)):
    elevator = repo.get(Elevator, elevator_id)
    if elevator is None:
        raise HTTPException(status_code=404, detail="Elevator not found")
    return elevator