from sqlalchemy.orm import Session
from db.models import DbComments
from router.schemas import CommentBase
from datetime import datetime

def create(db:Session,request: CommentBase):
    new_comment = DbComments(
        text = request.text,
        username = request.username,
        post_id = request.post_id,
        timestamp = datetime.datetime.now()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db:Session,post_id:int):
    comments = db.query(DbComments).filter(post_id == DbComments.post_id)
    if not comments:
        return "No Comments on this Post!!"
    return comments