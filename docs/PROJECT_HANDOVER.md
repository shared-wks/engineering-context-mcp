# Engineering Context MCP — Project Handover & Continuity Guide

> **Snapshot:** 11 October 2026, updated after creation of the GitLab group `shared-wks`.  
> **Project status:** v0.1.0 MCP foundation is published on GitHub with passing CI; a **public GitLab group now exists**, but its `engineering-context-mcp` project, second Git remote, and CI/CD pipeline are **not created/verified**. Docker and PostgreSQL are planned.  
> **Purpose of this document:** Preserve the project's decisions, implementation, setup history, verified results, open questions, and next steps so another developer or AI assistant can resume work accurately.  
> **Repository location:** Intended path `docs/PROJECT_HANDOVER.md`; the latest Git commit containing this file has **not been verified**. Update and commit the Markdown copy explicitly.

## 1. Read this first: current state

**Project:** Engineering Context MCP  
**Python distribution / repository:** `engineering-context-mcp`  
**Python import package:** `engineering_context_mcp`  
**GitHub organization:** [Shared Workspace (`shared-wks`)](https://github.com/shared-wks)  
**Public GitHub repository:** https://github.com/shared-wks/engineering-context-mcp  
**Public GitLab group:** https://gitlab.com/shared-wks (created; **project not yet created**)  
**Local workspace on the original Mac:** `~/myprojects/poc/engineering-context-mcp`  
**Primary branch:** `main`  
**First release tag:** `v0.1.0`  
**License:** MIT

### Verified as completed

- [x] Created a standalone Python project with a `src/` package layout.
- [x] Used Python **`venv` + `pip`**, explicitly **not `uv`**.
- [x] Built a functioning MCP server and a separate Python MCP client using **stdio**.
- [x] Exposed **4 tools, 2 resources and 1 prompt**.
- [x] Implemented **8 unit tests** and **6 subprocess/protocol integration tests**.
- [x] All **14 tests passed** locally; Ruff linting and formatting checks passed; `pip check` passed.
- [x] Generated `requirements/dev-py314.txt` using `pip-tools` for a Python 3.14 development dependency resolution.
- [x] Initialized local Git (`main`), created a first commit, and published the code to a **public GitHub repository**.
- [x] Published **one version tag** (`v0.1.0` in the project's release process).
- [x] Updated the README roadmap to Docker/PostgreSQL rather than SQLite and pushed the documentation commit.
- [x] Added six GitHub topics: `python`, `mcp`, `model-context-protocol`, `mcp-server`, `ai-engineering`, `integration-testing`.
- [x] Observed **two successful GitHub Actions workflow runs** in the latest screenshots (initial commit and README update).
- [x] Created the `shared-wks` organization, configured its display name as **Shared Workspace**, and enforced secure two-factor authentication for members.
- [x] Set up SSH key authentication from the personal Mac to the GitHub user account; `ssh -T git@github.com` succeeded.
- [x] Created the **public GitLab group** `shared-wks` with display name **Shared Workspace**; verified both from the GitLab page and through the connected GitLab API. Group contains no projects at the time of this snapshot.

### Not completed — do not claim these are implemented

- [ ] GitLab **project** `shared-wks/engineering-context-mcp`, GitLab SSH key/remote, GitLab CI/CD, and publication of matching `main` and `v0.1.0` refs. (**Public GitLab group is complete**.)
- [ ] Dockerfile, Docker Compose services, PostgreSQL, SQLAlchemy, Alembic migrations.
- [ ] Database persistence (the current task store is **in memory** and resets on server restart).
- [ ] Networked/remote MCP transport (current implementation uses **stdio**, not deployed Streamable HTTP).
- [ ] Jira Cloud and Confluence Cloud integration. **No Atlassian credentials or API calls** are required by v0.1.0.
- [ ] Production authentication/authorization, service observability, vulnerability scanning and deployment.
- [ ] GitHub branch protection/rulesets, a formal GitHub Release page, and additional production-oriented repository polish (not confirmed).
- [ ] Portable root-level `requirements.txt` and `requirements-dev.txt`, a user/developer Quick Start in README, and GitHub CI installation via `requirements-dev.txt` were **proposed** in the next GitLab-preparation discussion; their presence and publication have **not been verified**.
- [ ] Committing this current handover as `docs/PROJECT_HANDOVER.md` has **not been verified**, even though a downloadable copy was prepared earlier.

**Critical distinction:** This is currently a credible, tested **MCP foundation** and a scaffold for an engineering-context platform; it is **not yet** a production-ready Jira/Confluence context service.

## 2. Why the project exists and what it will become

The project began as a way to learn **Model Context Protocol (MCP)** without Claude Code. Claude Code was available on a work laptop, but the implementation is being built on a **personal Mac**. Learning and testing must therefore work without a paid model or proprietary IDE integration.

The business direction was then refined: build a **portfolio-quality, open-source engineering context platform** so AI applications can discover and use structured context across engineering systems. An eventual example workflow is:

> Find high-priority Jira bugs, retrieve related Confluence specifications, and surface missing acceptance criteria.

Target users include developers, QA engineers and engineering teams. The portfolio should demonstrate **AI engineering, backend engineering, data integration, testing, containerization and CI/CD**. Do not add Kafka/Kubernetes/microservices merely for visual complexity; introduce services only where justified.

**Business/source-of-truth rule:** Jira and Confluence APIs remain authoritative for their records. PostgreSQL should store **application-owned** data (e.g., saved context queries, task records, integration audit events, sync checkpoints and appropriate metadata), not uncritically duplicate every Atlassian record.

### Technology decisions

| Decision | Status / rationale |
|---|---|
| Python, standard `venv`, `pip` | **Chosen and implemented.** No `uv` for this project. |
| Official Python MCP SDK / `FastMCP` | **Implemented** for a local stdio server/client. |
| Python `src/` package layout | **Implemented** and installable with `pip install -e`. |
| pytest + Ruff | **Implemented** and passing. |
| `pip-tools` + Python 3.14 constraints file | **Implemented**; Linux/cross-version reproducibility needs further CI hardening. |
| GitHub public organization + GitHub Actions | **Implemented**. |
| GitLab public group | **Implemented and verified:** `shared-wks`, display name Shared Workspace, visibility public. |
| GitLab repository, SSH, CI | **Not yet created/verified.** The group currently has no projects. |
| Docker + Compose + PostgreSQL | **Chosen for v0.2**, not implemented. SQLite is **not** in the revised plan. |
| SQLAlchemy + Alembic | Planned persistence/migrations for v0.2. |
| Streamable HTTP | Planned for v0.3; retain stdio for debugging/tests. |
| HTTPX + Atlassian REST APIs | Planned for v0.4. No Atlassian Rovo dependency required. |
| OpenTelemetry/structured observability | Planned later, not implemented. |

## 3. Historical setup and milestones

1. **Local workspace:** The Mac already organized source code into `myprojects/{ai,dev,mobile,poc,sf}`. The project was placed under `myprojects/poc/`.
2. **Original name:** Started as `mcp-integration-lab` (a generic learning lab).
3. **Virtual environment:** Created with `python3 -m venv venv`, then `source venv/bin/activate`. Note that the folder is named **`venv`**, not `.venv`.
4. **Initial Python package:** Added `pyproject.toml`, `src/`, `tests/`, `README.md`, `LICENSE`, `.gitignore`, `.env.example`, `docs/`, `examples/`, and `.github/workflows/`.
5. **First implementation:** Wrote an in-memory `TaskStore`, MCP server decorators, and a Python MCP client. Verified the client can discover/invoke tools and read resources without an LLM.
6. **Unit testing:** Eight domain-level pytest tests passed.
7. **Linting fixes:** Ruff flagged `SIM117` for nested async context managers and `I001` for import ordering. Combined async context managers and applied Ruff fixes/formatting.
8. **MCP integration testing:** Added six tests that run the MCP server as a subprocess over stdio. One test initially failed because the MCP SDK represented returned task list items as text content blocks rather than a single JSON list. The test was corrected to parse the content blocks. All 14 tests then passed.
9. **Business-oriented rename:** Renamed directory to `engineering-context-mcp`, Python module to `engineering_context_mcp`, distribution and CLI entry points accordingly. Re-created `venv` after the move (virtual environments may embed absolute paths). All 14 tests and client smoke tests passed after migration.
10. **Dependency reproducibility:** Created `requirements/dev-py314.txt` using `pip-compile`. The first attempt to use it as a constraint failed with `Constraints cannot have extras`; it was regenerated with `--strip-extras`. The constrained editable install then succeeded, and `pip check`, Ruff and pytest passed.
11. **GitHub organization:** Created `shared-wks`, display name **Shared Workspace**, intended for future public/collaborative projects beyond MCP. The `shared` username was unavailable. Organization contact/billing email is separate from GitHub login email; do not publish those details unnecessarily.
12. **GitHub security:** Enabled personal 2FA via an authenticator app, added a passkey through Google Password Manager, then enabled organization-wide 2FA and secure-method requirements. Organization member privilege changes were discussed; exact saved values should be rechecked instead of assumed.
13. **GitHub SSH:** Generated a dedicated ED25519 key pair and configured SSH to select it for `github.com`; registered the public key on the GitHub account. Verified `ssh -T git@github.com` printed successful authentication.
14. **GitHub repository:** Created `shared-wks/engineering-context-mcp` as **Public** and initially empty. Local `git init -b main` followed by staging, content checks, a first commit/tag, and push via SSH.
15. **GitHub CI and profile polish:** The initial commit and subsequent README roadmap update both appeared as **successful `Python CI` runs** in screenshots. Added six topical tags to the repository's About section.
16. **GitLab group created (11 Oct 2026):** Created `https://gitlab.com/shared-wks` with display name **Shared Workspace** and Public visibility. The screenshot shows **Create project**, no entries under Subgroups and projects, and the group URL; a live GitLab lookup confirmed `full_path=shared-wks`, `visibility=public`, and an empty project list. Lookup for `shared-wks/engineering-context-mcp` returned not found.
17. **Portable local/desktop setup requested:** User requested a root-level `requirements.txt` and README instructions so another machine or other developers can clone, install, run and test the app. Instructions and proposed files `requirements.txt`, `requirements-dev.txt`, and `.gitlab-ci.yml` were provided in chat, but **there is no evidence yet they have been created, tested or pushed**.
18. **Next work:** Create the matching **public GitLab project** under the existing group, finish portable installation/readme changes and GitLab CI, configure GitLab SSH/remote and push matching history. Then implement Docker/PostgreSQL-based v0.2.

### Git history seen during setup

| Reference | Description | Evidence |
|---|---|---|
| `4240449` | `feat: initialize engineering context MCP` | GitHub initial public commit screenshot. |
| `v0.1.0` | Annotated first-release tag created during publication workflow | Repository showed one tag; verify target with `git show v0.1.0`. |
| `bdb3452` | `docs: update project roadmap for containerized architecture` | Latest GitHub screenshot on `main`. |
| `Python CI #1` and `#2` | Both showed success in the latest GitHub Actions screenshot | Verify individual run/job details when needed. |

**Do not move/re-create `v0.1.0` just to include later documentation commits.** The tagged release is a historical snapshot; later updates belong on `main` until the next planned release.

## 4. Current repository layout

```text
engineering-context-mcp/
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions workflow
├── docs/
│   ├── architecture.md            # v0.1 architecture (existing)
│   └── PROJECT_HANDOVER.md        # THIS proposed handover (add to local repo)
├── examples/
│   └── inspector.md               # MCP Inspector instructions
├── requirements/
│   └── dev-py314.txt              # pip-tools generated constraints
├── src/
│   └── engineering_context_mcp/
│       ├── __init__.py
│       ├── tasks.py                # in-memory task model/store
│       ├── server.py               # FastMCP tools/resources/prompt
│       └── client.py               # stdio MCP client demonstration
├── tests/
│   ├── __init__.py
│   ├── test_tasks.py               # 8 unit tests
│   └── test_mcp_integration.py     # 6 real stdio protocol tests
├── .env.example                   # future config placeholders, no real credentials
├── .gitignore                     # ignores virtual environment/secrets/caches
├── LICENSE                        # MIT
├── README.md
├── pyproject.toml                 # setuptools, dependencies, scripts, tool config
└── venv/                          # local ONLY; ignored by Git
```

**Do not assume these files exist yet:** `.gitlab-ci.yml`, root-level `requirements.txt` and `requirements-dev.txt`, `Dockerfile`, `compose.yaml`, database migration directories, Jira/Confluence integrations, `.env`, or `docs/PROJECT_HANDOVER.md` in the public repo until explicitly verified with `git ls-files` / the hosted repository. The root requirements and GitLab CI files have been **designed in chat, not confirmed as committed**.

### `pyproject.toml` snapshot

- Python requirement: `>=3.12`.
- MCP dependency: `mcp>=1.28,<2` (the working local installation reported **MCP SDK 1.30.0**).
- Development extras: `pytest>=8,<10`, `ruff>=0.9,<1`.
- Build backend: setuptools.
- Entry points: `engineering-context-server` and `engineering-context-client`.
- The working Mac reported **Python 3.14.5**, **pytest 9.1.1**, **Ruff 0.17.0** at the time of setup.

## 5. What the current Python code actually does

### Server / client architecture

```text
Python MCP client (client.py)          Optional MCP Inspector
          │                                  │
          └──────── MCP protocol over stdio ─┘
                             │
                 FastMCP server (server.py)
                             │
                   TaskStore (tasks.py)
                             │
                     In-memory state
```

The client launches the server as a subprocess using the active Python interpreter, runs MCP session initialization, lists tools, executes tool calls, lists and reads resources, and lists prompts. It is **not an LLM agent** and needs no Claude Code, API key or paid inference service.

| MCP capability | Name / URI | Current behavior |
|---|---|---|
| Tool | `add_task(title)` | Creates an in-memory task. |
| Tool | `list_tasks()` | Lists tasks. |
| Tool | `complete_task(task_id)` | Marks a task complete. |
| Tool | `delete_task(task_id)` | Deletes a task. |
| Resource | `tasks://all` | JSON representation of current tasks. |
| Resource | `tasks://stats` | JSON counts of total/completed/pending tasks. |
| Prompt | `summarize_tasks` | Returns instructions for summarizing tasks. |

`TaskStore` is deliberately separated from the transport layer. For v0.2, migrate behind a storage abstraction rather than embedding SQL queries inside MCP tool functions.

### Automated test inventory

**Unit tests (8):** add task, list tasks, complete task, delete task, reject empty title, reject unknown task, incremental IDs, total count.

**MCP subprocess integration tests (6):** initialize session, discover tools/schemas, invoke tools, discover/read resources, discover/retrieve prompts, report invalid tool arguments and recover for subsequent valid operations.

The suite isolates each MCP integration test by launching a fresh server process. The current tests do **not** cover PostgreSQL, container networking, HTTP transport, Jira, Confluence, credential handling, or production authorization.

## 6. Development environment and reproducible commands

### Original development environment

- Personal **macOS on Apple Silicon (ARM64)**.
- Local path: `~/myprojects/poc/engineering-context-mcp`.
- Python installed on host: **3.14.5** (Homebrew); project `venv/` recreated after renaming.
- Docker Desktop installed and running: **Docker Engine 29.3.1**, **Docker Compose 5.1.1**. Docker host reported `linux/arm64`, approximately 7.65 GiB memory allocated. **No project containers or database services were created yet.**
- PyCharm used for project editing; `.idea/` ignored.
- MCP Inspector is documented as an optional tool, but a successful Inspector UI run was **not explicitly verified**. The native Python MCP client **was verified**.

### Start work in the existing checkout

```bash
cd ~/myprojects/poc/engineering-context-mcp
source venv/bin/activate
python --version
python -m pip check
python -m ruff check .
python -m ruff format --check .
python -m pytest -v
python -m engineering_context_mcp.client
```

### Recreate a clean virtual environment (new machine or broken `venv`)

```bash
git clone git@github.com:shared-wks/engineering-context-mcp.git
cd engineering-context-mcp
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m pip check
python -m pytest -v
python -m ruff check .
python -m ruff format --check .
```

For a Python **3.14** environment, apply the checked-in constraints as needed:

```bash
python -m pip install -e '.[dev]' -c requirements/dev-py314.txt
```

The constraints file was generated on macOS. Its compatibility with other OSes/architectures and Python versions must be proven by CI; it is not a universal cross-platform lock. A clean install into a fresh environment is more meaningful than checking an already-populated venv.

### Portable installation requested for a second desktop and other users (pending implementation)

The next repository improvement is to add two **thin pip entry-point files** at the repository root, *without duplicating or independently pinning all dependencies*:

`requirements.txt`:

```text
# Runtime dependencies come from pyproject.toml
-e .
```

`requirements-dev.txt`:

```text
# Runtime and optional dev dependencies from pyproject.toml
-e .[dev]
```

Then make the README explain (a) HTTPS/SSH cloning, (b) `python3 -m venv venv` and activation on macOS/Linux, (c) Windows activation separately, (d) `python -m pip install -r requirements-dev.txt`, (e) `python -m engineering_context_mcp.client` and/or `engineering-context-client`, (f) why a directly launched stdio server waits for an MCP client, (g) pytest/Ruff commands, and (h) all **current** limitations (in-memory state, no Jira/Confluence, no HTTP endpoint). The full proposed README content was supplied in the conversation but **is not independently verified as applied**.

For a new desktop *before* those files are published, the existing and verified editable installation remains:

```bash
git clone https://github.com/shared-wks/engineering-context-mcp.git
cd engineering-context-mcp
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m pytest -v
python -m engineering_context_mcp.client
```

Use `python -m pip install -r requirements-dev.txt` **only after** that file has been added and pushed. A private SSH key for the original Mac should **never** be copied to the desktop; use HTTPS to clone public code, then configure a new per-machine SSH key if push access is needed.

### Regenerate the Python 3.14 constraints file

```bash
python -m pip install pip-tools
pip-compile --strip-extras --extra dev \
  --output-file requirements/dev-py314.txt pyproject.toml
```

`--strip-extras` matters when the generated file is used with pip's `-c` **constraints** flag: the original generation failed with `ERROR: Constraints cannot have extras`.

### Optional MCP Inspector (Node.js required)

```bash
npx @modelcontextprotocol/inspector \
  ./venv/bin/python -m engineering_context_mcp.server
```

See `examples/inspector.md`. Do not claim this manual Inspector step has already been completed.

## 7. GitHub organization, Git and CI configuration

### GitHub organization / public repository

- GitHub user: `othmane-fathallah`.
- GitHub organization slug: **`shared-wks`**; public display name: **Shared Workspace**.
- Organization purpose: hold **multiple future public/collaborative projects**, not exclusively MCP or AI.
- Repository: **`shared-wks/engineering-context-mcp`**, set **Public**, MIT license.
- Topics visible in screenshot: `python`, `mcp`, `model-context-protocol`, `mcp-server`, `ai-engineering`, `integration-testing`.
- Personal GitHub account has multi-factor authentication and a passkey; organization requires 2FA and secure methods.
- Member privileges were reviewed and recommendations made (base permissions None, limit risky repository admin actions). **Recheck settings in GitHub** if exact effective values matter; screenshots did not independently confirm all saves.
- Contact/billing email was configured separately from the GitHub login; keep private contact information out of public project documents unless deliberately published.
- The Git author uses a verified professional email. Commits can expose author addresses publicly; use an appropriately verified email or a platform-specific noreply address based on privacy preference.

### Git authentication

- Dedicated personal GitHub SSH key names: `~/.ssh/id_ed25519_github_personal` (private) and `.pub` (public).
- `~/.ssh/config` contains a `Host github.com` entry selecting the dedicated private key, with `IdentitiesOnly yes`, `AddKeysToAgent yes` and `UseKeychain yes`.
- Successful verification: `ssh -T git@github.com` returned the user's GitHub account identity and confirmed authentication.
- The GitHub `origin` remote uses the SSH URL below. Verify current local state with `git remote -v` before editing it.

```bash
git remote -v
git branch --show-current
git log --oneline --decorate -5
git tag -n
git status
```

Expected GitHub remote:

```text
origin  git@github.com:shared-wks/engineering-context-mcp.git (fetch)
origin  git@github.com:shared-wks/engineering-context-mcp.git (push)
```

### GitHub Actions

- Workflow file: `.github/workflows/ci.yml`.
- Workflow name: **Python CI**.
- Existing initial matrix targeted **Python 3.12 and Python 3.13** on Linux, ran installation, Ruff linting and pytest. Do not assume Python 3.14 or formatting checks run in CI unless the workflow is updated and verified.
- Latest supplied screenshots show **Python CI #1 and #2 both successful** (green checks), corresponding to the initial release push and the README roadmap update.
- Links: [repository Actions](https://github.com/shared-wks/engineering-context-mcp/actions), [public repository](https://github.com/shared-wks/engineering-context-mcp).
- Future improvements: current supported action versions, Python 3.14 job, formatting check, `pip check`, dependency caching, minimum permissions, PR validation, and eventually database/container integration tests.

### Account recovery follow-up

Verify that GitHub account recovery codes have been refreshed as appropriate, and are securely backed up. That final verification has **not been independently confirmed**. Never copy recovery codes, private keys, passwords, tokens, or `.env` contents into this document, GitHub, GitLab, AI prompts, issues or screenshots.

## 8. Publishing workflow and dual-remote strategy

### Current status

- **GitHub:** organization/repository created, public, pushed, tag present, initial two CI runs succeeded.
- **GitLab group:** **created and confirmed public**: [Shared Workspace `shared-wks`](https://gitlab.com/shared-wks). GitLab group ID observed: `144466068`.
- **GitLab project:** **not created**. Live lookup of `shared-wks/engineering-context-mcp` returned `404 Project Not Found`; group project list was empty.
- **GitLab SSH remote and CI:** **not yet configured/verified**.
- **Local:** keep one working checkout only; **do not** create a separate codebase for GitLab.

### GitLab publication steps (group done; repository pending)

1. **DONE:** Created a **public** GitLab group named **Shared Workspace**, URL path `shared-wks` (`https://gitlab.com/shared-wks`). Do not attempt to re-create it.
2. **NEXT:** Click **Create project** from the existing group page, choose **Create blank project**, set name/slug to `engineering-context-mcp`, namespace `shared-wks`, visibility **Public**, and **do not initialize with a README**. Avoid an initial remote commit that would diverge from GitHub.
3. Add root `requirements.txt` and `requirements-dev.txt` and complete the README for second-machine onboarding (see section 6); validate clean installation, Ruff and the 14 tests. These changes are proposed, not yet verified.
4. Add `.gitlab-ci.yml` **at repository root**, using a suitable Python Linux image and jobs for dependency validation, Ruff and pytest. Update GitHub CI only after reviewing the existing workflow. Commit and push changes to GitHub `main` first; verify GitHub Actions again.
5. Create a **separate** GitLab ED25519 SSH key on the Mac, register only its `.pub` half in GitLab, and add a distinct `Host gitlab.com` entry to `~/.ssh/config` without overwriting GitHub settings. Test `ssh -T git@gitlab.com` and verify host fingerprints when prompted.
6. Add a second remote named `gitlab`, and push the **same existing Git history** (not an import-created independent history) to GitLab.
7. Push release tags explicitly (at least `v0.1.0`) and verify histories, file contents, and the real GitLab pipeline. GitLab runner availability may require setup/checks.
8. Keep GitHub as the primary remote `origin`, GitLab as `gitlab`; no automatic bidirectional synchronization until explicitly chosen.

After the blank GitLab project and SSH authentication are confirmed:

```bash
# Use the verified public group path, shared-wks.
git remote add gitlab git@gitlab.com:shared-wks/engineering-context-mcp.git
git push gitlab main
git push gitlab v0.1.0

# Normal future publishing:
git push origin main
git push gitlab main
```

**Never force-push** simply to make the two hosts match; reconcile differences intentionally.

## 9. Planned application architecture: v0.2 and beyond

### v0.2 — Containerized backend (next engineering milestone)

Planned minimum viable services:

```text
        MCP client / local test runner
                    │
        MCP application container
      Python + FastMCP + service layer
                    │
          SQLAlchemy repository
                    │
            PostgreSQL container
             persistent volume

    Docker Compose + health checks
    Alembic migration management
```

Build these **incrementally** while keeping v0.1 tests valid. At v0.2, retain stdio as one supported transport; remote Streamable HTTP becomes a separate follow-on feature.

**Suggested acceptance criteria for v0.2** (not implemented yet):

- Application Docker image built for the Mac's ARM64 platform and capable of running in Linux CI.
- Compose starts an application service and PostgreSQL with a health check, named volume and private network.
- Database configuration comes from environment variables / local secret configuration and contains no committed credentials.
- SQLAlchemy models/repositories isolate persistence from MCP tools.
- Alembic migrations can create a clean schema from scratch; migrations are idempotently managed, not manually applied table DDL scattered through code.
- Existing MCP operations persist data across **application** restarts (while PostgreSQL volume remains intact).
- Tests cover persistence, migrations, invalid inputs and protocol behavior; integration tests run against an isolated test database/container.
- CI validates container build and persistence tests, with clear development commands in README.
- Logs do not print sensitive values; containers have appropriate health/readiness behavior and avoid unnecessary privileged access.

**Do not** add Redis, Kafka, Kubernetes, microservices, or a cloud provider until a concrete capability requires them.

### Roadmap (agreed, updated in README)

| Milestone | Plan | Status |
|---|---|---|
| **v0.1.0 — MCP Foundation** | Python MCP server/client, tools, resources, prompt, tests, basic CI | **Implemented / public** |
| **v0.2.0 — Containerized Backend** | Docker, Compose, PostgreSQL, SQLAlchemy, Alembic | **Next — planned** |
| **v0.3.0 — Networked MCP Service** | Streamable HTTP, config, health checks, logging | Planned |
| **v0.4.0 — Atlassian Integrations** | Jira and Confluence REST APIs via safe adapters | Planned |
| **v0.5.0 — Engineering Workflows** | Cross-service search/context aggregation and workflow automation | Planned |
| **v1.0.0 — Production-ready release** | Auth/security, observability, CI/CD, docs, demo | Planned |

### Jira/Confluence integration boundaries

- Use personal/test Atlassian Cloud projects and spaces first; no Rovo license is required for a separate open-source MCP server.
- Begin with read-only issue search/retrieval and Confluence page retrieval; add mutations only after validating authorization and safety boundaries.
- Never expose real employer/client issues, screenshots, credentials or confidential specifications in a public repository or an unauthorized third-party AI workflow.
- Authorization must come from provider/credential scopes and app enforcement; project filters alone are not a sufficient security boundary.

## 10. Known pitfalls encountered (and fixes)

| Symptom | Root cause / lesson | Resolution |
|---|---|---|
| Ruff `SIM117` | Nested `async with` contexts | Combine into one multi-context `async with` block. |
| Ruff `I001` | Unsorted imports | `python -m ruff check . --fix`, then format/check. |
| MCP test `assert len(tasks) == 1` returned 3 | Parsed first text block as a dict, not a task list | Parse returned `TextContent` blocks (or SDK structured result when supported). |
| `Constraints cannot have extras` | `pip-compile` output had extras not accepted via `pip -c` | Regenerate with `pip-compile --strip-extras`. |
| SSH public key rejected as invalid | Clipboard replaced after copying another terminal command | Run `pbcopy < key.pub`, then paste immediately; key fingerprint verified with `ssh-keygen -lf`. |
| Shell showed clipboard text `pbpaste` | Copying the next command replaced clipboard data | Combine copy-and-test in one command, or type verification command without copying. |
| Renaming virtualenv-based project | Virtual env scripts can embed absolute old paths | Recreate `venv` at renamed project path and reinstall editable package. |
| Local tests passed but CI unseen | Local validation is not remote CI validation | Inspect actual GitHub/GitLab run and individual jobs. |

## 11. Exact recommended next actions

### First: preserve this handover in GitHub

Copy this Markdown file into the local repository as `docs/PROJECT_HANDOVER.md`, then:

```bash
cd ~/myprojects/poc/engineering-context-mcp
git status
git add docs/PROJECT_HANDOVER.md
git diff --cached --check
git diff --cached --stat
git commit -m "docs: add project handover and continuity guide"
git push origin main
```

Optionally add this line under README's Documentation section and commit it with the handover:

```markdown
See [Project Handover](docs/PROJECT_HANDOVER.md) for setup history, verified milestones and the next development steps.
```

This handover describes current status **as of 11 October 2026**, not a continuously synchronized inventory. Update the snapshot/date and checkboxes after future milestones.

### Then: finish the dual public publishing setup

- [x] **GitLab public group** created: `https://gitlab.com/shared-wks`, display name Shared Workspace.
- [ ] **GitLab blank public project** `shared-wks/engineering-context-mcp` — next browser action: **Create project** within the group.
- [ ] Add root `requirements.txt` and `requirements-dev.txt`; update README with working setup instructions for a second desktop and third-party developers; confirm with a clean `venv` test.
- [ ] Create `.gitlab-ci.yml` at repository root and review GitHub CI installation consistency; commit to `main` and push to GitHub.
- [ ] Configure/verify a separate GitLab SSH key and local `gitlab` remote (do not disturb working `origin`).
- [ ] Push `main` and the existing `v0.1.0` tag to GitLab and verify matching commit IDs with GitHub.
- [ ] Confirm the GitLab pipeline and subsequent GitHub Actions jobs actually pass.
- [ ] Review GitHub organization member privileges, recovery-code rotation, and branch protection if not yet independently confirmed.
- [ ] Optional polish: published release notes, README badges, minimal workflow permissions, CI dependency upgrades.

### Then: begin v0.2 technical design and implementation

- [ ] Write `docs/adr/` architecture decisions for persistence, transport and migrations.
- [ ] Choose supported PostgreSQL major version and pin container images intentionally.
- [ ] Introduce application configuration (`pydantic-settings` or similar), avoiding real `.env` commits.
- [ ] Implement Dockerfile, `.dockerignore`, `compose.yaml`, and PostgreSQL health checks.
- [ ] Add SQLAlchemy persistence abstraction and Alembic migration(s).
- [ ] Preserve current MCP contracts; refactor domain/service/persistence layers incrementally.
- [ ] Write PostgreSQL integration tests and add them to CI, then demonstrate restart persistence.
- [ ] Update architecture docs and README with exact reproducible commands and CI status.

## 12. Safe restart instructions for any new chat / AI coding assistant

Copy the following prompt into a future conversation, and attach this file (plus current `README.md`, `pyproject.toml` and any recently changed files if code changes are requested):

> Continue development of **Engineering Context MCP**. Read the attached `docs/PROJECT_HANDOVER.md` first. The project uses standard Python `venv` and `pip`, not `uv`. It is a public portfolio project under GitHub `shared-wks/engineering-context-mcp`. v0.1.0 implements an in-memory FastMCP server and Python stdio client, with 8 unit tests and 6 protocol integration tests (14 passing), Ruff, a Python 3.14 constraints file, and working GitHub CI. The public GitLab group `shared-wks` now exists; **creating the blank GitLab project** is the next step. Root `requirements.txt` / `requirements-dev.txt`, fuller onboarding README, `.gitlab-ci.yml`, GitLab SSH/push/CI and the v0.2 Docker/Compose/PostgreSQL/SQLAlchemy/Alembic backend remain unverified/planned. **Do not assume planned features exist.** Respect the business goal of connecting engineering context from Jira/Confluence, avoid SQLite, preserve tests, and provide exact project paths and copyable files. Ask for the latest `git status`, `git log`, and relevant files when facts may have changed. Keep credentials out of chat and the repository.

### Recommended fresh-session verification commands

```bash
cd ~/myprojects/poc/engineering-context-mcp
git status --short
git log --oneline --decorate -5
git remote -v
git tag -n
source venv/bin/activate
python -m pip check
python -m ruff check .
python -m ruff format --check .
python -m pytest -v
```

### Handover update log

| Date | Event | Evidence / validation |
|---|---|---|
| 2026-10-11 (earlier) | First handover written after GitHub `main` push, `v0.1.0`, and two successful GitHub CI runs | User screenshots and local command outputs in original setup conversation. |
| 2026-10-11 (current update) | **Public GitLab group created**: Shared Workspace / `shared-wks` | Group page screenshot and connected GitLab `get_group` lookup (`public`; empty projects), plus project lookup 404. |
| 2026-10-11 (current update) | Portable installation / README / GitLab CI requested and drafted | Draft instructions exist in chat; **no proof yet that files have been committed**. |

**Rule for future documentation:** mark items **verified**, **reported by user**, or **planned/unverified**. Never silently convert plans into accomplishments. Update this handover whenever a release or infrastructure milestone is completed.
