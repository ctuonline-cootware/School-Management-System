from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import create_access_token, get_password_hash, verify_password
from app.core.config import settings
from app.db.session import get_db
from app.models.sqlalchemy_models import Users as UsersModel

router = APIRouter()

# replace with real credential check / DB lookup
def authenticate_user(username: str, password: str, db: Session):
    # query DB for user, verify password hash
    # return a dict/object like {"id": 1, "username": username, "roles": ["user"]}
    if username == "demo" and password == "demo":
        return {
            "id": 1, 
            "username": "demo", 
            "roles": ["admin"]
        }
    
    # validate we have a user with that name
    user = db.query(UsersModel).filter(UsersModel.username == username).first()
    if user is None:
        return None
    
    # confirm we were given the correct password
    if not verify_password(password, user.password_hash):
        return None

    # return user info if validated
    return {
        "id": user.id,
        "username": user.username,
        "roles": [role.name for role in user.roles]  # assuming a relationship 'roles' exists
    }

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    token_data = {
        "sub": user["username"],
        "user_id": user["id"],
        "roles": user.get("roles", [])
    }

    access_token = create_access_token(token_data, expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}