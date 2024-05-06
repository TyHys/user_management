from builtins import Exception, dict, list, str
import uuid
from fastapi import Depends, HTTPException, Header, Cookie, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import Database
from app.utils.template_manager import TemplateManager
from app.services.email_service import EmailService
from app.services.jwt_service import decode_token
from settings.config import Settings
from sqlalchemy.exc import SQLAlchemyError

def get_settings() -> Settings:
    """Return application settings."""
    return Settings()

def get_email_service() -> EmailService:
    template_manager = TemplateManager()
    return EmailService(template_manager=template_manager)

async def get_db() -> AsyncSession:
    """Dependency that provides a database session for each request."""
    async_session_factory = Database.get_session_factory()
    async with async_session_factory() as session:
        try:
            yield session
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database error: " + str(e))

#Need to add an OAuth token for the U
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    connection_error = HTTPException(
                                                status_code=401,
                                                detail="Could not validate request",
                                                headers={"WWW-Authenticate": "Bearer"},
                                            )
    payload = decode_token(token)
    if payload is None:
        raise connection_error
    user_email: str = payload.get("sub")
    user_role: str = payload.get("role")
    if user_email is None or user_role is None:
        raise connection_error
    return {"user_email": user_email, "role": user_role}

def require_role(role: str):
    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user["role"] not in role:
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return current_user
    return role_checker


