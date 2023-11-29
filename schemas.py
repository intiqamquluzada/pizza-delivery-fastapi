from pydantic import BaseModel, validator
from typing import Optional


class SignUp(BaseModel):
    # id: Optional[int] = None
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = False

    class Config:
        orm_mode = True
        json_schema_extra = {
            'username': 'intigam',
            'email': 'intigam@gmail.com',
            'password': 'password',
            'is_staff': False,
            'is_active': True
        }


class UserResponse(BaseModel):
    username: str
    email: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = False

    class Config:
        orm_mode = True
        json_schema_extra = {
            'username': 'intigam',
            'email': 'intigam@gmail.com',
            'is_staff': False,
            'is_active': True
        }
class Settings(BaseModel):
    authjwt_secret_key: str = '1f4c878dca6ca65c03d18005563e29ad52fe2c6c263a6696646b90bc975b2927'


class LoginModel(BaseModel):
    username: str
    password: str

class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = "PENDING"
    pizza_size: Optional[str] = "SMALL"
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "quantity": 2,
                "pizza_size": "LARGE",
            }
        }

