# app/routers/assignments.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import Assignment as AssignmentModel
from app.schemas.generated_models import Assignment, AssignmentCreate, AssignmentUpdate

router = APIRouter()

# get a list of all assignments (filtering can happen on the front end)
@router.get("/", response_model=list[Assignment], dependencies=[Depends(get_current_user)])
def list_assignments(db: Session = Depends(get_db)):
    return db.query(AssignmentModel).all()

# get a specific assignment by ID - used to provide details for review or editing
@router.get("/{assignment_id}", response_model=Assignment, dependencies=[Depends(get_current_user)])
def get_assignment(assignment_id: int, db: Session = Depends(get_db)):
    obj = db.query(AssignmentModel).get(assignment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return obj

# create a new assignment - restricted to the admin role
@router.post("/", response_model=Assignment, dependencies=[Depends(require_role("admin"))])
def create_assignment(payload: AssignmentCreate, db: Session = Depends(get_db)):
    obj = AssignmentModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing assignment - restricted to the admin role
@router.put("/{assignment_id}", response_model=Assignment, dependencies=[Depends(require_role("admin"))])
def update_assignment(assignment_id: int, payload: AssignmentUpdate, db: Session = Depends(get_db)):
    obj = db.query(AssignmentModel).get(assignment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Assignment not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj