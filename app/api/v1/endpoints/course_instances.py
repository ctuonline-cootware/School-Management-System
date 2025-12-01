# app/routers/course_instances.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import CourseInstance as CourseInstanceModel
from app.schemas.generated_models import CourseInstance, CourseInstanceCreate, CourseInstanceUpdate

router = APIRouter()

# get a list of all course_instances (filtering can happen on the front end)
@router.get("/", response_model=list[CourseInstance], dependencies=[Depends(get_current_user)])
def list_course_instances(db: Session = Depends(get_db)):
    return db.query(CourseInstanceModel).all()

# get a specific course_instance by ID - used to provide details for review or editing
@router.get("/{course_instance_id}", response_model=CourseInstance, dependencies=[Depends(get_current_user)])
def get_course_instance(course_instance_id: int, db: Session = Depends(get_db)):
    obj = db.query(CourseInstanceModel).get(course_instance_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

# create a new course_instance - restricted to the admin role
@router.post("/", response_model=CourseInstance, dependencies=[Depends(require_role("admin"))])
def create_course_instance(payload: CourseInstanceCreate, db: Session = Depends(get_db)):
    obj = CourseInstanceModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing course_instance - restricted to the admin role
@router.put("/{course_instance_id}", response_model=CourseInstance, dependencies=[Depends(require_role("admin"))])
def update_course_instance(course_instance_id: int, payload: CourseInstanceUpdate, db: Session = Depends(get_db)):
    obj = db.query(CourseInstanceModel).get(course_instance_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj