from uuid import uuid4
from datetime import datetime
from domain.entities import Task, TaskTitle, Deadline
from domain.repositories import ITaskRepository


class TaskService:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    async def create_task(self, title: str, deadline: datetime):
        task = Task(
            id=uuid4(),
            title=TaskTitle(title),
            deadline=Deadline(deadline)
        )
        await self.repository.add(task)

    async def list_tasks(self):
        return await self.repository.get_all()

    async def complete_task(self, task_id):
        task = await self.repository.get_by_id(task_id)
        task.complete()
        await self.repository.save(task)
