# Testing with MCP Inspector

MCP Inspector is an interactive debugging tool
for Model Context Protocol servers.

## Prerequisites

- Node.js and npm
- Active Python virtual environment
- Installed Python project

## Start Inspector

From the project root:

```bash
npx @modelcontextprotocol/inspector \
  ./venv/bin/python -m engineering_context_mcp.server
```

Open the URL printed in the terminal.

## Tests

### Tools

List available tools.

Call `add_task`:

```json
{
  "title": "Learn MCP"
}
```

Call `list_tasks` with empty arguments.

Call `complete_task`:

```json
{
  "task_id": 1
}
```

### Resources

Read these resources:

- tasks://all
- tasks://stats

### Prompts

Retrieve the `summarize_tasks` prompt.

## Expected behavior

- Tools are discoverable.
- Tasks can be created and completed.
- Resources return JSON data.
- The prompt returns reusable instructions.

Note: Restarting the server clears the tasks.