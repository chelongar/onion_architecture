from dataclasses import dataclass
from uuid import UUID, uuid4
from datetime import datetime, timezone


@dataclass
class TaskTitle:
    value: str

    def __post_init__(self):
        if not self.value or len(self.value.strip()) == 0:
            raise ValueError("Task title cannot be empty")


@dataclass
class Deadline:
    value: datetime

    def __post_init__(self):
        now = datetime.now(timezone.utc)
        self.value = self.value.astimezone(timezone.utc)
        if self.value < now:
            raise ValueError("Deadline cannot be in the past")


@dataclass
class Task:
    id: UUID
    title: TaskTitle
    deadline: Deadline
    completed: bool = False

    def complete(self):
        self.completed = True
