from .database import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = "User"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbPost',back_populates='user')

class DbPost(Base):
    __tablename__ = "Post"
    id = Column(Integer,primary_key=True,index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer,ForeignKey('User.id'))
    user = relationship('DbUser',back_populates="items")
    comments = relationship('DbComment',back_populates="posts")

class DbComments(Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True,index = True)
    text = Column(String)
    username = Column(String)
    timestamp = Column(DateTime)
    post_id = Column(Integer,ForeignKey('Post.id'))
    post = relationship("DbPost",back_populates="comments")