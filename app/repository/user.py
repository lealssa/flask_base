from pydantic import BaseModel
from typing import Any
from models.mongodb import PyObjectId

from repository.store import MongoRepoBase

class UserRepository(MongoRepoBase):

    def __init__(self, model: BaseModel):
        COLLECTION = 'users'
        super().__init__(COLLECTION, model)

    def get_by_str(self, user_id: str) -> Any:
        """ Returns a object by str id"""
        return self.get_by(PyObjectId(user_id))