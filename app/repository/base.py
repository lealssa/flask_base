import abc

from repository.store import MongoRepoBase

class RepositoryBase(abc.ABC):

    @abc.abstractmethod
    def add(self, entity: object):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, entity_id: str):
        raise NotImplementedError      

    @abc.abstractmethod
    def update(self, entity_id: str, entity: object):
        raise NotImplementedError          