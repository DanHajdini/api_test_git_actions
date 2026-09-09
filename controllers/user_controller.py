from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException

from sqlalchemy import select
from starlette import status

from dtos.user_login_request_dto import UserLoginRequestDto
from dtos.user_register_request_dto import UserRegisterRequestDto
from models.base import get_session
from models.user import User
from utils import jwt_utils, password_utils

from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["User"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(
    dto: Annotated[UserRegisterRequestDto, Body()],
    session: Annotated[Session, Depends(get_session)]
):

    try: 
        account = User(
            username=dto.username,
            email=dto.email,
            password=password_utils.hash(dto.password),
            role=dto.role
        )
        session.add(account)
        session.flush()
    except Exception as e:
        print('-----------------------------------')
        raise HTTPException(status_code=400, detail=str(e))

    return account

@router.post("/login", status_code=status.HTTP_201_CREATED)
def login(dto: Annotated[UserLoginRequestDto, Body()], session: Annotated[Session, Depends(get_session)]):


    account = session.execute(
        select(User).where(User.username == dto.username)
    ).scalar()

    if not account or not password_utils.verify_password(dto.password, account.password):
        raise HTTPException(401)

    return {
        'access_token': jwt_utils.create_token(account.id, account.role.value)
    }

    
    
