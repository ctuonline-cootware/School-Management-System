# app/routers/job.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import Job as JobModel
from app.schemas.generated_models import Job, JobCreate, JobUpdate

router = APIRouter()

# get a list of all jobs (filtering can happen on the front end)
@router.get("/", response_model=list[Job], dependencies=[Depends(get_current_user)])
def list_jobs(db: Session = Depends(get_db)):
    return db.query(JobModel).all()

# get a specific job by ID - used to provide details for review or editing
@router.get("/{job_id}", response_model=Job, dependencies=[Depends(get_current_user)])
def get_job(job_id: int, db: Session = Depends(get_db)):
    obj = db.query(JobModel).get(job_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

# create a new job - restricted to the admin role
@router.post("/", response_model=Job, dependencies=[Depends(require_role("admin"))])
def create_job(payload: JobCreate, db: Session = Depends(get_db)):
    obj = JobModel(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# update an existing job - restricted to the admin role
@router.put("/{job_id}", response_model=Job, dependencies=[Depends(require_role("admin"))])
def update_job(job_id: int, payload: JobUpdate, db: Session = Depends(get_db)):
    obj = db.query(JobModel).get(job_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj