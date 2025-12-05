from router.schemas import PostBase
from sqlalchemy.orm import Session
from db.models import DbPost
import datetime
from fastapi import HTTPException,status

def create_post(db:Session,request:PostBase):
    post = DbPost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.datetime.now(),
        user_id = request.creator_id
    )

    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_posts(db:Session):
    posts = db.query(DbPost).all()
    if not posts:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,description="No posts are found!!")
    return posts

def delete_posts(db:Session,id:int,user_id: int):
    posts = db.query(DbPost).filter(DbPost.id == id and DbPost.user_id == user_id).first()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The Posts with id: {id} and user_id : {user_id} was not found!")
    if posts.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only post creator can delete post')
    db.delete(posts)
    db.commit()
    return "Okay"
