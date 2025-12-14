# app/routers/faculty.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
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

@router.get("/{faculty_id}/classes")
def get_faculty_classes(faculty_id: int, db: Session = Depends(get_db)):
    faculty = (
        db.query(FacultyModel)
        .options(joinedload(FacultyModel.course_instance))  # eager load courses
        .filter(FacultyModel.faculty_id == faculty_id)
        .first()
    )

    if not faculty:
        return {"error": "Faculty not found"}

    return {
        "faculty_id": faculty.faculty_id,
        "name": f"{faculty.first_name} {faculty.last_name}",
        "email": faculty.email_address,
        "department_id": faculty.department_id,
        "job_id": faculty.job_id,
        "courses": [
            {"course_instance_id": ci.instance_id, "course_name": ci.course.name}
            for ci in faculty.course_instance
        ]
    }

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