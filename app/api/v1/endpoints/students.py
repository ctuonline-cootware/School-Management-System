# app/routers/student.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import Student as StudentModel
from app.schemas.generated_models import Student, StudentCreate, StudentUpdate

router = APIRouter()

# get a list of all students (filtering can happen on the front end)
@router.get("/", response_model=list[Student], dependencies=[Depends(get_current_user)])
def list_students(db: Session = Depends(get_db)):
    #return db.query(StudentModel).all()

    return db.query(StudentModel).options(joinedload(StudentModel.course_instances), 
                                          joinedload(StudentModel.program)).all()

# get a specific student by ID - used to provide details for review or editing
@router.get("/{student_id}", response_model=Student, dependencies=[Depends(get_current_user)])
def get_student(student_id: int, db: Session = Depends(get_db)):
    obj = db.query(StudentModel).get(student_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

# create a new student - restricted to the admin role
@router.post("/", response_model=Student, dependencies=[Depends(require_role("admin"))])
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):
    obj = StudentModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing student - restricted to the admin role
@router.put("/{student_id}", response_model=Student, dependencies=[Depends(require_role("admin"))])
def update_student(student_id: int, payload: StudentUpdate, db: Session = Depends(get_db)):
    obj = db.query(StudentModel).get(student_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj