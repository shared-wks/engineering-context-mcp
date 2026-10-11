"""Unit tests for task management."""

import pytest

from engineering_context_mcp.tasks import TaskStore


@pytest.fixture
def store() -> TaskStore:
    return TaskStore()


def test_add_task(store: TaskStore) -> None:
    task = store.add("Learn MCP")

    assert task.id == 1
    assert task.title == "Learn MCP"
    assert task.completed is False


def test_list_tasks(store: TaskStore) -> None:
    store.add("Task A")
    store.add("Task B")

    tasks = store.list_all()

    assert len(tasks) == 2


def test_complete_task(store: TaskStore) -> None:
    task = store.add("Write MCP server")

    updated = store.complete(task.id)

    assert updated.completed is True


def test_delete_task(store: TaskStore) -> None:
    task = store.add("Temporary task")

    store.delete(task.id)

    assert store.count() == 0


def test_empty_title(store: TaskStore) -> None:
    with pytest.raises(ValueError):
        store.add("   ")


def test_unknown_task(store: TaskStore) -> None:
    with pytest.raises(ValueError):
        store.get(999)


def test_incremental_ids(store: TaskStore) -> None:
    first = store.add("First")
    store.delete(first.id)

    second = store.add("Second")

    assert second.id == 2


def test_statistics_count(store: TaskStore) -> None:
    store.add("One")
    store.add("Two")

    assert store.count() == 2
