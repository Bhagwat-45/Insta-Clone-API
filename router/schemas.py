from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email:str
    class Config():
        from_attributes = True
        #Does the Conversion for us


class User(BaseModel):
    username: str
    class Config():
        from_attributes = True 

class Comment(BaseModel):
    text : str
    username: str
    timestamp : datetime
    class Config():
        from_attributes = True


class PostBase(BaseModel):
    image_url : str
    image_url_type : str # Relative: From the fastapi and Absolute: If we get the Post From Internet
    caption : str
    creator_id : int


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp : datetime
    user: User
    comments: List[Comment]
    class Config():
        from_attributes = True


class UserAuth(BaseModel):
    id : int
    username: str
    email : str

class CommentBase(BaseModel):
    username: str
    text :str
    post_id : int
