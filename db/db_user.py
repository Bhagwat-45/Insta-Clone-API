from router.schemas import UserBase
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from db.models import DbUser
from db.hashing import Hash

def create_user(db:Session,request:UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db:Session):
    user = db.query(DbUser).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There are no user's present!!")
    return user
