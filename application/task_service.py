from uuid import uuid4
from datetime import datetime
from domain.entities import Task, TaskTitle, Deadline
from domain.repositories import ITaskRepository


class TaskService:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def create_task(self, title: str, deadline: datetime):
        task = Task(
            id=uuid4(),
            title=TaskTitle(title),
            deadline=Deadline(deadline)
        )
        self.repository.add(task)

    def list_tasks(self):
        return self.repository.get_all()

    def complete_task(self, task_id):
        task = self.repository.get_by_id(task_id)
        task.complete()
        self.repository.save(task)
