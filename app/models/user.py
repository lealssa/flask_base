from flask_login import UserMixin
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Union
from bson import ObjectId

from models.mongodb import PyObjectId

class UserBase(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    login: Optional[str]    
    is_active: Optional[bool] = True

    class Config:
        anystr_strip_whitespace: True  
        min_anystr_length: 1
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }        

class UserLogin(UserBase):
    id: PyObjectId
    is_authenticated: Optional[bool] = True
    is_anonymous: Optional[bool] = False

    def get_id(self) -> Union[str, None]:
        return str(self.id) or None               

class UserSec(UserBase):        
    password: Optional[bytes]            

class UserRegistrationViewModel(UserSec):
    first_name: str
    last_name: str  
    email: EmailStr
    password: bytes = Field(..., min_length=6)

class UserLoginViewModel(UserSec):
    login: str = Field(...)
    password: bytes = Field(..., min_length=6)

class UserEmailRecoverViewModel(UserBase):
    email: EmailStr = Field(...)

class UserPasswordResetViewModel(UserBase):
    token: str = Field(...)
