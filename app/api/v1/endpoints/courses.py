# app/routers/assignment.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import Course as CourseModel
from app.schemas.generated_models import Course, CourseCreate, CourseUpdate

router = APIRouter()

# get a list of all courses (filtering can happen on the front end)
@router.get("/", response_model=list[Course], dependencies=[Depends(get_current_user)])
def list_courses(db: Session = Depends(get_db)):
    return db.query(CourseModel).all()

# get a specific course by ID - used to provide details for review or editing
@router.get("/{course_id}", response_model=Course, dependencies=[Depends(get_current_user)])
def get_course(course_id: int, db: Session = Depends(get_db)):
    obj = db.query(CourseModel).get(course_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

# create a new course - restricted to the admin role
@router.post("/", response_model=Course, dependencies=[Depends(require_role("admin"))])
def create_course(payload: CourseCreate, db: Session = Depends(get_db)):
    obj = CourseModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing course - restricted to the admin role
@router.put("/{course_id}", response_model=Course, dependencies=[Depends(require_role("admin"))])
def update_course(course_id: int, payload: CourseUpdate, db: Session = Depends(get_db)):
    obj = db.query(CourseModel).get(course_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj