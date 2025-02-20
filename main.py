from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SesssionLocal,engine
import models,schemas,services

app = FastAPI()

def get_db():
    db = SesssionLocal()
    try:
        yield db
    finally:
        db.close()

@app.port("/api/v1/leave-requests", response_model=schemas.LeaveRequestResponces)
def create_leaves_request(leave_request:schemas.LeaveRequestCreate, db:Session=Depends(get_db)):
    try:
        return services.create_leave_request(db,leave_request)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    
@app.get("/api/v1/leave-requests/{employee_id}", response_model=list[schemas.LeaveRequestResponces])
def get_leave_requests(employee_id:str,db:Session=Depends(get_db)):
    return services.get_employee_leaves(db,employee_id)