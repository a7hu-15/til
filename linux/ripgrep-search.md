# Searching for Text in Files with ripgrep

`rg` (ripgrep) is a line-oriented search tool that recursively searches the current directory for a regex pattern. It is much faster than `grep` and respects `.gitignore` by default.

```bash
# Search for a word in the current directory
rg "TODO"

# Search only in files of a specific type (e.g. Python files)
rg "import os" -t py

# Search case-insensitively
rg -i "error"
```