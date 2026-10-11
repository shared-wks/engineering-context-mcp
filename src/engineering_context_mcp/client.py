"""Demonstrate communication with the local MCP server."""

import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run_client() -> None:
    """Connect to the server and invoke MCP operations."""

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "engineering_context_mcp.server"],
    )

    async with (
        stdio_client(server_params) as (read, write),
        ClientSession(read, write) as session,
    ):
        # Initialize MCP connection
        await session.initialize()
        print("Connected to MCP server.")

        # Discover available tools
        tools = await session.list_tools()

        print("\nAvailable tools:")
        for tool in tools.tools:
            print(f"- {tool.name}")

        # Create a task
        result = await session.call_tool(
            "add_task",
            arguments={"title": "Learn MCP fundamentals"},
        )
        print("\nAdd task result:")
        print(result.content)

        # List tasks
        result = await session.call_tool(
            "list_tasks",
            arguments={},
        )
        print("\nList tasks result:")
        print(result.content)

        # Discover resources
        resources = await session.list_resources()

        print("\nAvailable resources:")
        for resource in resources.resources:
            print(f"- {resource.uri}")

        # Retrieve tasks resource
        resource_result = await session.read_resource("tasks://all")

        print("\nTasks resource:")
        print(resource_result.contents)

        # Discover prompts
        prompts = await session.list_prompts()

        print("\nAvailable prompts:")
        for prompt in prompts.prompts:
            print(f"- {prompt.name}")


def main() -> None:
    asyncio.run(run_client())


if __name__ == "__main__":
    main()
