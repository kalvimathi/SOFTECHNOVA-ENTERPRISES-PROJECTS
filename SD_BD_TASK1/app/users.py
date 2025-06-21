from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, database, auth

router = APIRouter()
get_db = database.SessionLocal

@router.get("/me", response_model=schemas.UserOut)
def read_users_me(current_user: schemas.UserOut = Depends(auth.get_current_user)):
    return current_user
