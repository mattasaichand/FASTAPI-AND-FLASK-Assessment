from pydantic import BaseModel, Field
from datetime import date
from typing import List

class LeaveRequestCreate(BaseModel):
    employee_id : str = Field(..., example="EMP001")
    start_date: date
    end_date: date
    leave_type: Field(..., regex="ANNUAL")
    reason: Field(..., min_length=10)

class LeaveResponse(BaseModel):
    id:int
    status: str
    working_days:int

    class Config:
        from_attributes = True
        