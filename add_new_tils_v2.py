import os
import subprocess
import re

tils = [
    {
        "category": "Git",
        "cat_slug": "git",
        "file": "git-fork-contributions.md",
        "title": "GitHub Contribution Rules for Forks",
        "content": "# GitHub Contribution Rules for Forks\n\nCommits pushed to a forked repository do not count towards your GitHub contribution graph unless they are merged into the parent repository, or you open a pull request.\n\nTo get contribution credits for changes in forks:\n- Open a Pull Request to the upstream repository.\n- Or work in a standalone (non-forked) repository."
    },
    {
        "category": "Python",
        "cat_slug": "python",
        "file": "fastapi-dependency-injection.md",
        "title": "FastAPI Dependency Injection with Session",
        "content": "# FastAPI Dependency Injection with Session\n\nFastAPI allows injecting database sessions as dependencies to ensure connections are automatically created and closed after each request.\n\n```python\ndef get_db():\n    db = SessionLocal()\n    try:\n        yield db\n    finally:\n        db.close()\n\n@app.get(\"/items\")\ndef read_items(db: Session = Depends(get_db)):\n    return db.query(Item).all()\n```"
    },
    {
        "category": "Web Development",
        "cat_slug": "web-development",
        "file": "tanstack-query-conditional.md",
        "title": "Conditional Fetching in TanStack Query",
        "content": "# Conditional Fetching in TanStack Query\n\nYou can use the `enabled` option to prevent a query from running automatically when its dependencies (like a search query string) are empty.\n\n```typescript\nconst { data, isLoading } = useQuery({\n  queryKey: [\"search\", q],\n  queryFn: () => searchService.globalSearch(q),\n  enabled: q.trim().length > 0, // only fetch if query is not empty\n});\n```"
    },
    {
        "category": "Database",
        "cat_slug": "database",
        "file": "postgres-macos-default-roles.md",
        "title": "PostgreSQL Default Roles on macOS Homebrew",
        "content": "# PostgreSQL Default Roles on macOS Homebrew\n\nWhen installing PostgreSQL via Homebrew on macOS, it initializes the database cluster under your local macOS username (e.g. `ashuchaudhary`) rather than the default `postgres` role.\n\nTo connect using `postgres`, you must manually create the superuser role:\n```bash\ncreateuser -s postgres\n```"
    },
    {
        "category": "Python",
        "cat_slug": "python",
        "file": "pydantic-v2-config-dict.md",
        "title": "Pydantic V2 ConfigDict Configuration",
        "content": "# Pydantic V2 ConfigDict Configuration\n\nIn Pydantic V2, the legacy `class Config` is replaced by the `model_config` attribute using `ConfigDict`.\n\n```python\nfrom pydantic import BaseModel, ConfigDict\n\nclass UserResponse(BaseModel):\n    model_config = ConfigDict(from_attributes=True) # equivalent to orm_mode = True\n    id: int\n    username: str\n```"
    },
    {
        "category": "DevOps",
        "cat_slug": "devops",
        "file": "alembic-migrations-upgrade.md",
        "title": "Running Alembic Migrations",
        "content": "# Running Alembic Migrations\n\nTo apply all pending database migrations in a SQLAlchemy project using Alembic:\n\n```bash\nalembic upgrade head\n```\nThis runs the upgrade scripts up to the latest revision."
    }
]

def update_readme(entry):
    with open("README.md", "r") as f:
        content = f.read()
    
    # Ensure category exists
    category_header = f"## {entry['category']}\n\n"
    if category_header not in content:
        # Add category header before '---'
        parts = content.split("\n---\n")
        content = parts[0] + f"## {entry['category']}\n\n- _Coming soon_\n\n" + "\n---\n".join(parts[1:])
        
        # Add to table if needed
        table_row = f"| {entry['category']} | 0 |\n"
        if f"| {entry['category']} |" not in content:
            total_idx = content.find("| **Total**")
            content = content[:total_idx] + table_row + content[total_idx:]

    # Add link to category
    if "- _Coming soon_\n" in content.split(category_header)[1].split("##")[0]:
        link = f"- [{entry['title']}]({entry['cat_slug']}/{entry['file']})\n"
        content = content.replace(category_header + "- _Coming soon_\n", category_header + link)
    else:
        link = f"- [{entry['title']}]({entry['cat_slug']}/{entry['file']})\n"
        content = content.replace(category_header, category_header + link)
            
    # Update stats
    stat_regex = rf"\| {entry['category']} \| (\d+) \|"
    def replace_stat(match):
        return f"| {entry['category']} | {int(match.group(1)) + 1} |"
    content = re.sub(stat_regex, replace_stat, content)
    
    total_regex = r"\| \*\*Total\*\* \| \*\*(\d+)\*\* \|"
    def replace_total(match):
        return f"| **Total** | **{int(match.group(1)) + 1}** |"
    content = re.sub(total_regex, replace_total, content)
    
    with open("README.md", "w") as f:
        f.write(content)

env = os.environ.copy()
env["GIT_AUTHOR_NAME"] = "Ashu Chaudhary"
env["GIT_AUTHOR_EMAIL"] = "xripprix85@gmail.com"
env["GIT_COMMITTER_NAME"] = "Ashu Chaudhary"
env["GIT_COMMITTER_EMAIL"] = "xripprix85@gmail.com"

for entry in tils:
    os.makedirs(entry['cat_slug'], exist_ok=True)
    with open(f"{entry['cat_slug']}/{entry['file']}", "w") as f:
        f.write(entry['content'])
        
    update_readme(entry)
    
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"docs({entry['cat_slug']}): add TIL on {entry['title'].lower()}"], check=True, env=env)
    
print("Running git push...")
subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
