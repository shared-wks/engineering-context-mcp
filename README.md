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

| Version | Milestone | Scope |
|---------|-----------|-------|
| v0.1.0 | MCP Foundation | Python MCP server/client, tools, resources, prompts, automated tests |
| v0.2.0 | Containerized Backend | Docker, Docker Compose, PostgreSQL, SQLAlchemy, Alembic |
| v0.3.0 | Networked MCP Service | Streamable HTTP, configuration, health checks, logging |
| v0.4.0 | Atlassian Integrations | Jira Cloud and Confluence Cloud API integrations |
| v0.5.0 | Engineering Workflows | Cross-platform context retrieval and workflow automation |
| v1.0.0 | Production-Ready Release | Security hardening, observability, CI/CD, documentation |

## Security

Never commit credentials, tokens, or local environment files.

Use personal test environments for external integrations.

## License

MIT