"""Integration tests for the MCP server over stdio."""

import asyncio
import json
import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent, TextResourceContents


@asynccontextmanager
async def connected_session() -> AsyncIterator[ClientSession]:
    """Launch a fresh MCP server and initialize a client session."""

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "engineering_context_mcp.server"],
    )

    async with (
        stdio_client(server_params) as (read, write),
        ClientSession(read, write) as session,
    ):
        await session.initialize()
        yield session


def test_server_initialization() -> None:
    """Verify that the client can initialize an MCP session."""

    async def scenario() -> None:
        async with connected_session() as session:
            result = await session.list_tools()
            assert result is not None

    asyncio.run(scenario())


def test_tool_discovery() -> None:
    """Verify tool names and their declared input schemas."""

    async def scenario() -> None:
        async with connected_session() as session:
            result = await session.list_tools()

            tools = {tool.name: tool for tool in result.tools}

            expected = {
                "add_task",
                "list_tasks",
                "complete_task",
                "delete_task",
            }

            assert expected.issubset(tools.keys())

            schema = tools["add_task"].inputSchema

            assert "title" in schema["properties"]
            assert "title" in schema["required"]

    asyncio.run(scenario())


def test_tool_invocation() -> None:
    """Verify that tool calls create and return task data."""

    async def scenario() -> None:
        async with connected_session() as session:
            create_result = await session.call_tool(
                "add_task",
                arguments={"title": "Integration test task"},
            )

            assert not create_result.isError
            assert len(create_result.content) > 0

            content = create_result.content[0]
            assert isinstance(content, TextContent)

            created_task = json.loads(content.text)

            assert created_task["id"] == 1
            assert created_task["title"] == "Integration test task"
            assert created_task["completed"] is False

            list_result = await session.call_tool(
                "list_tasks",
                arguments={},
            )

            assert not list_result.isError

            tasks = [
                json.loads(content.text)
                for content in list_result.content
                if isinstance(content, TextContent)
            ]

            assert len(tasks) == 1
            assert tasks[0]["id"] == created_task["id"]
            assert tasks[0]["title"] == "Integration test task"

            complete_result = await session.call_tool(
                "complete_task",
                arguments={"task_id": created_task["id"]},
            )

            assert not complete_result.isError

            complete_content = complete_result.content[0]
            assert isinstance(complete_content, TextContent)

            completed_task = json.loads(complete_content.text)

            assert completed_task["completed"] is True

    asyncio.run(scenario())


def test_resource_discovery_and_reading() -> None:
    """Verify resource discovery and JSON content."""

    async def scenario() -> None:
        async with connected_session() as session:
            resources = await session.list_resources()
            resource_uris = {str(r.uri) for r in resources.resources}

            assert "tasks://all" in resource_uris
            assert "tasks://stats" in resource_uris

            await session.call_tool(
                "add_task",
                arguments={"title": "Resource test task"},
            )

            result = await session.read_resource("tasks://all")

            assert len(result.contents) > 0

            content = result.contents[0]
            assert isinstance(content, TextResourceContents)

            tasks = json.loads(content.text)

            assert len(tasks) == 1
            assert tasks[0]["title"] == "Resource test task"

            stats_result = await session.read_resource("tasks://stats")

            stats_content = stats_result.contents[0]
            assert isinstance(stats_content, TextResourceContents)

            stats = json.loads(stats_content.text)

            assert stats["total"] == 1
            assert stats["pending"] == 1
            assert stats["completed"] == 0

    asyncio.run(scenario())


def test_prompt_discovery_and_retrieval() -> None:
    """Verify that MCP prompts can be listed and retrieved."""

    async def scenario() -> None:
        async with connected_session() as session:
            result = await session.list_prompts()

            prompt_names = {prompt.name for prompt in result.prompts}

            assert "summarize_tasks" in prompt_names

            prompt_result = await session.get_prompt(
                "summarize_tasks",
                arguments={},
            )

            assert len(prompt_result.messages) > 0

            message = prompt_result.messages[0]

            assert message.role == "user"
            assert isinstance(message.content, TextContent)

            assert "Completed tasks" in message.content.text
            assert "Pending tasks" in message.content.text

    asyncio.run(scenario())


def test_invalid_tool_arguments() -> None:
    """Verify that the server reports invalid task input."""

    async def scenario() -> None:
        async with connected_session() as session:
            result = await session.call_tool(
                "add_task",
                arguments={"title": "   "},
            )

            assert result.isError

            assert any(
                isinstance(content, TextContent) and "Task title cannot be empty" in content.text
                for content in result.content
            )

            # Verify the session still supports valid operations
            valid_result = await session.call_tool(
                "add_task",
                arguments={"title": "Valid task"},
            )

            assert not valid_result.isError

    asyncio.run(scenario())
