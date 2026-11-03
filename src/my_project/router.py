from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status

from my_project.schemas import (
    Animal,
    AnimalResponse,
    StatusResponse,
    UserCreate,
    UserResponse,
)
from my_project.services import UserService

router = APIRouter()


def get_user_service(request: Request) -> UserService:
    return request.app.state.user_service


type UserServiceDep = Annotated[UserService, Depends(get_user_service)]


@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
)
async def signup(user: UserCreate, user_service: UserServiceDep):
    await user_service.signup(user)


@router.get("/users/{id}")
async def get_user_by_id(id: int, user_service: UserServiceDep) -> UserResponse:
    user = await user_service.get_by_id(id)
    return UserResponse(
        name=user.name,
        email=user.email,
    )


animals_database = dict[int, AnimalResponse]()


@router.get("/animals/{id}")
def get_animal(id: int) -> AnimalResponse:
    if id not in animals_database:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return animals_database[id]


@router.post(
    "/animals",
    status_code=status.HTTP_201_CREATED,
)
def create_animal(animal: Animal) -> AnimalResponse:
    new_id = len(animals_database) + 1
    animal_response = AnimalResponse(
        id=new_id,
        name=animal.name,
        breed=animal.breed,
        country=animal.country,
    )
    animals_database[new_id] = animal_response
    return animal_response


@router.get("/animals")
def get_all_animals() -> list[AnimalResponse]:
    return list(animals_database.values())
