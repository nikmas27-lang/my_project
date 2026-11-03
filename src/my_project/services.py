from my_project.models import User
from my_project.repositories import UserRepository
from my_project.schemas import UserCreate

class UserService:
    def _init_(self, user_repository: UserRepository):
        self.__user_repository = user_repository

        async def singup(self):
            if len(self.__user_repository.get_all()) = 0:
                role = UserRole.ADMIN
            else:
                role = UserRole.USER


            model = User(
                id = 0,
                login = user.login,
                name = user.name,
                role = ...,
                email = user.email,
                password = user.password
            )
        
        async def get_by_id(self, id: int)-> User | None:
        
        async def get_all(self) -> list[User]: