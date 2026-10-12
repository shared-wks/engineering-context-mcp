# Engineering Context MCP — Active Continuity Snapshot

**As of:** 12 October 2026  
**Release:** `v0.1.0` — working MCP foundation; in-memory stdio demonstration  
**Full project history:** [`PROJECT_HANDOVER.md`](PROJECT_HANDOVER.md)

## Where the project is

- Public GitHub: <https://github.com/shared-wks/engineering-context-mcp>
- Public GitLab: <https://gitlab.com/shared-wks/engineering-context-mcp>
- Original macOS checkout: `~/myprojects/poc/engineering-context-mcp`
- Ubuntu desktop (`hq-dev`) checkout: `/home/heliosquant/myprojects/poc/engineering-context-mcp`
- Default branch: `main`; annotated historical first-release tag: `v0.1.0`.
- Latest verified **GitLab** `main` SHA: `aaaef73ba81c41275a28bacdacad76bdafbaaedc` — commit `docs: update handover with GitLab publication and CI`.
- Earlier **fully verified dual-host** `main` SHA: `73db8f944f029fd77db556cf7eab906bb21bb2c9`. Newer GitHub SHA parity needs a fresh check.
- Annotated `v0.1.0` **tag object SHA** on both hosts: `39b080abcaff1e98c128e223fd97f989e99da427`; points to the initial release commit `424044936356ff111488a3a5fb4892ea148978a7`. Do not move this tag.

## Completed and verified

1. Python `src/` package with official MCP SDK/FastMCP stdio server and native client; **4 tools, 2 resources, 1 prompt**. Tasks are in memory only.
2. **8 unit tests + 6 protocol integration tests**, pytest and Ruff; Python project managed by **`venv` and `pip` only** (no `uv`).
3. Public GitHub and GitLab repositories under `shared-wks`; working GitHub/GitLab **SSH from the original Mac**. Mac: `origin` points to GitHub; `gitlab` points to GitLab.
4. Portable onboarding (`README.md`, `requirements.txt`, `requirements-dev.txt`), GitHub Actions, GitLab `.gitlab-ci.yml`, and previous handover published.
5. **GitLab CI pipeline 2935106858 SUCCESS** on `aaaef73` (confirmed 12 October), with both `quality` and `tests` jobs successful. Earlier pipeline `2935094589` also passed. Earlier two GitHub CI runs were green; current GitHub run not freshly verified.
6. **Ubuntu fresh-clone reproduction passed:** clone via **GitLab HTTPS** on `hq-dev`; Ubuntu Python **3.14.4**, Git **2.53.0**; local `venv`, editable dev requirements installed with pip **without using Mac constraint file**; `pip check` clean; **14/14 pytest tests passed in 2.62s**; Ruff lint successful, 11 files formatted; MCP Python client connected, created/listed task, discovered tools/resources/prompt, and read resource.
7. Ubuntu working tree was clean at `aaaef73`; after the initial HTTPS clone, its `origin` was switched to **GitLab SSH**. `git ls-remote origin HEAD` returned the same `aaaef73` commit. No Ubuntu Git push has yet been verified.

## Ubuntu SSH setup — both providers now authenticated

- **GitLab:** First `~/.ssh/id_ed25519_gitlab_hqdev` ED25519 key was registered, but local `ssh-keygen -y` failed repeatedly to unlock it; this is a **historical resolved issue**, not the current status. Its old fingerprint was `SHA256:cj0ik78DVUcUOgP6loWmHoPdM8B8l6tjODcqtPXTFCE`.
- **GitLab replacement:** Created/registered `~/.ssh/id_ed25519_gitlab_hqdev_v2` (fingerprint `SHA256:5v+KsS82WFrFfNJjbHQkCleg9aNbEFEGOTEJNyHjPgY`). Explicit-key verbose login completed `Authenticated to gitlab.com using "publickey"`, returned `Welcome to GitLab, @othmane.fathallah.mail!`, exit 0. Updated SSH configuration, loaded replacement with `ssh-add`, and confirmed normal `ssh -T git@gitlab.com` worked.
- **GitLab Git remote:** `origin` changed from HTTPS to `git@gitlab.com:shared-wks/engineering-context-mcp.git`. Verified `git ls-remote origin HEAD` equals `aaaef73ba81c41275a28bacdacad76bdafbaaedc` and clean/up-to-date `main`. **No Ubuntu push was attempted or verified.**
- **GitHub:** Dedicated `~/.ssh/id_ed25519_github_hqdev` (fingerprint `SHA256:l2zO5uH3mKCJ0PjgE28z719hGtubkuAGLccdabEln7U`) was accepted by GitHub, but the GNOME/GCR SSH agent stalled at signing. Direct `ssh -o IdentityAgent=none ... -T git@github.com` succeeded after prompting for the key's passphrase. After editing `~/.ssh/config`, normal `ssh -T git@github.com` also succeeded: `Hi othmane-fathallah! You've successfully authenticated...`.
- **Pending Git housekeeping:** Old GitLab key was still visible in `ssh-add -l` alongside the new one; retirement/revocation has **not** been confirmed. Ubuntu `github` secondary remote and GitHub repository read (`git ls-remote`) are **not yet verified**. Ubuntu global Git identity was previously `Helios Quant` / `heliosquant@gmail.com`; suggested project-local professional author settings have **not** been verified applied. Preserve Raspberry Pi `id_ed25519_hqiot` and unrelated keys; never share private keys or passphrases.

## Next actions, in order

1. **Publish this refreshed full handover and continuity snapshot** from the Mac (working GitHub `origin` and GitLab `gitlab` remotes). Neither of these new 12 October updates has been committed or pushed yet. Verify latest SHA parity afterward. Ubuntu could alternatively publish once remotes and push permissions are deliberately confirmed.
2. **Finish optional Ubuntu Git hygiene:** Check `git ls-remote git@github.com:shared-wks/engineering-context-mcp.git HEAD`; add `github` remote if absent; inspect `git config --local user.name` / `user.email`; revoke obsolete GitLab key by **old fingerprint only**, and optionally remove its agent identity. Do not disrupt the working `v2` GitLab/GitHub SSH logins.
3. Check latest GitHub Actions workflow status and optionally align CI (`pip check`, Ruff format check, Python 3.14). GitLab pipeline 2935106858 is already confirmed successful.
4. Begin **v0.2.0**: Dockerfile, Docker Compose, PostgreSQL, SQLAlchemy models/repositories, Alembic migrations, persistent task store, database integration tests and CI updates. SQLite is not the primary choice; preserve stdio MCP compatibility.
5. Later: Streamable HTTP, Jira/Confluence read-only adapters with proper authorization, security and observability.

## Quick local validation (either computer)

```bash
cd ~/myprojects/poc/engineering-context-mcp
source venv/bin/activate
python -m pip check
python -m pytest -v
python -m ruff check .
python -m ruff format --check .
python -m engineering_context_mcp.client
```

## Publishing from the original Mac (recommended; verified SSH remotes)

```bash
cd ~/myprojects/poc/engineering-context-mcp
cp ~/Downloads/PROJECT_HANDOVER.md docs/PROJECT_HANDOVER.md
cp ~/Downloads/PROJECT_CONTINUITY.md docs/PROJECT_CONTINUITY.md
git status
git add docs/PROJECT_HANDOVER.md docs/PROJECT_CONTINUITY.md
git diff --cached --check
git commit -m "docs: record Ubuntu reproducibility and dual SSH access"
git push origin main
git push gitlab main
git rev-parse main
git ls-remote origin refs/heads/main
git ls-remote gitlab refs/heads/main
```

**Scope boundary:** Do not claim Docker services, PostgreSQL, SQLAlchemy/Alembic, HTTP deployment, Jira or Confluence integrations are built yet. Do not share credentials, private keys, passphrases, `.env` contents or recovery codes. Mark facts as verified vs. proposed. Use the full handover for historical detail.
