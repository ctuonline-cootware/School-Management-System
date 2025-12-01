# app/routers/program_course_requirement.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import ProgramCourseRequirement as ProgramCourseRequirementModel
from app.schemas.generated_models import ProgramCourseRequirement, ProgramCourseRequirementCreate, ProgramCourseRequirementUpdate

router = APIRouter()

# get a list of all program_course_requirements (filtering can happen on the front end)
@router.get("/", response_model=list[ProgramCourseRequirement], dependencies=[Depends(get_current_user)])
def list_program_course_requirements(db: Session = Depends(get_db)):
    return db.query(ProgramCourseRequirementModel).all()

# get a specific program_course_requirement by ID - used to provide details for review or editing
@router.get("/{program_course_requirement_id}", response_model=ProgramCourseRequirement, dependencies=[Depends(get_current_user)])
def get_program_course_requirement(program_course_requirement_id: int, db: Session = Depends(get_db)):
    obj = db.query(ProgramCourseRequirementModel).get(program_course_requirement_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

# create a new program_course_requirement - restricted to the admin role
@router.post("/", response_model=ProgramCourseRequirement, dependencies=[Depends(require_role("admin"))])
def create_program_course_requirement(payload: ProgramCourseRequirementCreate, db: Session = Depends(get_db)):
    obj = ProgramCourseRequirementModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing program_course_requirement - restricted to the admin role
@router.put("/{program_course_requirement_id}", response_model=ProgramCourseRequirement, dependencies=[Depends(require_role("admin"))])
def update_program_course_requirement(program_course_requirement_id: int, payload: ProgramCourseRequirementUpdate, db: Session = Depends(get_db)):
    obj = db.query(ProgramCourseRequirementModel).get(program_course_requirement_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj