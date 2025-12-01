# app/core/security.py
from datetime import datetime, timedelta, timezone
from typing import Optional, List, Dict, Any, Callable
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

def get_current_user(token: str = Depends(oauth2_scheme)) -> Dict[str, Any]:
    payload = decode_token(token)
    sub = payload.get("sub")

    if not sub:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload (missing sub)")

    return payload  # caller can inspect sub, roles, user_id, etc.


def require_role(*required_roles: str):
    if not required_roles:
        raise ValueError("At least one role must be specified")

    def dependency(current_user: dict = Depends(get_current_user)):
        # Support common claim names: roles, role, scope, permissions, etc.
        roles_claim = (
            current_user.get("roles") or
            current_user.get("role") or
            current_user.get("permissions") or
            current_user.get("scope", "").split()
        )

        if isinstance(roles_claim, str):
            user_roles = roles_claim.split()  # support space-separated
        else:
            user_roles = list(roles_claim or [])

        if not any(role in required_roles for role in user_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires role(s): {', '.join(required_roles)}. You have: {user_roles or 'none'}"
            )
        return current_user

    return dependency