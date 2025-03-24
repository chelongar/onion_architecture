# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
import uvicorn

from application.task_service import TaskService
from infrastructure.in_memory_repo import InMemoryTaskRepository

# FastAPI app
app = FastAPI(title="ToDo App - Onion Architecture + DDD")

# Services
repo = InMemoryTaskRepository()
service = TaskService(repo)


# Request and Response Models
class TaskRequest(BaseModel):
    title: str
    deadline: datetime


class TaskResponse(BaseModel):
    id: UUID
    title: str
    deadline: datetime
    completed: bool


@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskRequest):
    service.create_task(task.title, task.deadline)
    created = service.list_tasks()[-1]
    return TaskResponse(
        id=created.id,
        title=created.title.value,
        deadline=created.deadline.value,
        completed=created.completed
    )


@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks():
    tasks = service.list_tasks()
    return [
        TaskResponse(
            id=t.id,
            title=t.title.value,
            deadline=t.deadline.value,
            completed=t.completed
        )
        for t in tasks
    ]


@app.post("/tasks/{task_id}/complete")
def complete_task(task_id: UUID):
    try:
        service.complete_task(task_id)
        return {"message": "Task marked as complete"}
    except Exception:
        raise HTTPException(status_code=404, detail="Task not found")


# Run app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
