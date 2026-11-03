from fastapi import APIRouter, status, HTTPException

from my_project.schemas import (
    Animal,
    AnimalResponse,
    StatusResponse,
    User,
    UserResponse,
)

router = APIRouter()
users_database = dict[str, User]()
animals_database = dict[int, AnimalResponse]()


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
