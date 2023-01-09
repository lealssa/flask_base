from redbird.repos import MongoRepo
from pydantic import BaseModel

from pymongo import MongoClient

from extensions.config import app_settings

class MongodbStore:    

    def __init__(self, dsn: str, database: str, collection: str) -> None:
        self.client = MongoClient(dsn)
        self.db = self.client.get_database(database)
        self.collection = self.db.get_collection(collection)
    
    def __enter__(self):
        return self

    def __exit__(self):
        if self.client:
            self.client.close()

class MongoRepoBase(MongoRepo):

    def __init__(self, collection: str, model: BaseModel):
        super().__init__(            
            uri=app_settings.mongodb_dsn,
            database=app_settings.db_name,
            collection=collection,
            model=model
        )

        self.id_field = "_id"
        self.default_id_field = "_id"





        
