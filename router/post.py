from fastapi import APIRouter,status,Depends,HTTPException,File,UploadFile
from .schemas import PostBase,PostDisplay,UserAuth
from sqlalchemy.orm import Session
from db.database import get_db
from auth.oauth2 import get_current_user
from db import db_post
import random
import string
import shutil

router = APIRouter(
    prefix="/post",
    tags=["Post"]
)

image_url_types = ['absolute','relative']

@router.post("",status_code=status.HTTP_201_CREATED,response_model=PostDisplay)
def create_post(request: PostBase,db:Session = Depends(get_db),current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,description="Not a relative or absolute image")
    post = db_post.create_post(request=request,db=db)
    if not post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Couldn't Create a User")
    return post

@router.get("",status_code=status.HTTP_200_OK,response_model=list[PostDisplay])
def get_post(db:Session = Depends(get_db)):
    post = db_post.get_posts(db)
    return post

@router.post("/image")
def upload_image(image:UploadFile = File(...),current_user: UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = "".join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}'

    with open(path,"w+b") as buffer :
        shutil.copyfileobj(image.file,buffer)

    return {'filename' : path}

@router.delete("/delete/{id}")
def delete(id: int,db: Session= Depends(get_db),current_user: UserAuth = Depends(get_current_user)):
    return db_post.delete_posts(db,id,current_user.id)