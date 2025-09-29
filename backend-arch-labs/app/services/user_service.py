from typing import List
from app.models.user import User, UserCreate, UserUpdate
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def list_users(self) -> List[User]:
        return self.repo.list()

    def get_user(self, user_id: int) -> User:
        user = self.repo.get(user_id)
        if not user:
            raise ValueError("USER_NOT_FOUND")
        return user

    def create_user(self, payload: UserCreate) -> User:
        # place business rules here (e.g., uniqueness, validations)
        return self.repo.create(payload)

    def update_user(self, user_id: int, payload: UserUpdate) -> User:
        user = self.repo.update(user_id, payload)
        if not user:
            raise ValueError("USER_NOT_FOUND")
        return user

    def delete_user(self, user_id: int) -> None:
        ok = self.repo.delete(user_id)
        if not ok:
            raise ValueError("USER_NOT_FOUND")
