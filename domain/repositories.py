from abc import ABC, abstractmethod
from domain.entities import Task
from typing import List
from uuid import UUID


class ITaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task):
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Task:
        pass

    @abstractmethod
    def save(self, task: Task):
        pass
