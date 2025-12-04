from fastapi import APIRouter,status,Depends,HTTPException
from .schemas import PostBase,PostDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_post

router = APIRouter(
    prefix="/post",
    tags=["Post"]
)

image_url_types = ['absolute','relative']

@router.post("",status_code=status.HTTP_201_CREATED,response_model=PostDisplay)
def create_post(request: PostBase,db:Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,description="Not a relative or absolute image")
    post = db_post.create_post(request=request,db=db)
    if not post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Couldn't Create a User")
    return post

@router.get("",status_code=status.HTTP_200_OK,response_model=list[PostDisplay])
def get_post(db:Session):
    post = db_post.get_posts(db)
    return post