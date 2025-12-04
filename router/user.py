from fastapi import APIRouter,status,Depends,HTTPException
from .schemas import UserBase,UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("",status_code=status.HTTP_201_CREATED,response_model=UserDisplay)
def create_user(request:UserBase,db:Session = Depends(get_db)):
    user = db_user.create_user(db,request)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Couldn't Create a User")
    return user