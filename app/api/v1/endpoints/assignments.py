# app/routers/assignment.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.db.session import get_db
from app.models.sqlalchemy_models import Assignment as AssignmentModel
from app.schemas.generated_models import Assignment, AssignmentCreate, AssignmentUpdate

router = APIRouter()

@router.get("/", response_model=list[Assignment], dependencies=[Depends(get_current_user)])
def list_assignments(db: Session = Depends(get_db)):
    return db.query(AssignmentModel).all()

@router.get("/{assignment_id}", response_model=Assignment)
def get_assignment(assignment_id: int, db: Session = Depends(get_db)):
    obj = db.query(AssignmentModel).get(assignment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return obj

@router.post("/", response_model=Assignment)
def create_assignment(payload: AssignmentCreate, db: Session = Depends(get_db)):
    obj = AssignmentModel(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.put("/{assignment_id}", response_model=Assignment)
def update_assignment(assignment_id: int, payload: AssignmentUpdate, db: Session = Depends(get_db)):
    obj = db.query(AssignmentModel).get(assignment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Assignment not found")
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj