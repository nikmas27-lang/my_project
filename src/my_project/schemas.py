from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: str


class User(BaseModel):
    login: str
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    name: str
    email: str


class Animal(BaseModel):
    id: int
    name: str
    breed: str
    country: str

class AnimalResponse(BaseModel):
    id: int