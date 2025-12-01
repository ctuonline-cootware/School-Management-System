# app/routers/departments.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import Department as DepartmentModel
from app.schemas.generated_models import Department, DepartmentCreate, DepartmentUpdate

router = APIRouter()

# get a list of all departments (filtering can happen on the front end)
@router.get("/", response_model=list[Department], dependencies=[Depends(get_current_user)])
def list_departments(db: Session = Depends(get_db)):
    return db.query(DepartmentModel).all()

# get a specific department by ID - used to provide details for review or editing
@router.get("/{department_id}", response_model=Department, dependencies=[Depends(get_current_user)])
def get_department(department_id: int, db: Session = Depends(get_db)):
    obj = db.query(DepartmentModel).get(department_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return obj

# create a new department - restricted to the admin role
@router.post("/", response_model=Department, dependencies=[Depends(require_role("admin"))])
def create_department(payload: DepartmentCreate, db: Session = Depends(get_db)):
    obj = DepartmentModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing department - restricted to the admin role
@router.put("/{department_id}", response_model=Department, dependencies=[Depends(require_role("admin"))])
def update_department(department_id: int, payload: DepartmentUpdate, db: Session = Depends(get_db)):
    obj = db.query(DepartmentModel).get(department_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Assignment not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj