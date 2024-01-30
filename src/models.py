from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum, DateTime
from datetime import datetime
from enum import Enum

from src.database import Base


class ElevatorStatusEnum(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"


class Elevator(Base):
    __tablename__ = "elevators"

    id = Column(Integer, primary_key=True, index=True)
    current_floor = Column(Integer, nullable=False)
    resting_floor = Column(Integer, nullable=False)
    status = Column(
        SQLAlchemyEnum(
            ElevatorStatusEnum, 
            name="elevator_status"
        ),
        default=ElevatorStatusEnum.COMPLETED,
        nullable=False,
        index=True
    )


class Floor(Base):
    __tablename__ = "floors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)


class Demand(Base):
    __tablename__ = "demands"

    id = Column(Integer, primary_key=True, index=True)
    from_floor = Column(Integer, nullable=False)
    to_floor = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    status = Column(
            SQLAlchemyEnum(
                ElevatorStatusEnum, 
                name="elevator_status"
            ),
            default=ElevatorStatusEnum.COMPLETED,
            nullable=False,
            index=True
        )