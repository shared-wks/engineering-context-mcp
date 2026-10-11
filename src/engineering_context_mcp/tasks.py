"""In-memory task management domain."""

from dataclasses import asdict, dataclass


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


class TaskStore:
    """Manage tasks in memory for the MCP learning project."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str) -> Task:
        title = title.strip()

        if not title:
            raise ValueError("Task title cannot be empty.")

        task = Task(id=self._next_id, title=title)

        self._tasks[task.id] = task
        self._next_id += 1

        return task

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def get(self, task_id: int) -> Task:
        if task_id not in self._tasks:
            raise ValueError(f"Task {task_id} not found.")

        return self._tasks[task_id]

    def complete(self, task_id: int) -> Task:
        task = self.get(task_id)
        task.completed = True
        return task

    def delete(self, task_id: int) -> Task:
        task = self.get(task_id)
        del self._tasks[task_id]
        return task

    def count(self) -> int:
        return len(self._tasks)
