# Engineering Context MCP — Project Handover & Continuity Guide

> **Snapshot:** 11 October 2026, updated after **successful dual-platform publication and GitLab CI**.  
> **Project status:** v0.1.0 foundation published under `shared-wks` on **GitHub and GitLab**. The two `main` refs and annotated `v0.1.0` tags have been verified identical via local `git ls-remote`. GitLab CI has a successful `quality` and `tests` pipeline. **Docker/PostgreSQL and Jira/Confluence integrations remain planned**, not implemented.  
> **Purpose:** Keep all setup history, architectural choices, verified work, environment setup, current limitations, and upcoming actions available to future developers and AI sessions.  
> **File location:** `docs/PROJECT_HANDOVER.md`. A previous version is present in the public repositories; **this updated version must be copied into the local checkout and pushed to both**.

## 1. Read this first: current state

**Project:** Engineering Context MCP  
**Distribution / repository:** `engineering-context-mcp`  
**Python import package:** `engineering_context_mcp`  
**GitHub organization:** [Shared Workspace (`shared-wks`)](https://github.com/shared-wks)  
**GitHub repo (Public):** https://github.com/shared-wks/engineering-context-mcp  
**GitLab group:** [Shared Workspace (`shared-wks`)](https://gitlab.com/shared-wks), Public, group ID `144466068`  
**GitLab repo (Public):** https://gitlab.com/shared-wks/engineering-context-mcp, project ID `87479265`  
**Local workspace on original personal Mac:** `~/myprojects/poc/engineering-context-mcp`  
**Default branch:** `main`  
**Release tag:** annotated `v0.1.0`  
**License:** MIT

### Verified Git reference integrity (11 Oct 2026)

The user ran `git rev-parse main` and `git ls-remote` against **both** remotes. All three branch IDs were identical:

```text
main (local, origin and gitlab)
73db8f944f029fd77db556cf7eab906bb21bb2c9

annotated tag ref v0.1.0 (origin and gitlab)
39b080abcaff1e98c128e223fd97f989e99da427
```

The GitLab API independently confirmed `main` at `73db8f9...`, `v0.1.0` **tag object** at `39b080a...`, and the tag's **target commit** at `424044936356ff111488a3a5fb4892ea148978a7`. The tag intentionally references the initial release, not today's later `main` tip.

### Verified as completed

- [x] Created a standalone Python project with a `src/` package layout, managed using **`venv` + `pip`** (not `uv`).
- [x] Implemented a functional MCP stdio server/client: **4 tools, 2 resources, 1 prompt**.
- [x] Implemented **8 unit tests** and **6 real protocol/subprocess integration tests** (14 passing in local validation).
- [x] Validated `pip check`, Ruff lint/format, and Python dependency installation locally.
- [x] Added `requirements/dev-py314.txt` with `pip-tools` / `--strip-extras` constraints.
- [x] Created public GitHub `shared-wks/engineering-context-mcp`, set up working SSH and published `main` and annotated `v0.1.0`.
- [x] Observed two initial green GitHub Actions `Python CI` runs; README Docker/PostgreSQL roadmap and six GitHub topics published.
- [x] Created and configured public-facing GitHub organization **Shared Workspace**, with secure organization-wide 2FA; personal GitHub 2FA/passkey configured.
- [x] Created **Public GitLab group** `shared-wks` / **Shared Workspace**.
- [x] Created **Public GitLab project** `shared-wks/engineering-context-mcp` as an empty repository (no remote README/initial commit).
- [x] Generated a separate Mac GitLab ED25519 SSH key, registered its public half, and successfully authenticated with `ssh -T git@gitlab.com`.
- [x] Added GitLab SSH remote `gitlab` without disturbing GitHub `origin` (which remains `main`'s upstream).
- [x] Pushed existing `main` and `v0.1.0` to GitLab, and verified **matching full branch/tag SHAs on GitHub and GitLab**.
- [x] Published root **`requirements.txt`** and **`requirements-dev.txt`**, with thin editable-install references to `pyproject.toml`.
- [x] Published expanded README with clone/venv/install/run/pytest/Ruff instructions and explicit in-memory limits.
- [x] Published **`.gitlab-ci.yml`** with independent `quality` and `tests` jobs.
- [x] **GitLab pipeline 2935094589 succeeded** on commit `73db8f9...`, with both jobs reported successful by live GitLab lookup.
- [x] Published the **previous** `docs/PROJECT_HANDOVER.md` on GitLab's `main` (also covered by the matching GitHub branch tip); this current updated copy still needs a documentation commit.

### Still pending / not yet implemented

- [ ] Apply **this newly updated handover** to local `docs/PROJECT_HANDOVER.md`, commit and push to both remotes.
- [ ] Verify a **fresh clean clone/install/client smoke test on the second desktop** (portable instructions are published, but actual second-machine validation is not established).
- [ ] Confirm the **latest GitHub Actions workflow** status after the recent portable-setup/CI commits; the earlier two green runs are confirmed, but the latest run is not independently checked here.
- [ ] Align GitHub Actions installation with `requirements-dev.txt` if desired; live published `.github/workflows/ci.yml` still installs `-e ".[dev]"` and tests Python 3.12/3.13.
- [ ] Dockerfile, Docker Compose services, PostgreSQL, SQLAlchemy, Alembic migrations, and persistent task storage.
- [ ] Streamable HTTP/networked MCP service, Jira and Confluence adapters, production auth/security and observability.
- [ ] GitHub protected branch/rulesets, a formal GitHub Release, extra security scans, and production hardening (not confirmed).
- [ ] Confirm account recovery codes are stored securely and replaced if they were ever exposed.

**Critical distinction:** GitLab dual publication and CI **are completed**, but the running app is still an **in-memory, local stdio MCP demonstration**. It is not yet a production-ready Jira/Confluence integration.

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
| Portable requirements and onboarding README | **Published** on both remotes (confirmed by GitLab tree and file content). Second-desktop fresh install remains untested. |
| GitLab repository, SSH, CI | **Implemented and verified.** Public project, working SSH key and second remote, matching `main`/tag, passing `quality`/`tests` pipeline. |
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
16. **GitLab group created (11 Oct 2026):** Created Public `shared-wks` / Shared Workspace group (ID `144466068`).
17. **GitLab public project created:** Created blank Public repository `shared-wks/engineering-context-mcp` (ID `87479265`), without initializing a README or divergent commit.
18. **Portable onboarding files now published:** The latest synchronized `main` includes `requirements.txt` (`-e .`), `requirements-dev.txt` (`-e .[dev]`), a significantly expanded README (including fresh clone/venv/install/client/test instructions), and `.gitlab-ci.yml`.
19. **GitLab SSH and remotes:** On the original Mac, created `~/.ssh/id_ed25519_gitlab_personal` (+ `.pub`) and added `Host gitlab.com` in SSH config, preserving `Host github.com`. `ssh -T git@gitlab.com` returned a successful GitLab welcome message. GitLab key was configured without an expiration date; if the device is lost or compromised, revoke it from GitLab. Added `gitlab` remote; existing `origin` continues to point to GitHub.
20. **First GitLab push and synchronization (11 Oct 2026):** `git push gitlab main` and `git push gitlab v0.1.0` succeeded. Full `main` branch ID `73db8f944f029fd77db556cf7eab906bb21bb2c9` and annotated tag ref `39b080abcaff1e98c128e223fd97f989e99da427` were identical on both hosts. This is verified both by terminal logs and live GitLab branch/tag lookup.
21. **GitLab CI passing:** GitLab pipeline `2935094589` succeeded on `main` at `73db8f9...` with distinct `quality` and `tests` jobs both successful. The user still needs to test a clean clone on the desktop, and future CI changes should be verified on both hosts.
22. **Handover continuity:** An earlier `docs/PROJECT_HANDOVER.md` is already published on synchronized `main`; **this new status update** is a replacement that must be committed and pushed to GitHub and GitLab.
23. **Next engineering milestone:** Validate desktop onboarding; prepare Docker/Compose/PostgreSQL persistence using SQLAlchemy/Alembic. Jira/Confluence and HTTP transport remain later releases.

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
│   └── PROJECT_HANDOVER.md        # old version already published; replace with this update
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
├── .gitlab-ci.yml                 # GitLab quality + test pipeline (published)
├── requirements.txt               # -e . (published)
├── requirements-dev.txt           # -e .[dev] (published)
├── LICENSE                        # MIT
├── README.md
├── pyproject.toml                 # setuptools, dependencies, scripts, tool config
└── venv/                          # local ONLY; ignored by Git
```

**Verified present on GitLab `main` at `73db8f9...` (and therefore on identical GitHub `main`):** `.gitlab-ci.yml`, `requirements.txt`, `requirements-dev.txt`, `docs/PROJECT_HANDOVER.md`. **Not implemented:** `Dockerfile`, `compose.yaml`, database migrations, Jira/Confluence integrations, and real `.env` files. The old handover in Git must be replaced by this newer document.

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

### Portable installation and second-desktop onboarding (published; remote test pending)

The root requirements files are **present in GitLab `main`**, and the user's local Git history matches both remotes:

`requirements.txt`:

```text
# Install the application using dependencies from pyproject.toml
-e .
```

`requirements-dev.txt`:

```text
# Install application and development dependencies
-e .[dev]
```

The expanded `README.md` on GitLab `main` documents HTTPS/SSH cloning, `venv` creation and activation for macOS/Linux/Windows, pip installation, `python -m engineering_context_mcp.client`, direct MCP server launch, MCP Inspector, pytest, Ruff and the in-memory limitation. It describes v0.2 Docker/PostgreSQL as planned, not done. **Actual fresh-clone installation on the second desktop is still pending.**

**Recommended first-time desktop test (Ubuntu/Linux):**

```bash
mkdir -p ~/myprojects/poc
cd ~/myprojects/poc
git clone https://github.com/shared-wks/engineering-context-mcp.git
cd engineering-context-mcp
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pip check
python -m pytest -v
python -m ruff check .
python -m ruff format --check .
python -m engineering_context_mcp.client
```

This uses HTTPS only for public cloning. If changes will be pushed from the second desktop, configure that machine's **own** SSH key(s) and verified Git author identity—do not transfer a private key from the Mac or copy its `venv/` directory. Root requirements files delegate dependency metadata to `pyproject.toml`; they are **not universal immutable locks**. Python 3.14 local constraints remain separate under `requirements/`.

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
- The **published** workflow (verified from GitLab mirror) targets **Python 3.12 and Python 3.13** on Linux, uses `python -m pip install -e ".[dev]"`, runs Ruff lint and pytest. It **has not yet been changed** to use `requirements-dev.txt`, or add a Python 3.14 job, `ruff format --check` or `pip check`.
- Earlier screenshots showed **Python CI #1 and #2 both successful** (green checks). The latest workflow result after subsequent portable-install/CI commits is **not independently checked** in this handover; verify it before claiming full dual-CI completion.
- Links: [repository Actions](https://github.com/shared-wks/engineering-context-mcp/actions), [public repository](https://github.com/shared-wks/engineering-context-mcp).
- Future improvements: current supported action versions, Python 3.14 job, formatting check, `pip check`, dependency caching, minimum permissions, PR validation, and eventually database/container integration tests.

### Account recovery follow-up

Verify account recovery codes are securely stored, and replace any that have been exposed. Never copy recovery codes, private keys, passwords, tokens, or `.env` contents into this document, GitHub, GitLab, AI prompts, issues or screenshots.

## 8. Publishing workflow and dual-remote strategy

### Current result — both repositories published and synchronized

| Property | GitHub (`origin`) | GitLab (`gitlab`) |
|---|---|---|
| Public repository | https://github.com/shared-wks/engineering-context-mcp | https://gitlab.com/shared-wks/engineering-context-mcp |
| Group / organization | `shared-wks` | `shared-wks` |
| SSH URL | `git@github.com:shared-wks/engineering-context-mcp.git` | `git@gitlab.com:shared-wks/engineering-context-mcp.git` |
| `main` commit | `73db8f944f029fd77db556cf7eab906bb21bb2c9` | **Same SHA** |
| Annotated `v0.1.0` ref | `39b080abcaff1e98c128e223fd97f989e99da427` | **Same SHA** |
| CI | Two earlier successful GitHub runs seen | Pipeline **2935094589 successful** (`quality`, `tests`) |

**GitLab facts verified live:** project ID `87479265`; public visibility; default branch `main`; non-empty repository. GitLab's `main` branch SHA is `73db8f9...`; annotated `v0.1.0` tag object SHA `39b080a...`, pointing to initial commit `424044936356ff111488a3a5fb4892ea148978a7`. Pipeline [2935094589](https://gitlab.com/shared-wks/engineering-context-mcp/-/pipelines/2935094589) has status **success**, triggered by push to `main`, with jobs `quality` and `tests` both **success**.

### SSH setup on the original Mac

GitHub key (already working):

```text
~/.ssh/id_ed25519_github_personal      # PRIVATE, never share
~/.ssh/id_ed25519_github_personal.pub  # public registration key
```

GitLab key (already working):

```text
~/.ssh/id_ed25519_gitlab_personal      # PRIVATE, never share
~/.ssh/id_ed25519_gitlab_personal.pub  # public registration key
```

`~/.ssh/config` has distinct `Host github.com` and `Host gitlab.com` entries, each selecting its own key. The GitLab key was added to the GitLab account and `ssh -T git@gitlab.com` confirmed successful authentication. The SSH key was added without an expiration date as requested. Verify the private key has a passphrase, appropriate filesystem permissions and a secure backup policy. Revoke it from GitLab if the Mac is lost or compromised.

**Account note:** The successful local SSH push establishes which GitLab account has access to this project. When using any additional GitLab integration or connector, verify its authenticated account and project permissions separately.

### Publishing commands for future development

```bash
cd ~/myprojects/poc/engineering-context-mcp
git status
git remote -v
# After local tests and a new commit:
git push origin main
git push gitlab main
# Publish new version tags explicitly when a release is ready:
# git push origin vX.Y.Z
# git push gitlab vX.Y.Z
```

`origin` is the default upstream for local `main`. The `gitlab` remote is for deliberate mirrored pushes. **No automatic synchronization or forced rewrites.** Always verify full SHA parity after significant pushes:

```bash
git rev-parse main
git ls-remote origin refs/heads/main
git ls-remote gitlab refs/heads/main

git ls-remote --tags origin 'refs/tags/v0.1.0'
git ls-remote --tags gitlab 'refs/tags/v0.1.0'
```

Do not re-create/move `v0.1.0`. It labels the initial historical release. Later docs, requirements and CI commits stay on `main` until a future release tag is intentionally created.

### GitLab CI file and observed results

The published root `.gitlab-ci.yml` uses `python:3.13-slim`, pip installs `requirements-dev.txt`, and runs these separate jobs:

- `quality`: `pip check`, `ruff check .`, `ruff format --check .`.
- `tests`: `pytest -v`.

Live GitLab status: **pipeline 2935094589 SUCCESS**, both jobs SUCCESS, on `main` SHA `73db8f9...`. Check the job logs for detailed test counts whenever needed; job success alone does not specify an exact number of collected tests.

Next improvement is ensuring both providers run the same test/check set, updating GitHub Actions deliberately and re-validating hosted CI. The portable README has already been published; the clean desktop installation remains to be tested.

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

### First: commit **this updated** handover to both repositories

The earlier `docs/PROJECT_HANDOVER.md` already exists on published `main`, but it still reports GitLab as pending. Download this replacement into the original local checkout:

```bash
cd ~/myprojects/poc/engineering-context-mcp
# If saved into ~/Downloads, for example:
cp ~/Downloads/PROJECT_HANDOVER.md docs/PROJECT_HANDOVER.md
git status
git diff -- docs/PROJECT_HANDOVER.md
# Check for accidental secrets, credentials or sensitive local data.
git add docs/PROJECT_HANDOVER.md
git diff --cached --check
git commit -m "docs: record successful dual-platform publication and GitLab CI"
git push origin main
git push gitlab main
```

Verify the two new `main` refs again after the push. This is a **new docs commit on `main`**, not a modification to `v0.1.0`.

### Then: validate onboarding and CI

- [x] Public GitHub organization/repository and first release tag.
- [x] Public GitLab group and project.
- [x] GitLab SSH key and working SSH authentication.
- [x] Two Git remotes with synchronized `main` and `v0.1.0` SHAs (at snapshot).
- [x] Root `requirements.txt`, `requirements-dev.txt`, and developer-friendly README published.
- [x] `.gitlab-ci.yml` published and GitLab pipeline **2935094589** successful (`quality`, `tests`).
- [x] Earlier GitHub `Python CI` runs #1 and #2 successful.
- [ ] Push this latest handover update to **both** platforms; re-check SHA parity.
- [ ] Check GitHub Actions **most recent** workflow status and inspect failures or warnings if any.
- [ ] Fresh clone and run on second desktop (Python 3.12+; Linux/macOS/Windows instructions as appropriate), including 14 automated tests and an MCP client smoke test.
- [ ] Consider aligning GitHub CI with `requirements-dev.txt`, `ruff format --check`, `pip check` and an additional Python 3.14 job; only mark complete after CI success.
- [ ] Review GitHub membership permissions, secure recovery-code storage, repository protection/rulesets and security scanning.
- [ ] Optionally create a formal GitHub Release for `v0.1.0`, and add a GitLab pipeline status badge to README.

### Then: begin v0.2 engineering work (not started)

- [ ] Write `docs/adr/` architecture decision records for persistence, SQLAlchemy/repositories and migrations.
- [ ] Choose and pin PostgreSQL/container image versions, design `compose.yaml` and persistent volumes.
- [ ] Add Dockerfile, `.dockerignore`, app config and Compose health checks.
- [ ] Implement SQLAlchemy and Alembic migrations with repository/service layers.
- [ ] Keep MCP tool contracts and the current 14 tests valid; add PostgreSQL integration and restart-persistence tests.
- [ ] Extend both CI pipelines to exercise the backend containers; confirm clean fresh-install and development workflows.
- [ ] Update README/architecture/handover as each deliverable is completed.

## 12. Safe restart instructions for any new chat / AI coding assistant

Copy this prompt into a future conversation and attach this updated `docs/PROJECT_HANDOVER.md` plus any files being actively edited:

> Continue **Engineering Context MCP**. Read `docs/PROJECT_HANDOVER.md` first; it is the project continuity source. Use standard Python `venv` and `pip`, not `uv`. The public **GitHub and GitLab** repositories both use namespace `shared-wks/engineering-context-mcp`; local Git remotes are `origin` (GitHub upstream) and `gitlab` (GitLab), with one checkout. At the last verified snapshot, both `main` refs were `73db8f944f029fd77db556cf7eab906bb21bb2c9` and annotated `v0.1.0` tag objects were `39b080abcaff1e98c128e223fd97f989e99da427`. Root `requirements.txt`/`requirements-dev.txt`, expanded README and `.gitlab-ci.yml` are published. GitLab pipeline 2935094589 succeeded with `quality` and `tests` jobs; earlier GitHub Python CI runs were green. The functional app remains a **local in-memory FastMCP stdio server/client** with 4 tools, 2 resources, 1 prompt, 8 unit tests and 6 integration tests. **Do not claim PostgreSQL, Docker deployment, Streamable HTTP, Jira or Confluence are implemented.** The next steps are to commit any newer handover, confirm latest GitHub Actions, test fresh desktop installation, then design v0.2 with Docker/Compose/PostgreSQL/SQLAlchemy/Alembic rather than SQLite. Preserve history and the `v0.1.0` tag; verify `git status`, latest commits and CI before changes. Never share private SSH keys, `.env` values or recovery codes.

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
| 2026-10-11 (early) | First public GitHub release and two initial successful GitHub CI runs | Terminal commands and screenshots |
| 2026-10-11 (mid) | Public GitLab group `shared-wks` created | GitLab UI and live group lookup; ID `144466068` |
| 2026-10-11 (later) | Public GitLab project created, separate SSH registered, `gitlab` remote added | GitLab project lookup and user's terminal SSH/remote output |
| 2026-10-11 (later) | First GitLab `main` and `v0.1.0` pushes succeeded | User's `git push` output; full branch SHA and annotated tag object SHA matched GitHub |
| 2026-10-11 (verified live) | README, portable requirement files, old handover and `.gitlab-ci.yml` present | GitLab repository tree and file reads at `73db8f9...` |
| 2026-10-11 (verified live) | **GitLab CI pipeline 2935094589 succeeded**; `quality` and `tests` jobs both successful | Live GitLab pipeline and jobs lookup on `main` SHA `73db8f9...` |
| 2026-10-11 (this document) | Continuity handover updated to show dual-publication milestone | This replacement Markdown/Word copy; Git commits to publish this update still pending |

**Rule for future documentation:** mark items **verified**, **reported by user**, or **planned/unverified**. Never silently convert plans into accomplishments. Update this handover whenever a release or infrastructure milestone is completed.
