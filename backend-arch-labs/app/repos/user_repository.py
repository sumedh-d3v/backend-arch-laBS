from typing import Dict, List, Optional
from threading import Lock
from app.models.user import User, UserCreate, UserUpdate

class UserRepository:
    def __init__(self) -> None:
        self._db: Dict[int, User] = {}
        self._lock = Lock()
        self._next_id = 1

    def list(self) -> List[User]:
        return list(self._db.values())

    def get(self, user_id: int) -> Optional[User]:
        return self._db.get(user_id)

    def create(self, data: UserCreate) -> User:
        with self._lock:
            uid = self._next_id
            self._next_id += 1
        user = User(id=uid, name=data.name, email=data.email)
        self._db[uid] = user
        return user

    def update(self, user_id: int, data: UserUpdate) -> Optional[User]:
        user = self._db.get(user_id)
        if not user:
            return None
        updated = user.model_copy(
            update={k: v for k, v in data.model_dump(exclude_unset=True).items()}
        )
        self._db[user_id] = updated
        return updated

    def delete(self, user_id: int) -> bool:
        return self._db.pop(user_id, None) is not None
