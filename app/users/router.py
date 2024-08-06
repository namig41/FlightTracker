from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import Response

from app.users.auth import get_password_hash, verify_password, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.shemas import SUserAuth

from app.tasks.tasks import send_confirmation_email

from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/moc_users.csv",
    tags=["Пользователи"]
)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_or_one(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.insert(email=user_data.email, hashed_password=hashed_password)
    send_confirmation_email.delay(user_data.email)


@router.get("/all")
async def get_users():
    return await UsersDAO.find_all()


@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return await UsersDAO.find_by_id(user_id)


@router.post("/logout")
async def user_logout(response: Response):
    response.delete_cookie("booking_access_token")


@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user
