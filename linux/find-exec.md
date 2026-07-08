# Executing Commands on Found Files

You can use `-exec` with `find` to run commands on each matched file.

```bash
find . -name "*.log" -exec rm {} \;
```
This deletes all `.log` files in the current directory and subdirectories.