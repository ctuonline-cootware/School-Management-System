# app/routers/course_assignments.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import CourseAssignment as CourseAssignmentModel, Assignment as AssignmentModel
from app.schemas.generated_models import CourseAssignment, CourseAssignmentCreate, CourseAssignmentUpdate

router = APIRouter()

# get a list of all course_assignments (filtering can happen on the front end)
@router.get("/", response_model=list[CourseAssignment], dependencies=[Depends(get_current_user)])
def list_course_assignments(db: Session = Depends(get_db)):
    return db.query(CourseAssignmentModel).options(joinedload(CourseAssignmentModel.assignment)).all()

# get a list of all course_assignments by student
@router.get("/{student_id}", response_model=list[CourseAssignment], dependencies=[Depends(get_current_user)])
def list_course_assignments_by_student(student_id: int, db: Session = Depends(get_db)):
    return db.query(CourseAssignmentModel).options(joinedload(CourseAssignmentModel.assignment)).where(CourseAssignmentModel.student_id == student_id).all()

# get a specific course_assignment by ID - used to provide details for review or editing
@router.get("/{course_assignment_id}", response_model=CourseAssignment, dependencies=[Depends(get_current_user)])
def get_course_assignment(course_assignment_id: int, db: Session = Depends(get_db)):
    obj = db.query(CourseAssignmentModel).get(course_assignment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

# create a new course_assignment - restricted to the admin role
@router.post("/", response_model=CourseAssignment, dependencies=[Depends(require_role("admin", "faculty"))])
def create_course_assignment(payload: CourseAssignmentCreate, db: Session = Depends(get_db)):
    obj = CourseAssignmentModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing course_assignment - restricted to the admin role
@router.put("/{course_assignment_id}", response_model=CourseAssignment, dependencies=[Depends(require_role("admin", "faculty"))])
def update_course_assignment(course_assignment_id: int, payload: CourseAssignmentUpdate, db: Session = Depends(get_db)):
    obj = db.query(CourseAssignmentModel).get(course_assignment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj