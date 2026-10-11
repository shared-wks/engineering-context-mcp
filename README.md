# Engineering Context MCP

A Python engineering project for learning, building,
testing, and documenting Model Context Protocol (MCP)
integrations.

## Goals

- Understand MCP architecture and capabilities
- Develop MCP servers and clients in Python
- Practice software engineering and automated testing
- Integrate Jira and Confluence in future releases
- Build an open-source engineering portfolio project

## Tech Stack

- Python 3.12+
- Official MCP Python SDK v1.x
- Python venv and pip
- pytest
- Ruff
- MCP Inspector
- GitHub Actions

## Project Structure

- `src/engineering_context_mcp/`: application source code
- `tests/`: automated tests
- `docs/`: technical documentation
- `examples/`: MCP usage examples
- `.github/workflows/`: CI configuration

## Quick Start

Clone the repository, then:

```bash
python3 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the MCP Client Demo

```bash
python -m engineering_context_mcp.client
```

Or use the installed command:

```bash
engineering-context-client
```

The client automatically launches the server.

## Run the Server

```bash
engineering-context-server
```

The server communicates over stdio.

It waits for MCP requests from a client and
does not expose a normal command-line menu.

## Run Tests

```bash
python -m pytest -q
python -m ruff check .
```

## MCP Capabilities

### Tools

- add_task
- list_tasks
- complete_task
- delete_task

### Resources

- tasks://all
- tasks://stats

### Prompts

- summarize_tasks

## Documentation

See `docs/architecture.md` for the architecture.

See `examples/inspector.md` for interactive testing.

## Roadmap

| Version | Scope |
|---------|-------|
| 0.1 | Local MCP server and client |
| 0.2 | Protocol tests and SQLite |
| 0.3 | Jira integration |
| 0.4 | Confluence integration |
| 1.0 | Portfolio release |

## Security

Never commit credentials, tokens, or local environment files.

Use personal test environments for external integrations.

## License

MIT