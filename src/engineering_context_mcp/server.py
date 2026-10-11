"""MCP server exposing task-management capabilities."""

import json

from mcp.server.fastmcp import FastMCP

from engineering_context_mcp.tasks import TaskStore

mcp = FastMCP("Engineering Context MCP")
store = TaskStore()


# -------------------------------------------------
# MCP TOOLS
# -------------------------------------------------


@mcp.tool()
def add_task(title: str) -> dict:
    """Create a new task using its title."""
    return store.add(title).to_dict()


@mcp.tool()
def list_tasks() -> list[dict]:
    """Return all existing tasks."""
    return [task.to_dict() for task in store.list_all()]


@mcp.tool()
def complete_task(task_id: int) -> dict:
    """Mark an existing task as completed."""
    return store.complete(task_id).to_dict()


@mcp.tool()
def delete_task(task_id: int) -> dict:
    """Delete an existing task by its ID."""
    return store.delete(task_id).to_dict()


# -------------------------------------------------
# MCP RESOURCES
# -------------------------------------------------


@mcp.resource("tasks://all")
def tasks_resource() -> str:
    """Read the current task collection as JSON."""
    tasks = [task.to_dict() for task in store.list_all()]
    return json.dumps(tasks, indent=2)


@mcp.resource("tasks://stats")
def task_statistics() -> str:
    """Read task completion statistics."""
    tasks = store.list_all()

    completed = sum(task.completed for task in tasks)

    return json.dumps(
        {
            "total": len(tasks),
            "completed": completed,
            "pending": len(tasks) - completed,
        },
        indent=2,
    )


# -------------------------------------------------
# MCP PROMPTS
# -------------------------------------------------


@mcp.prompt()
def summarize_tasks() -> str:
    """Generate instructions for summarizing tasks."""
    return (
        "Review the available tasks and provide:\n"
        "1. Total number of tasks\n"
        "2. Completed tasks\n"
        "3. Pending tasks\n"
        "4. Recommended next actions"
    )


# -------------------------------------------------
# SERVER ENTRY POINT
# -------------------------------------------------


def main() -> None:
    """Start the MCP server using stdio transport."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
