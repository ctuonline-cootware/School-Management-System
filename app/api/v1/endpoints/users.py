# app/routers/job.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user, get_password_hash, require_role
from app.db.session import get_db
from app.models.sqlalchemy_models import Users as UserModel, Roles as RoleModel, Student as StudentModel, Faculty as FacultyModel
from app.schemas.generated_models import Users, UsersCreate, UsersUpdate

router = APIRouter()

# get a list of all jobs (filtering can happen on the front end)
@router.get("/", response_model=list[Users], dependencies=[Depends(get_current_user)])
def list_Users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()

# get a specific job by ID - used to provide details for review or editing
@router.get("/{job_id}", response_model=Users, dependencies=[Depends(get_current_user)])
def get_user(job_id: int, db: Session = Depends(get_db)):
    obj = db.query(UserModel).get(job_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

# # create a new job - restricted to the admin user
# @router.post("/", response_model=Users, dependencies=[Depends(require_role("admin"))])
# def create_user(payload: UsersCreate, db: Session = Depends(get_db)):
#     data = payload.model_dump()
#     raw_password = data.pop("password")
#     roles = data.pop("roles", [])
#     hashed_password = get_password_hash(raw_password)

#     obj = UserModel(**data)
#     obj.password_hash = hashed_password

#    # Look up roles by name (or ID)
#     roles = db.query(RoleModel).filter(RoleModel.id.in_(roles)).all()
    
#     if len(roles) != len(payload.roles):
#         raise HTTPException(status_code=400, detail="One or more roles not found")

#     obj.roles = roles

#     db.add(obj)
#     db.commit()
#     db.refresh(obj)
#     return obj

@router.post("/", response_model=Users, dependencies=[Depends(require_role("admin"))])
def create_user(payload: UsersCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    raw_password = data.pop("password")
    requested_role_ids = data.pop("roles", [])

    username = data.get("username")  # this should be an email, e.g. "ada.lovelace@school.edu"

    if not username or "@" not in username:
        raise HTTPException(
            status_code=400,
            detail="Username must be a valid email address"
        )

    # Check if this email exists in Student OR Faculty
    email_found = (
        db.query(StudentModel).filter(StudentModel.email_address == username).first() is not None
        or db.query(FacultyModel).filter(FacultyModel.email_address == username).first() is not None
    )

    if not email_found:
        raise HTTPException(
            status_code=400,
            detail="Cannot create user: email not found in Student or Faculty records"
        )

    # Check for duplicate username (in case user already exists)
    if db.query(UserModel).filter(UserModel.username == username).first():
        raise HTTPException(
            status_code=400,
            detail="User with this username already exists"
        )

    # Hash password
    hashed_password = get_password_hash(raw_password)

    # Create the UserModel instance
    new_user = UserModel(**data, password_hash=hashed_password)

    # Attach roles (by ID)
    if requested_role_ids:
        roles = db.query(RoleModel).filter(RoleModel.id.in_(requested_role_ids)).all()
        if len(roles) != len(requested_role_ids):
            raise HTTPException(status_code=400, detail="One or more roles not found")
        new_user.roles = roles

    # Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# update an existing job - restricted to the admin user
@router.put("/{user_id}", response_model=Users, dependencies=[Depends(get_current_user)])
def update_job(user_id: int, payload: UsersUpdate, db: Session = Depends(get_db)):
    obj = db.query(UserModel).get(user_id)
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in payload.model_dump(exclude_unset=True).items():
        if (key == "password"):
            hash = get_password_hash(value)
            setattr(obj, "password_hash", hash)
        elif (key == "roles"):
            roles = db.query(RoleModel).filter(RoleModel.id.in_(value)).all()
            
            if len(roles) != len(value):
                raise HTTPException(status_code=400, detail="One or more roles not found")
            
            obj.roles = roles
        else:
            setattr(obj, key, value)

    db.commit()
    db.refresh(obj)
    return obj