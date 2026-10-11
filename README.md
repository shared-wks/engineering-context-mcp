
# Engineering Context MCP

An open-source Python project for building MCP-powered integrations
between AI applications and engineering tools, documentation, and workflows.

[![Python CI](https://github.com/shared-wks/engineering-context-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/shared-wks/engineering-context-mcp/actions/workflows/ci.yml)

**Current version:** 0.1.0  
**Status:** MCP foundation implemented; business integrations in development  
**License:** MIT

## Overview

Engineering Context MCP explores how Model Context Protocol (MCP) can
expose engineering data and workflows to compatible AI applications.

The current implementation is a working Python MCP client and server,
with an in-memory task-management example.

The long-term goal is to integrate Jira, Confluence, and other
engineering platforms into a containerized, secure MCP service.

## Technology Stack

### Implemented
- Python 3.12+
- Official MCP Python SDK (v1.x)
- FastMCP
- Python venv and pip
- pytest
- Ruff
- GitHub Actions

### Planned
- Docker and Docker Compose
- PostgreSQL
- SQLAlchemy and Alembic
- Streamable HTTP transport
- Jira Cloud and Confluence Cloud APIs
- OpenTelemetry and improved observability

## Prerequisites

To run version 0.1.0, you need:

- Python 3.12 or newer
- Git
- pip (included with most Python installations)

Optional:
- Node.js and npm for MCP Inspector
- An IDE such as VS Code or PyCharm

Docker, a PostgreSQL server, an LLM, and Atlassian API
credentials are not required for this release.

## Installation

### 1. Clone the repository

Using HTTPS:

```bash
git clone https://github.com/shared-wks/engineering-context-mcp.git
cd engineering-context-mcp
```

SSH is also supported if you have registered an SSH key:

```bash
git clone git@github.com:shared-wks/engineering-context-mcp.git
cd engineering-context-mcp
```

Use either clone method, not both.

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows PowerShell**

```powershell
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
```

The `venv` directory is local and excluded from Git.

### 3. Install dependencies

For development, including tests and linting:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

For application-only installation:

```bash
python -m pip install -r requirements.txt
```

These commands read package dependencies from `pyproject.toml`.

The existing `requirements/dev-py314.txt` contains optional
Python 3.14 dependency constraints generated during development.

### 4. Verify installation

```bash
python -m pip check
python -m pip show engineering-context-mcp
```

## Running the Application

### Option A: Run the MCP client demo (recommended)

```bash
python -m engineering_context_mcp.client
```

Or use the installed CLI:

```bash
engineering-context-client
```

The client automatically launches a local MCP server subprocess,
initializes a session, discovers capabilities, creates a sample
task, reads resources, and lists prompts.

Expected output includes:

```text
Connected to MCP server.

Available tools:
- add_task
- list_tasks
- complete_task
- delete_task

Available resources:
- tasks://all
- tasks://stats

Available prompts:
- summarize_tasks
```

Additional tool and resource results will also be displayed.

### Option B: Start the MCP server directly

```bash
python -m engineering_context_mcp.server
```

Or:

```bash
engineering-context-server
```

The server uses the MCP stdio transport.

It waits for protocol messages from an MCP client. It does not
start an interactive terminal menu or an HTTP web page.

Use Ctrl+C to stop it if necessary.

### Option C: Test with MCP Inspector

MCP Inspector is optional and requires a compatible Node.js
installation with npm.

From the project root:

```bash
npx @modelcontextprotocol/inspector \
  ./venv/bin/python -m engineering_context_mcp.server
```

Open the local URL shown by Inspector.

You can inspect tools, resources, prompts, input schemas,
and server responses.

See [Inspector guide](examples/inspector.md).

## Available MCP Capabilities

### Tools

| Tool | Description |
|------|-------------|
| `add_task` | Create a new task |
| `list_tasks` | Retrieve existing tasks |
| `complete_task` | Mark a task as completed |
| `delete_task` | Delete a task |

### Resources

| URI | Description |
|-----|-------------|
| `tasks://all` | Current task collection as JSON |
| `tasks://stats` | Task completion statistics |

### Prompts

| Prompt | Description |
|--------|-------------|
| `summarize_tasks` | Reusable instructions for summarizing tasks |

**Current limitation:** Tasks are stored in memory. The data
does not persist when the server process stops.

## Running Tests

The project contains unit and MCP protocol integration tests.

Run all tests:

```bash
python -m pytest -v
```

Run unit tests:

```bash
python -m pytest tests/test_tasks.py -v
```

Run MCP integration tests:

```bash
python -m pytest tests/test_mcp_integration.py -v
```

Run code-quality checks:

```bash
python -m ruff check .
python -m ruff format --check .
```

Apply formatting:

```bash
python -m ruff format .
```

The current test suite includes 8 unit tests and
6 MCP integration tests.

Integration tests launch a real MCP server subprocess and
communicate with it over stdio.

## Architecture

```text
        Python MCP Client
                 |
                 | MCP / stdio
                 v
         FastMCP Server
                 |
                 | Python calls
                 v
        In-memory TaskStore
```

See [Architecture documentation](docs/architecture.md).

## Project Structure

```text
src/engineering_context_mcp/
    client.py       MCP client demonstration
    server.py       FastMCP server entry point
    tasks.py        Task-management domain logic

tests/
    test_tasks.py             Unit tests
    test_mcp_integration.py   Protocol integration tests

docs/             Technical documentation
examples/         MCP Inspector instructions
requirements/     Optional dependency constraints
.github/workflows/ GitHub Actions
```

## Development Workflow

1. Create a feature branch.
2. Make a focused change.
3. Add or update automated tests.
4. Run pytest and Ruff.
5. Commit with a descriptive message.
6. Open a pull request or merge request.

Never commit your virtual environment, `.env` files,
API tokens, private keys, or recovery codes.

## CI/CD

GitHub Actions runs automated validation on pushes to `main`
and on pull requests.

A GitLab CI/CD pipeline is also planned as part of the
dual-platform publication.

The primary source repository is:

https://github.com/shared-wks/engineering-context-mcp

## Roadmap

| Version | Milestone | Scope |
|---------|-----------|-------|
| v0.1.0 | MCP Foundation | Python server/client, tools, resources, prompts, tests |
| v0.2.0 | Containerized Backend | Docker, Compose, PostgreSQL, SQLAlchemy, Alembic |
| v0.3.0 | Networked MCP Service | Streamable HTTP, health checks, logging |
| v0.4.0 | Atlassian Integrations | Jira and Confluence APIs |
| v0.5.0 | Engineering Workflows | Cross-service context retrieval and automation |
| v1.0.0 | Production Release | Security, observability, deployment and documentation |

## Security

- No credentials are needed for the current local demo.
- Never commit actual secrets or `.env` files.
- Use only authorized data when integrating external services.
- Use least-privilege access for future API integrations.

## License

This project is licensed under the [MIT License](LICENSE).
