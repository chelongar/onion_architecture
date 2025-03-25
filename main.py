from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
import os

from databases import Database
from typing import List

from application.task_service import TaskService
from infrastructure.postgresql_repo import PostgresTaskRepository, tasks_table, metadata

import sqlalchemy
import uvicorn

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/tododb")
database = Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL.replace("+asyncpg", ""))
metadata.create_all(engine)

app = FastAPI(title="ToDo App - Onion Architecture + DDD + Postgres")

# Dependency Injection
task_repo = PostgresTaskRepository(database)
task_service = TaskService(task_repo)


class TaskRequest(BaseModel):
    title: str
    deadline: datetime


class TaskResponse(BaseModel):
    id: UUID
    title: str
    deadline: datetime
    completed: bool


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskRequest):
    await task_service.create_task(task.title, task.deadline)
    tasks = await task_service.list_tasks()
    created = tasks[-1]
    return TaskResponse(id=created.id,
                        title=created.title.value,
                        deadline=created.deadline.value,
                        completed=created.completed)


@app.get("/tasks", response_model=List[TaskResponse])
async def list_tasks():
    tasks = await task_service.list_tasks()
    return [TaskResponse(id=t.id,
                         title=t.title.value,
                         deadline=t.deadline.value,
                         completed=t.completed) for t in tasks]


@app.post("/tasks/{task_id}/complete")
async def complete_task(task_id: UUID):
    try:
        await task_service.complete_task(task_id)
        return {"message": "Task marked as complete"}
    except Exception:
        raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
