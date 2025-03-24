from domain.repositories import ITaskRepository
from domain.entities import Task
from uuid import UUID


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = {}

    def add(self, task: Task):
        self.tasks[task.id] = task

    def get_all(self):
        return list(self.tasks.values())

    def get_by_id(self, id: UUID):
        return self.tasks.get(id)

    def save(self, task: Task):
        self.tasks[task.id] = task
