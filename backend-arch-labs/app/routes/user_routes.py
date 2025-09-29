from fastapi import APIRouter, Depends
from app.models.user import User, UserCreate, UserUpdate
from app.controllers.user_controller import UserController

router = APIRouter(prefix="/users", tags=["users"])

def get_controller() -> UserController:
    # simple manual DI wire-up
    from app.services.user_service import UserService
    from app.repos.user_repository import UserRepository
    return UserController(UserService(UserRepository()))

@router.get("", response_model=list[User])
def list_users(ctrl: UserController = Depends(get_controller)):
    return ctrl.list_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, ctrl: UserController = Depends(get_controller)):
    return ctrl.get_user(user_id)

@router.post("", response_model=User, status_code=201)
def create_user(payload: UserCreate, ctrl: UserController = Depends(get_controller)):
    return ctrl.create_user(payload)

@router.patch("/{user_id}", response_model=User)
def update_user(user_id: int, payload: UserUpdate, ctrl: UserController = Depends(get_controller)):
    return ctrl.update_user(user_id, payload)

@router.delete("/{user_id}")
def delete_user(user_id: int, ctrl: UserController = Depends(get_controller)):
    return ctrl.delete_user(user_id)
