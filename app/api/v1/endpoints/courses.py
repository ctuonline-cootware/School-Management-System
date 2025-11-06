# app/routers/assignment.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.item import Course as CourseModel
from app.schemas.generated_models import Course, CourseCreate, CourseUpdate

router = APIRouter()

@router.get("/", response_model=list[Course])
def list_courses(db: Session = Depends(get_db)):
    return db.query(CourseModel).all()

@router.get("/{course_id}", response_model=Course)
def get_course(course_id: int, db: Session = Depends(get_db)):
    obj = db.query(CourseModel).get(course_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

@router.post("/", response_model=Course)
def create_course(payload: CourseCreate, db: Session = Depends(get_db)):
    obj = CourseModel(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.put("/{course_id}", response_model=Course)
def update_course(course_id: int, payload: CourseUpdate, db: Session = Depends(get_db)):
    obj = db.query(CourseModel).get(course_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj