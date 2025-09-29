from fastapi import HTTPException, status
from app.models.user import User, UserCreate, UserUpdate
from app.services.user_service import UserService

class UserController:
    def __init__(self, service: UserService) -> None:
        self.service = service

    def list_users(self) -> list[User]:
        return self.service.list_users()

    def get_user(self, user_id: int) -> User:
        try:
            return self.service.get_user(user_id)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    def create_user(self, payload: UserCreate) -> User:
        return self.service.create_user(payload)

    def update_user(self, user_id: int, payload: UserUpdate) -> User:
        try:
            return self.service.update_user(user_id, payload)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    def delete_user(self, user_id: int) -> dict:
        try:
            self.service.delete_user(user_id)
            return {"status": "deleted"}
        except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
