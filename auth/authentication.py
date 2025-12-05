from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from db.database import get_db
from sqlalchemy.orm import Session
from db.models import DbUser
from db.hashing import Hash

router = APIRouter(
    tags=["authentication"]
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="The password is incorrect!")
    
    