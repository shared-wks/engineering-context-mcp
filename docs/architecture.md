# Architecture

## Overview

Engineering Context MCP is a Python project for learning and
implementing Model Context Protocol integrations.

## Components

1. MCP Client
   - Discovers tools, resources, and prompts
   - Sends requests to the MCP server

2. MCP Server
   - Implements MCP using FastMCP
   - Exposes task-management operations
   - Uses stdio transport

3. Domain Layer
   - Implements task-management rules
   - Does not depend on MCP
   - Can be tested independently

## Communication

```text
Python MCP Client
        |
        | MCP over stdio
        v
Python MCP Server
        |
        | Python function calls
        v
TaskStore (in-memory)
```

## Design principles

- Separation of concerns
- Typed Python interfaces
- Testable business logic
- Dependency isolation
- No hardcoded credentials
- Reproducible development setup

## Limitations

- Task data is not persistent
- No authentication is required for the local server
- No external APIs are connected
- No LLM is needed
- stdio transport is local

## Roadmap

- v0.1: Local MCP server and client
- v0.2: MCP protocol integration tests and SQLite
- v0.3: Jira Cloud integration
- v0.4: Confluence Cloud integration
- v1.0: Production hardening and portfolio release