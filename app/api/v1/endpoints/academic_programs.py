# app/routers/academic_programs.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import AcademicProgram as AcademicProgramModel
from app.schemas.generated_models import AcademicProgram, AcademicProgramCreate, AcademicProgramUpdate

router = APIRouter()

# get a list of all academic programs (filtering can happen on the front end)
@router.get("/", response_model=list[AcademicProgram], dependencies=[Depends(get_current_user)])
def list_academic_programs(db: Session = Depends(get_db)):
    return db.query(AcademicProgramModel).all()

# get a specific academic program by ID - used to provide details for review or editing
@router.get("/{academic_program_id}", response_model=AcademicProgram, dependencies=[Depends(get_current_user)])
def get_academic_program(academic_program_id: int, db: Session = Depends(get_db)):
    obj = db.query(AcademicProgramModel).get(academic_program_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

# create a new academic program - restricted to the admin role
@router.post("/", response_model=AcademicProgram, dependencies=[Depends(require_role("admin"))])
def create_academic_program(payload: AcademicProgramCreate, db: Session = Depends(get_db)):
    obj = AcademicProgramModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing academic program - restricted to the admin role
@router.put("/{academic_program_id}", response_model=AcademicProgram, dependencies=[Depends(require_role("admin"))])
def update_academic_program(academic_program_id: int, payload: AcademicProgramUpdate, db: Session = Depends(get_db)):
    obj = db.query(AcademicProgramModel).get(academic_program_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj