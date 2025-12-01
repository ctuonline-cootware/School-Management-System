# app/routers/faculty.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import Faculty as FacultyModel
from app.schemas.generated_models import Faculty, FacultyCreate, FacultyUpdate

router = APIRouter()

# get a list of all faculty (filtering can happen on the front end)
@router.get("/", response_model=list[Faculty], dependencies=[Depends(get_current_user)])
def list_faculty(db: Session = Depends(get_db)):
    return db.query(FacultyModel).all()

# get a specific faculty by ID - used to provide details for review or editing
@router.get("/{faculty_id}", response_model=Faculty, dependencies=[Depends(get_current_user)])
def get_faculty(faculty_id: int, db: Session = Depends(get_db)):
    obj = db.query(FacultyModel).get(faculty_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

# create a new faculty - restricted to the admin role
@router.post("/", response_model=Faculty, dependencies=[Depends(require_role("admin"))])
def create_faculty(payload: FacultyCreate, db: Session = Depends(get_db)):
    obj = FacultyModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing faculty - restricted to the admin role
@router.put("/{faculty_id}", response_model=Faculty, dependencies=[Depends(require_role("admin"))])
def update_faculty(faculty_id: int, payload: FacultyUpdate, db: Session = Depends(get_db)):
    obj = db.query(FacultyModel).get(faculty_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj