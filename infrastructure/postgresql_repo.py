from uuid import UUID

from databases import Database
from sqlalchemy import Table, Column, String, Boolean, DateTime, MetaData
from sqlalchemy.dialects.postgresql import UUID as SQLUUID

from domain.entities import Task, TaskTitle, Deadline
from domain.repositories import ITaskRepository

metadata = MetaData()

tasks_table = Table(
    "tasks",
    metadata,
    Column("id", SQLUUID(as_uuid=True), primary_key=True),
    Column("title", String, nullable=False),
    Column("deadline", DateTime, nullable=False),
    Column("completed", Boolean, default=False),
)


class PostgresTaskRepository(ITaskRepository):
    def __init__(self, database: Database):
        self.db = database

    async def add(self, task: Task):
        query = tasks_table.insert().values(
            id=task.id,
            title=task.title.value,
            deadline=task.deadline.value.replace(tzinfo=None),
            completed=task.completed
        )
        await self.db.execute(query)

    async def get_all(self):
        query = tasks_table.select()
        rows = await self.db.fetch_all(query)
        return [
            Task(
                id=row["id"],
                title=TaskTitle(row["title"]),
                deadline=Deadline(row["deadline"]),
                completed=row["completed"]
            )
            for row in rows
        ]

    async def get_by_id(self, id: UUID):
        query = tasks_table.select().where(tasks_table.c.id == id)
        row = await self.db.fetch_one(query)
        if row:
            return Task(
                id=row["id"],
                title=TaskTitle(row["title"]),
                deadline=Deadline(row["deadline"]),
                completed=row["completed"]
            )
        raise Exception("Task not found")

    async def save(self, task: Task):
        query = tasks_table.update().where(tasks_table.c.id == task.id).values(
            completed=task.completed
        )
        await self.db.execute(query)
