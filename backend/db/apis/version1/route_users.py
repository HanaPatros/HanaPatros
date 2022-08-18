from pastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.users import UserCreate
from db.session import get_db
from db.repository.users import create_new_user

router = APIRouter()


@router.post("/users")
def create_users(user: UserCreate, db:Session=Depends(get_db)):
    user = create_new_users(user, db)
    return user