# Engineering Context MCP — Project Handover & Continuity Guide

> **Snapshot:** 12 October 2026, after **successful Ubuntu desktop reproduction and SSH authentication on GitHub and GitLab**.  
> **Project status:** v0.1.0 MCP foundation is published under `shared-wks` on **GitHub and GitLab**, and reproducibly installed/tested on a second machine running **Ubuntu / Python 3.14.4**. All **14 tests**, Ruff checks, `pip check`, and the live stdio client/server demo passed on Ubuntu. The latest GitLab commit verified here is `aaaef73ba81c41275a28bacdacad76bdafbaaedc` with **successful pipeline 2935106858** (`quality`, `tests`). **Ubuntu GitLab and GitHub SSH authentication are now verified**. GitLab `origin` was switched from HTTPS to SSH, and `git ls-remote origin HEAD` succeeded at `aaaef73...`. **Git push from Ubuntu has not been tested**; adding a GitHub remote, retiring the old GitLab key, and verifying local Git author configuration remain follow-ups. Docker/PostgreSQL and Jira/Confluence are planned, not implemented.  
> **Purpose:** Keep all setup history, architectural choices, verified work, environment setup, current limitations, and upcoming actions available to future developers and AI sessions.  
> **File location:** `docs/PROJECT_HANDOVER.md`. The preceding handover revision was published in commit `aaaef73`; **this refreshed 12 October update is a newly generated replacement and has not been committed/pushed yet**.

## 1. Read this first: current state

**Project:** Engineering Context MCP  
**Distribution / repository:** `engineering-context-mcp`  
**Python import package:** `engineering_context_mcp`  
**GitHub organization:** [Shared Workspace (`shared-wks`)](https://github.com/shared-wks)  
**GitHub repo (Public):** https://github.com/shared-wks/engineering-context-mcp  
**GitLab group:** [Shared Workspace (`shared-wks`)](https://gitlab.com/shared-wks), Public, group ID `144466068`  
**GitLab repo (Public):** https://gitlab.com/shared-wks/engineering-context-mcp, project ID `87479265`  
**Local workspace on original personal Mac:** `~/myprojects/poc/engineering-context-mcp`  
**Validated Ubuntu desktop:** `hq-dev`, `/home/heliosquant/myprojects/poc/engineering-context-mcp`  
**Default branch:** `main`  
**Release tag:** annotated `v0.1.0`  
**License:** MIT

### Verified Git reference integrity (11–12 Oct 2026)

The user ran `git rev-parse main` and `git ls-remote` against **both** remotes. All three branch IDs were identical:

```text
main (local, origin and gitlab)
73db8f944f029fd77db556cf7eab906bb21bb2c9

annotated tag ref v0.1.0 (origin and gitlab)
39b080abcaff1e98c128e223fd97f989e99da427
```

The GitLab API independently confirmed `main` at `73db8f9...` at that comparison, `v0.1.0` **tag object** at `39b080a...`, and the tag's **target commit** at `424044936356ff111488a3a5fb4892ea148978a7`. Subsequently, the user committed/pushed the revised handover, and the **Ubuntu HTTPS clone** reported commit `aaaef73` (`docs: update handover with GitLab publication and CI`). Live GitLab lookup on 12 October confirmed the full GitLab `main` SHA `aaaef73ba81c41275a28bacdacad76bdafbaaedc` and passing CI pipeline `2935106858` with `quality` and `tests` both successful. **GitHub/GitLab parity at the newer `aaaef73` commit was not freshly checked here**; the exact SHA parity above is historical and verified.

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
- [x] Published `docs/PROJECT_HANDOVER.md`; later updated it in commit **`aaaef73`** (`docs: update handover with GitLab publication and CI`), confirmed by the fresh Ubuntu clone and live GitLab branch lookup.
- [x] Confirmed the latest GitLab pipeline **2935106858 SUCCESS** on `aaaef73`, with both `quality` and `tests` jobs successful.
- [x] **Fresh-cloned the GitLab repository via HTTPS on Ubuntu `hq-dev`** into `/home/heliosquant/myprojects/poc/engineering-context-mcp`; Git `2.53.0`, `main`, clean working tree; **initially** GitLab HTTPS `origin` (later switched to SSH).
- [x] Created and activated a dedicated Ubuntu project **`venv/`** with Python **3.14.4** (`/usr/bin/python3` on host); installed requirements with `python -m pip install -r requirements-dev.txt` in editable mode **without using the Mac-only constraints file**.
- [x] On Ubuntu, verified **`pip check` clean**, all **14 pytest tests passed in 2.62s** (8 unit + 6 MCP integration), **Ruff lint passed**, **11 files already formatted**, and the **stdio MCP client successfully ran** (4 tools, 2 resources, 1 prompt; sample task added/listed/resource read).
- [x] **Ubuntu GitLab SSH fixed:** The original `id_ed25519_gitlab_hqdev` key was registered but its private-key passphrase could not be verified. Replaced it with `id_ed25519_gitlab_hqdev_v2`, registered the new public key, successfully authenticated directly (`Authenticated ... using "publickey"`, `Welcome to GitLab, @othmane.fathallah.mail!`), updated `~/.ssh/config`, and added `v2` to the SSH agent. Normal `ssh -T git@gitlab.com` succeeded.
- [x] **Ubuntu GitLab remote switched to SSH:** `origin` now points to `git@gitlab.com:shared-wks/engineering-context-mcp.git`; `git ls-remote origin HEAD` returned `aaaef73ba81c41275a28bacdacad76bdafbaaedc`, and `git status` reported clean `main` up to date with `origin/main`.
- [x] **Ubuntu GitHub SSH fixed:** Existing dedicated `id_ed25519_github_hqdev` key was recognized by GitHub. The GNOME/GCR SSH agent stalled at the signing step, but direct signing using `IdentityAgent=none` succeeded after entering the private-key passphrase. After editing `~/.ssh/config`, normal `ssh -T git@github.com` also succeeded, showing `Hi othmane-fathallah! You've successfully authenticated...`.

### Still pending / not yet implemented

- [ ] Apply **this 12 October handover replacement** to `docs/PROJECT_HANDOVER.md` and add the companion `docs/PROJECT_CONTINUITY.md` if desired; commit/push from the **working Mac SSH checkout**, then confirm both remotes.
- [ ] **Retire the obsolete Ubuntu GitLab key**: remove old `id_ed25519_gitlab_hqdev` from SSH agent and revoke only the old registered public key on GitLab, matching fingerprint `SHA256:cj0ik78DVUcUOgP6loWmHoPdM8B8l6tjODcqtPXTFCE`; keep the working `v2` key (fingerprint `SHA256:5v+KsS82WFrFfNJjbHQkCleg9aNbEFEGOTEJNyHjPgY`) and Raspberry Pi key intact. Retirement has not been confirmed.
- [ ] **Ubuntu GitHub repository access (`git ls-remote`), adding the `github` remote, and verifying project-local Git author settings** remain unconfirmed. Both providers' `ssh -T` logins succeeded, but **neither a Git push from Ubuntu nor a GitHub repository-read command has been verified**.
- [ ] Optionally refine GitHub SSH-agent support. Current `ssh -T` works with a passphrase prompt and agent-bypass configuration; this is functional and need not block development.
- [ ] Confirm the **latest GitHub Actions workflow** status after the recent portable-setup/CI commits; the earlier two green runs are confirmed, but the latest run is not independently checked here.
- [ ] Align GitHub Actions installation with `requirements-dev.txt` if desired; live published `.github/workflows/ci.yml` still installs `-e ".[dev]"` and tests Python 3.12/3.13.
- [ ] Dockerfile, Docker Compose services, PostgreSQL, SQLAlchemy, Alembic migrations, and persistent task storage.
- [ ] Streamable HTTP/networked MCP service, Jira and Confluence adapters, production auth/security and observability.
- [ ] GitHub protected branch/rulesets, a formal GitHub Release, extra security scans, and production hardening (not confirmed).
- [ ] Confirm account recovery codes are stored securely and replaced if they were ever exposed.

**Critical distinction:** GitLab publication/CI, Ubuntu fresh-install validation, and **both Ubuntu SSH login tests are complete**. Successful `ssh -T` and remote reads do **not** demonstrate a successful Ubuntu Git push. The running app is still an **in-memory, local stdio MCP demonstration**, not a production-ready Jira/Confluence integration.

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
| Portable requirements and onboarding README | **Published and successfully exercised on Ubuntu `hq-dev`** with Python 3.14.4, unpinned pip install, 14 passing tests, Ruff and MCP smoke test. |
| GitLab repository, Mac SSH, CI | **Implemented and verified.** Public project, working **Mac** SSH key and second remote, previously matching `main`/tag, passing `quality`/`tests` pipelines (including latest #2935106858). **Ubuntu GitLab SSH works with replacement `v2` key; Ubuntu GitHub SSH works by bypassing a stalled agent.** |
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
18. **Portable onboarding files now published:** The previously synchronized `main` includes `requirements.txt` (`-e .`), `requirements-dev.txt` (`-e .[dev]`), a significantly expanded README (including fresh clone/venv/install/client/test instructions), and `.gitlab-ci.yml`.
19. **GitLab SSH and remotes:** On the original Mac, created `~/.ssh/id_ed25519_gitlab_personal` (+ `.pub`) and added `Host gitlab.com` in SSH config, preserving `Host github.com`. `ssh -T git@gitlab.com` returned a successful GitLab welcome message. GitLab key was configured without an expiration date; if the device is lost or compromised, revoke it from GitLab. Added `gitlab` remote; existing `origin` continues to point to GitHub.
20. **First GitLab push and synchronization (11 Oct 2026):** `git push gitlab main` and `git push gitlab v0.1.0` succeeded. Full `main` branch ID `73db8f944f029fd77db556cf7eab906bb21bb2c9` and annotated tag ref `39b080abcaff1e98c128e223fd97f989e99da427` were identical on both hosts. This is verified both by terminal logs and live GitLab branch/tag lookup.
21. **GitLab CI passing:** GitLab pipeline `2935094589` succeeded on `main` at `73db8f9...` with distinct `quality` and `tests` jobs both successful. After the documentation commit `aaaef73`, **pipeline `2935106858` also passed with both jobs successful**, confirmed live on 12 October.
22. **Handover continuity (11 Oct):** The updated `docs/PROJECT_HANDOVER.md` was committed as **`aaaef73`**, message `docs: update handover with GitLab publication and CI`; the fresh Ubuntu clone and GitLab API establish publication.
23. **Ubuntu reproducibility (11 Oct):** Cloned via GitLab HTTPS to `/home/heliosquant/myprojects/poc/engineering-context-mcp` on `hq-dev`; Git 2.53.0, Python 3.14.4, isolated `venv`, pip 26.2.1, MCP SDK 1.30.0, pytest 9.1.1, Ruff 0.17.0. Installation using `requirements-dev.txt` succeeded, `pip check` clean, **14/14 tests passed in 2.62 seconds**, Ruff lint and formatting passed, and the demo client successfully initialized MCP, created/listed a task, discovered 4 tools / 2 resources / 1 prompt, and read a resource.
24. **Ubuntu SSH diagnosis (11–12 Oct):** Created a separate Ubuntu ED25519 GitLab key, configured `Host gitlab.com` in `~/.ssh/config`, and registered its public key. The verbose trace showed successful connection, host-key match, key offered, and **`Server accepts key`**. The key unlock/signing step failed: `ssh-keygen -y -f ~/.ssh/id_ed25519_gitlab_hqdev > /dev/null` returned `incorrect passphrase supplied to decrypt private key` on repeated attempts. This was an **initial failed attempt**, resolved later with a replacement `v2` key. Preserve other keys (`id_ed25519`, `id_ed25519_hqiot`) and never repeat unsuccessful passphrase guesses.
25. **Ubuntu GitLab SSH recovery (12 Oct):** Generated the distinct `~/.ssh/id_ed25519_gitlab_hqdev_v2` key pair after the original key's unknown-passphrase issue. Registered the replacement public key; `ssh -vvv -o IdentityAgent=none -i ..._v2 -T git@gitlab.com` completed public-key authentication (exit 0) and welcomed `@othmane.fathallah.mail`. Updated the GitLab `Host` configuration to select `v2`, ran `ssh-add ..._v2`, and confirmed normal `ssh -T git@gitlab.com` succeeded. Existing old key remained visible in the agent as of the supplied `ssh-add -l`; revocation/removal was suggested but not confirmed.
26. **Ubuntu GitLab Git remote now SSH:** Switched `origin` with `git remote set-url origin git@gitlab.com:shared-wks/engineering-context-mcp.git`. Verified `git remote -v`, `git ls-remote origin HEAD` => `aaaef73ba81c41275a28bacdacad76bdafbaaedc`, and clean `main` up to date with `origin/main`. **Git pushes from Ubuntu were not yet attempted.**
27. **Ubuntu GitHub SSH resolution (12 Oct):** Existing key `~/.ssh/id_ed25519_github_hqdev` (fingerprint `SHA256:l2zO5uH3mKCJ0PjgE28z719hGtubkuAGLccdabEln7U`) was offered and accepted by GitHub, but GNOME/GCR SSH agent stalled at signing. Direct key authentication using `-o IdentityAgent=none -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519_github_hqdev` prompted for a passphrase and succeeded. After `nano ~/.ssh/config`, normal `ssh -T git@github.com` succeeded and identified `othmane-fathallah`. GitHub repository read via `git ls-remote` and a secondary remote on Ubuntu **remain to be verified**.
28. **Next engineering milestone:** Publish this refreshed documentation, complete optional Git hygiene (GitHub remote, obsolete key revocation, author config), then prepare Docker/Compose/PostgreSQL persistence using SQLAlchemy/Alembic. Jira/Confluence and HTTP transport remain later releases.

### Git history seen during setup

| Reference | Description | Evidence |
|---|---|---|
| `4240449` | `feat: initialize engineering context MCP` | GitHub initial public commit screenshot. |
| `v0.1.0` | Annotated first-release tag created during publication workflow | Repository showed one tag; verify target with `git show v0.1.0`. |
| `bdb3452` | `docs: update project roadmap for containerized architecture` | Earlier GitHub screenshot on `main`. |
| `aaaef73` | `docs: update handover with GitLab publication and CI` | Latest verified GitLab `main` commit in Ubuntu clone and API on 12 October. |
| `GitLab CI #2935106858` | `quality` and `tests` both succeeded | Live GitLab pipeline/jobs lookup against `aaaef73`. |
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
│   └── PROJECT_HANDOVER.md        # version in aaaef73 published; replace with 12 Oct update
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

**Verified present on GitLab `main`:** `.gitlab-ci.yml`, `requirements.txt`, `requirements-dev.txt`, `docs/PROJECT_HANDOVER.md`; most recently commit `aaaef73` is published. **This 12 October version is not yet published.** Not implemented: `Dockerfile`, `compose.yaml`, database migrations, Jira/Confluence integrations, and real `.env` files.

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

### Portable installation and second-desktop onboarding (published and **passed on Ubuntu**)

The root requirements files are **present in GitLab `main`**. The original Mac previously verified parity for commit `73db8f9`; the subsequent Ubuntu clone confirmed GitLab commit `aaaef73` (latest GitHub parity still to be rechecked):

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

The expanded `README.md` on GitLab `main` documents HTTPS/SSH cloning, `venv` creation and activation for macOS/Linux/Windows, pip installation, `python -m engineering_context_mcp.client`, direct MCP server launch, MCP Inspector, pytest, Ruff and the in-memory limitation. It describes v0.2 Docker/PostgreSQL as planned, not done. **A complete independent fresh clone/install/test/client run was successfully demonstrated on Ubuntu on 11 October 2026.**

**Successfully executed first-time desktop test (Ubuntu/Linux `hq-dev`):**

```bash
mkdir -p ~/myprojects/poc
cd ~/myprojects/poc
git clone https://gitlab.com/shared-wks/engineering-context-mcp.git
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

**Observed Ubuntu results:** clone to `/home/heliosquant/myprojects/poc/engineering-context-mcp`; `main` clean, `origin=https://gitlab.com/shared-wks/engineering-context-mcp.git`; Python `3.14.4` at `/usr/bin/python3`; Git `2.53.0`; pip upgraded to `26.2.1`; editable project `0.1.0` and MCP `1.30.0` installed with `requirements-dev.txt` (no Mac constraints); `pip check` reported **No broken requirements found**; **14 tests passed in 2.62s**; `ruff check` **All checks passed**; `ruff format --check` **11 files already formatted**; and `python -m engineering_context_mcp.client` connected, discovered tools/resources/prompts, invoked task tools and read `tasks://all`. The sample task `Learn MCP fundamentals` was added and listed successfully. This is a **completed, verified Linux portability milestone**.

**Git write-access caveat (updated 12 Oct):** Ubuntu originally cloned over public HTTPS, but its `origin` was subsequently changed to **GitLab SSH** and `git ls-remote origin HEAD` succeeded; both GitLab and GitHub `ssh -T` authenticated successfully. **No Ubuntu `git push` has been observed**, the `github` secondary remote is not yet configured, and GitHub repository-level read access has not been tested. Project-local Git author identity (`Othmane Fathallah` and professional email) was recommended but **not verified applied**, while Ubuntu global Git identity was observed as `Helios Quant` / `heliosquant@gmail.com`. Do not move a private key from the Mac to Ubuntu. Root requirements files delegate dependency metadata to `pyproject.toml` and are **not immutable locks**.

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

### Current result — both repositories published (historical SHA parity verified)

| Property | GitHub (`origin`) | GitLab (`gitlab`) |
|---|---|---|
| Public repository | https://github.com/shared-wks/engineering-context-mcp | https://gitlab.com/shared-wks/engineering-context-mcp |
| Group / organization | `shared-wks` | `shared-wks` |
| SSH URL | `git@github.com:shared-wks/engineering-context-mcp.git` | `git@gitlab.com:shared-wks/engineering-context-mcp.git` |
| `main` commit at *11 Oct initial comparison* | `73db8f944f029fd77db556cf7eab906bb21bb2c9` | **Same SHA** |
| Later handover commit (12 Oct check) | **Not freshly checked** | `aaaef73ba81c41275a28bacdacad76bdafbaaedc` |
| Annotated `v0.1.0` ref | `39b080abcaff1e98c128e223fd97f989e99da427` | **Same SHA** |
| CI | Two earlier successful GitHub runs seen; latest not verified | Pipelines **2935094589 and 2935106858 successful** (`quality`, `tests`) |

**GitLab facts verified live:** public project ID `87479265`; default branch `main`; latest SHA **`aaaef73ba81c41275a28bacdacad76bdafbaaedc`**. Annotated `v0.1.0` tag object SHA `39b080a...` points to the first release commit `424044936356ff111488a3a5fb4892ea148978a7`. The original [pipeline 2935094589](https://gitlab.com/shared-wks/engineering-context-mcp/-/pipelines/2935094589) and the newer [pipeline 2935106858](https://gitlab.com/shared-wks/engineering-context-mcp/-/pipelines/2935106858) both succeeded, with `quality` and `tests` jobs successful. **Current GitHub HEAD parity and latest GitHub CI have not been reverified.**

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

### Ubuntu `hq-dev` Git/SSH status — **both SSH logins working**

- **Host:** `hq-dev`, Ubuntu, `/home/heliosquant/myprojects/poc/engineering-context-mcp`. The project was originally cloned via GitLab HTTPS and was later switched to **SSH**.
- **GitLab remote / Git read verified:** `origin  git@gitlab.com:shared-wks/engineering-context-mcp.git` (fetch/push URLs). `git ls-remote origin HEAD` returned `aaaef73ba81c41275a28bacdacad76bdafbaaedc`. `git status`: clean `main`, up to date with `origin/main`. **No Ubuntu push has yet been performed.**
- **GitLab key recovery:** The first `~/.ssh/id_ed25519_gitlab_hqdev` had an unrecovered passphrase (historical failed attempts). Created **`~/.ssh/id_ed25519_gitlab_hqdev_v2`** and registered its `.pub` in GitLab (fingerprint `SHA256:5v+KsS82WFrFfNJjbHQkCleg9aNbEFEGOTEJNyHjPgY`). The explicit-agent-bypass diagnostic showed `Authenticated ... using "publickey"`, `Welcome to GitLab, @othmane.fathallah.mail!`, exit 0. After setting the GitLab `Host` entry to `v2` and adding it using `ssh-add`, **normal `ssh -T git@gitlab.com` succeeded**.
- **Old GitLab key cleanup pending:** The old key fingerprint is `SHA256:cj0ik78DVUcUOgP6loWmHoPdM8B8l6tjODcqtPXTFCE`; the supplied `ssh-add -l` still listed both old and new keys. Only revoke/remove the **old** key after positively matching its fingerprint. Keep the working `v2` key; preserve `id_ed25519_hqiot` and other unrelated keys. A successful `ssh -T` is not evidence of a successful Git push.
- **GitHub key/signing fixed:** Dedicated `~/.ssh/id_ed25519_github_hqdev` fingerprint `SHA256:l2zO5uH3mKCJ0PjgE28z719hGtubkuAGLccdabEln7U`. Verbose logs showed TCP/SSH connection and `Server accepts key` but the GNOME/GCR agent stalled during signing. Bypassing the agent with `IdentityAgent=none` prompted for the correct private-key passphrase and returned `Hi othmane-fathallah! You've successfully authenticated, but GitHub does not provide shell access.` After editing `~/.ssh/config`, the same **normal** `ssh -T git@github.com` succeeded. Exact `~/.ssh/config` text was not shown, so do not overstate its contents.
- **GitHub Git remote pending:** No additional `github` remote or GitHub `git ls-remote` confirmation has been shown on Ubuntu. Recommended after confirming access:

  ```bash
  git ls-remote git@github.com:shared-wks/engineering-context-mcp.git HEAD
  git remote add github git@github.com:shared-wks/engineering-context-mcp.git
  git remote -v
  ```

  Run `git remote add` only if `github` does not already exist; keep `origin` tracking GitLab. **Never force-push** to either host, and verify synchronization before/after intentional pushes.
- **Git author not verified on Ubuntu:** Global author observed `Helios Quant` / `heliosquant@gmail.com`. A local override using the preferred professional identity was suggested but execution was not shown; check `git config --local user.name` and `git config --local user.email` before committing.

### Publishing commands for future development (Mac checkout)

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

`origin` is the default upstream for local `main`. The `gitlab` remote is for deliberate mirrored pushes **in the Mac checkout**. On Ubuntu, `origin` is GitLab SSH and the `github` secondary remote has not yet been added. **No automatic synchronization or forced rewrites.** Always verify full SHA parity after significant pushes:

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

Live GitLab status: pipeline **2935094589 SUCCESS** on `73db8f9...` and **newest pipeline 2935106858 SUCCESS** on **`aaaef73...`**, both with `quality` and `tests` jobs SUCCESS. Separately, Ubuntu local pytest confirmed **14 tests passed**. A successful pipeline does not by itself prove the number of test cases run unless job logs are inspected.

Next improvement is ensuring both providers run the same test/check set, updating GitHub Actions deliberately and re-validating hosted CI. The portable README **has been validated through a successful clean Ubuntu installation and client smoke test**. Both Ubuntu SSH logins are now working; actual Ubuntu push remains untested.

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
| Ubuntu GitLab SSH: `Permission denied (publickey)` then repeated passphrase prompts | The first registered key was accepted, but its encrypted private key could not be unlocked | **Resolved:** created new `id_ed25519_gitlab_hqdev_v2`, registered public half, verified direct and normal GitLab SSH login; switched GitLab remote to SSH and verified `ls-remote`. **Old key retirement still pending.** |
| Confusing two machines' Git remote names | On the Mac `origin`=GitHub, `gitlab`=GitLab; on Ubuntu `origin`=GitLab **SSH** (originally HTTPS) | Run `git remote -v` in **each checkout** before any push or remote change. |
| Ubuntu GitHub SSH appeared to hang after `Server accepts key` | SSH reached GitHub, but GNOME/GCR agent stalled during the private-key signing operation | **Resolved:** verified direct authentication with `-o IdentityAgent=none`; after editing config, normal `ssh -T git@github.com` succeeded. A GitHub remote and `git ls-remote` have not yet been verified. |

## 11. Exact recommended next actions

### First: publish this **12 October** documentation update from the original Mac

The previous `docs/PROJECT_HANDOVER.md` **was published** as commit `aaaef73`; this 12 October version is newer and local to the generated deliverables. You may publish from the **Mac checkout where both SSH remotes are already configured**. Ubuntu GitLab SSH now also authenticates and its `origin` is SSH, but a push from Ubuntu has **not** yet been tested and the GitHub mirror remote is not added there. Copy both Markdown files from Downloads, then inspect before committing:

```bash
cd ~/myprojects/poc/engineering-context-mcp
cp ~/Downloads/PROJECT_HANDOVER.md docs/PROJECT_HANDOVER.md
cp ~/Downloads/PROJECT_CONTINUITY.md docs/PROJECT_CONTINUITY.md

git status
git diff -- docs/PROJECT_HANDOVER.md
# Carefully check for secrets, credential data, or local-only information.
git add docs/PROJECT_HANDOVER.md docs/PROJECT_CONTINUITY.md
git diff --cached --check
git commit -m "docs: record Ubuntu reproducibility and dual SSH access"
git push origin main
git push gitlab main

# Verify new branch refs match.
git rev-parse main
git ls-remote origin refs/heads/main
git ls-remote gitlab refs/heads/main
```

Do not re-tag `v0.1.0`. If either push fails, inspect the remote state before retrying; do not force-push. **These push commands have not been executed as part of this 12 October handover update.**

### Then: confirm CI and decide whether Ubuntu Git write access is needed

- [x] Public GitHub organization/repository and first release tag.
- [x] Public GitLab group and project.
- [x] **Mac** GitLab SSH key and working authentication. **Ubuntu GitLab SSH also works with the replacement `v2` key**; its `origin` is GitLab SSH and repository reads were verified.
- [x] Two Git remotes with synchronized `main` and `v0.1.0` SHAs (at snapshot).
- [x] Root `requirements.txt`, `requirements-dev.txt`, and developer-friendly README published.
- [x] `.gitlab-ci.yml` published and GitLab pipeline **2935094589** successful (`quality`, `tests`).
- [x] Earlier GitHub `Python CI` runs #1 and #2 successful.
- [x] Published previous handover revision as **`aaaef73`** on GitLab; newest GitLab **pipeline 2935106858** passed both jobs.
- [x] Fresh Ubuntu HTTPS clone, Python 3.14.4 `venv` installation, pip check, **14 tests**, Ruff and MCP demo all passed.
- [ ] Publish **this 12 October handover** and optional companion continuity file from working Mac SSH checkout; then check latest GitHub/GitLab SHAs.
- [x] Ubuntu GitLab `v2` key registered and direct + normal SSH logins verified. GitLab `origin` switched from HTTPS to SSH; `git ls-remote origin HEAD` succeeded.
- [x] Ubuntu GitHub SSH authenticated as `othmane-fathallah` using agent bypass, then through normal `ssh -T` after updating the configuration.
- [ ] Revoke the old Ubuntu GitLab public key and remove its stale SSH-agent identity, after checking the fingerprint (not yet confirmed).
- [ ] Verify Ubuntu GitHub repository read access, add a `github` secondary remote if needed, check local Git author settings and test an intentional Git push when ready; none of those steps has been confirmed yet.
- [ ] Check GitHub Actions **most recent** workflow status and inspect failures or warnings if any.
- [x] Fresh clone and run on **Ubuntu second desktop** with Python 3.14.4: 14 automated tests, Ruff and an MCP client smoke test all verified.
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

> Continue **Engineering Context MCP**. Read `docs/PROJECT_HANDOVER.md` and `docs/PROJECT_CONTINUITY.md` first. Use standard Python **`venv` and `pip`**, not `uv`. Public repos: `https://github.com/shared-wks/engineering-context-mcp` and `https://gitlab.com/shared-wks/engineering-context-mcp`. **Mac:** `origin`=GitHub SSH; `gitlab`=GitLab SSH. **Ubuntu `hq-dev`:** `origin`=GitLab **SSH** (initially cloned via HTTPS). GitHub/GitLab branch SHA parity was verified at `73db8f944f029fd77db556cf7eab906bb21bb2c9`, annotated `v0.1.0` tag object parity at `39b080abcaff1e98c128e223fd97f989e99da427`. GitLab later reached `aaaef73ba81c41275a28bacdacad76bdafbaaedc` (`docs: update handover with GitLab publication and CI`); GitLab CI pipeline **2935106858** passed both jobs. Newer GitHub SHA parity and latest GitHub CI remain to be checked. **Ubuntu fresh install is VERIFIED**: Python 3.14.4, requirements-dev.txt installed into project venv, pip check clean, **14/14 tests**, Ruff and stdio MCP client demo working (4 tools, 2 resources, 1 prompt). **Ubuntu SSH now works for BOTH providers:** GitLab old key could not be decrypted; new key `id_ed25519_gitlab_hqdev_v2` was registered and verified; GitLab `origin` SSH `ls-remote HEAD` matches `aaaef73`. GitHub key `id_ed25519_github_hqdev` authenticated after bypassing a stalling SSH agent, then normal `ssh -T` worked. Obsolete GitLab key revocation, Ubuntu GitHub remote / Git repo read, local Git author settings and any Ubuntu Git push remain **unverified**. Mac already has working mirrored remotes. App is still **in-memory FastMCP stdio**; Docker, PostgreSQL, SQLAlchemy/Alembic, Streamable HTTP, Jira and Confluence are **planned, not implemented**. Next: publish refreshed 12 Oct docs; finish optional Ubuntu Git hygiene; begin v0.2 Docker/Compose/PostgreSQL persistence. Keep `v0.1.0` tag unchanged. Do not disclose private keys, passphrases, tokens, `.env` secrets or recovery codes.

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
| 2026-10-11 (published) | Prior handover successfully committed to GitLab `main` as `aaaef73` | Fresh Ubuntu clone and live GitLab SHA lookup; commit message `docs: update handover with GitLab publication and CI` |
| 2026-10-11 (GitLab) | Pipeline **2935106858** passed on `aaaef73` | Live GitLab pipeline and two job lookups (`quality`, `tests` both success) |
| 2026-10-11 (Ubuntu) | **Fresh second-machine clone/install/test/MCP run succeeded** | User terminal output: Python 3.14.4, 14/14 pytest in 2.62s, Ruff, `pip check`, MCP tools/resources/prompt and task execution |
| 2026-10-11–12 (Ubuntu SSH) | First GitLab key accepted publicly, but decrypting its private key failed | SSH verbose trace and `ssh-keygen -y` error; historical issue resolved with `v2` key |
| 2026-10-12 (Ubuntu GitLab) | **Replacement `v2` key and normal `ssh -T` succeeded; GitLab `origin` switched to SSH** | `Authenticated ... using "publickey"`; GitLab welcome; `ssh-add`; `git remote -v`; `git ls-remote origin HEAD` matched `aaaef73`; clean `main` |
| 2026-10-12 (Ubuntu GitHub) | **Direct and normal `ssh -T git@github.com` succeeded as `othmane-fathallah`** | GitHub recognized existing key; bypassed stalled GCR agent (`IdentityAgent=none`) and entered passphrase; after config edit normal login succeeded |
| 2026-10-12 (this document) | Refreshed full handover and companion short continuity document with **both successful Ubuntu SSH logins** | Downloadable replacements prepared; **not yet committed or pushed** |

**Rule for future documentation:** mark items **verified**, **reported by user**, or **planned/unverified**. Never silently convert plans into accomplishments. Update this handover whenever a release or infrastructure milestone is completed.
