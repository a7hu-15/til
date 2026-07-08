import os
import subprocess
import re

tils = [
    {
        "category": "Git",
        "cat_slug": "git",
        "file": "git-rebase-interactive.md",
        "title": "Interactive Git Rebase",
        "content": "# Interactive Git Rebase\n\n`git rebase -i` allows you to edit, squash, reorder, or drop commits. It's a powerful tool for cleaning up your commit history before merging.\n\n```bash\ngit rebase -i HEAD~3\n```"
    },
    {
        "category": "Linux",
        "cat_slug": "linux",
        "file": "find-exec.md",
        "title": "Executing Commands on Found Files",
        "content": "# Executing Commands on Found Files\n\nYou can use `-exec` with `find` to run commands on each matched file.\n\n```bash\nfind . -name \"*.log\" -exec rm {} \\;\n```\nThis deletes all `.log` files in the current directory and subdirectories."
    },
    {
        "category": "DevOps",
        "cat_slug": "devops",
        "file": "docker-logs-follow.md",
        "title": "Following Docker Logs",
        "content": "# Following Docker Logs\n\nTo view continuous output from a running container, use the `-f` flag with `docker logs`.\n\n```bash\ndocker logs -f container_name\n```\nIt acts just like `tail -f`."
    },
    {
        "category": "Python",
        "cat_slug": "python",
        "file": "python-zip-strict.md",
        "title": "Strict Zip in Python",
        "content": "# Strict Zip in Python\n\nIn Python 3.10+, you can use `strict=True` with `zip()` to ensure all iterables are the same length. It raises a `ValueError` if they are not.\n\n```python\nlist1 = [1, 2]\nlist2 = ['a', 'b', 'c']\n# This will raise a ValueError\nfor x, y in zip(list1, list2, strict=True):\n    print(x, y)\n```"
    },
    {
        "category": "Git",
        "cat_slug": "git",
        "file": "git-log-oneline.md",
        "title": "Compact Git Log",
        "content": "# Compact Git Log\n\n`git log --oneline` shows a compact version of your commit history, displaying each commit on a single line with an abbreviated hash.\n\n```bash\ngit log --oneline --graph\n```"
    },
    {
        "category": "Open Source",
        "cat_slug": "open-source",
        "file": "markdown-tables.md",
        "title": "Creating Markdown Tables",
        "content": "# Creating Markdown Tables\n\nMarkdown tables are easy to create using pipes `|` and hyphens `-`.\n\n```markdown\n| Header 1 | Header 2 |\n|----------|----------|\n| Cell 1   | Cell 2   |\n```"
    }
]

def update_readme(entry):
    with open("README.md", "r") as f:
        content = f.read()
    
    category_header = f"## {entry['category']}\n\n"
    if category_header not in content:
        # Ensure category exists
        parts = content.split("\n---\n")
        content = parts[0] + f"## {entry['category']}\n\n- _Coming soon_\n\n" + "\n---\n".join(parts[1:])
        
        table_row = f"| {entry['category']} | 0 |\n"
        if f"| {entry['category']} |" not in content:
            total_idx = content.find("| **Total**")
            content = content[:total_idx] + table_row + content[total_idx:]

    if "- _Coming soon_\n" in content.split(category_header)[1].split("##")[0]:
        link = f"- [{entry['title']}]({entry['cat_slug']}/{entry['file']})\n"
        content = content.replace(category_header + "- _Coming soon_\n", category_header + link)
    else:
        link = f"- [{entry['title']}]({entry['cat_slug']}/{entry['file']})\n"
        content = content.replace(category_header, category_header + link)
            
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
subprocess.run(["git", "push"], check=True)
