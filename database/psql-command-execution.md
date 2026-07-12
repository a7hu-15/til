# Executing SQL Statements Directly via psql

Instead of opening an interactive `psql` shell, you can execute a SQL command directly from the command line using the `-c` flag.

```bash
psql -U postgres -d my_database -c "SELECT * FROM users LIMIT 5;"
```
This is extremely useful for shell scripting and automation tasks.