# Running Alembic Migrations

To apply all pending database migrations in a SQLAlchemy project using Alembic:

```bash
alembic upgrade head
```
This runs the upgrade scripts up to the latest revision.