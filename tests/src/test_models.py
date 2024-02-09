import pytest
from sqlalchemy.orm import Session, sessionmaker
from src.models import Elevator, Floor, Demand
from src.database import Base, engine
from src.database import get_db
from src.config import settings
from datetime import datetime
from src.models import ElevatorStatusEnum, DemandStatusEnum


SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URI

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_create_elevator(session: Session):
    elevator_data = {
        "current_floor": 1,
        "resting_floor": 5,
        "status": ElevatorStatusEnum.VACANT,
    }
    elevator = Elevator(**elevator_data)
    session.add(elevator)
    session.commit()
    session.refresh(elevator)
    assert elevator.id is not None
    assert elevator.current_floor == elevator_data["current_floor"]
    assert elevator.resting_floor == elevator_data["resting_floor"]
    assert elevator.status == elevator_data["status"]


def test_create_floor(session: Session):
    floor_data = {"name": "Ground Floor"}
    floor = Floor(**floor_data)
    session.add(floor)
    session.commit()
    session.refresh(floor)
    assert floor.id is not None
    assert floor.name == floor_data["name"]


def test_create_demand(session: Session):
    demand_data = {
        "from_floor": 2,
        "to_floor": 8,
        "status": DemandStatusEnum.PENDING,
    }
    demand = Demand(**demand_data)
    session.add(demand)
    session.commit()
    session.refresh(demand)
    assert demand.id is not None
    assert demand.from_floor == demand_data["from_floor"]
    assert demand.to_floor == demand_data["to_floor"]
    assert demand.status == demand_data["status"]
    assert isinstance(demand.created_at, datetime)
