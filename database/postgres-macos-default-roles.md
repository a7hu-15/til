# PostgreSQL Default Roles on macOS Homebrew

When installing PostgreSQL via Homebrew on macOS, it initializes the database cluster under your local macOS username (e.g. `ashuchaudhary`) rather than the default `postgres` role.

To connect using `postgres`, you must manually create the superuser role:
```bash
createuser -s postgres
```