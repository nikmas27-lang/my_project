from fastapi import APIRouter, status, HTTPException

from my_project.schemas import StatusResponse, User, UserResponse

router = APIRouter()
users_database = dict[str, User]()

@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")

@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
)
def signup(user: User):
    if user.login in users_database:
        raise HTTPException(status.HTTP_409_CONFLICT)
    users_database[user.login] = user

@router.get("/users/{login}")
def get_user(login: str) -> UserResponse:
    if login not in users_database:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    user = users_database[login]
    return UserResponse(
        name=user.name,
        email=user.email,
    )

    
@router.get("/users")
def get_all_users() -> list[UserResponse]:
    return [
        UserResponse(name=user.name, email=user.email)
        for user in users_database.values()
    ]