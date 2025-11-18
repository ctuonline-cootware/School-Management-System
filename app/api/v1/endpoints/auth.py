from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import create_access_token, get_password_hash
from app.core.config import settings
from app.db.session import get_db
from app.models.sqlalchemy_models import Users as UsersModel

router = APIRouter()

# replace with real credential check / DB lookup
def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    # query DB for user, verify password hash
    # return a dict/object like {"id": 1, "username": username, "roles": ["user"]}
    if username == "demo" and password == "demo":
        return {
            "id": 1, 
            "username": "demo", 
            "roles": ["admin"]
        }

    hashed_pasword = get_password_hash(password)
    obj = db.query(UsersModel).filter(UsersModel.username == username, UsersModel.password_hash == hashed_pasword).first()
    if obj is None:
        return None
    
    return {
        "id": obj.id,
        "username": obj.username,
        "roles": [role.role_name for role in obj.roles]  # assuming a relationship 'roles' exists
    }
    
    return None

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    token_data = {
        "sub": user["username"],
        "user_id": user["id"],
        "roles": user.get("roles", [])
    }

    access_token = create_access_token(token_data, expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}