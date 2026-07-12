import os
import subprocess
import re

tils = [
    {
        "category": "Python",
        "cat_slug": "python",
        "file": "python-merge-dictionary-operators.md",
        "title": "Merged Dictionary Operators in Python 3.9",
        "content": "# Merged Dictionary Operators in Python 3.9\n\nPython 3.9 introduced the union operators to `dict`. You can use `|` to merge two dictionaries and `|=` to update a dictionary in place.\n\n```python\ndict1 = {'a': 1, 'b': 2}\ndict2 = {'b': 3, 'c': 4}\n\n# Merge dictionaries\nmerged = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}\n\n# Update in place\ndict1 |= dict2  # dict1 is now {'a': 1, 'b': 3, 'c': 4}\n```\nThis is cleaner than using `{**dict1, **dict2}` or `dict1.update(dict2)`."
    },
    {
        "category": "Git",
        "cat_slug": "git",
        "file": "git-log-graph.md",
        "title": "Viewing Commit History as a Graph",
        "content": "# Viewing Commit History as a Graph\n\nTo visualize branch structures, merges, and commit history directly in the terminal, use the `--graph` flag with `git log`.\n\n```bash\ngit log --oneline --graph --all\n```\nYou can create a custom alias for this to make it easier to run:\n```bash\ngit config --global alias.adog \"log --all --decorate --oneline --graph\"\n```\nNow running `git adog` gives a beautiful text representation of your commit graph."
    },
    {
        "category": "Linux",
        "cat_slug": "linux",
        "file": "ripgrep-search.md",
        "title": "Searching for Text in Files with ripgrep",
        "content": "# Searching for Text in Files with ripgrep\n\n`rg` (ripgrep) is a line-oriented search tool that recursively searches the current directory for a regex pattern. It is much faster than `grep` and respects `.gitignore` by default.\n\n```bash\n# Search for a word in the current directory\nrg \"TODO\"\n\n# Search only in files of a specific type (e.g. Python files)\nrg \"import os\" -t py\n\n# Search case-insensitively\nrg -i \"error\"\n```"
    },
    {
        "category": "Web Development",
        "cat_slug": "web-development",
        "file": "css-variable-fallbacks.md",
        "title": "CSS Variable Fallbacks",
        "content": "# CSS Variable Fallbacks\n\nYou can provide a fallback value for custom CSS properties (variables) in case they are not defined.\n\n```css\n.card {\n  /* If --card-bg is not defined, it will fallback to white */\n  background-color: var(--card-bg, #ffffff);\n}\n```\nYou can also nest variables:\n```css\n.text {\n  color: var(--primary-color, var(--fallback-color, black));\n}\n```"
    },
    {
        "category": "Database",
        "cat_slug": "database",
        "file": "psql-command-execution.md",
        "title": "Executing SQL Statements Directly via psql",
        "content": "# Executing SQL Statements Directly via psql\n\nInstead of opening an interactive `psql` shell, you can execute a SQL command directly from the command line using the `-c` flag.\n\n```bash\npsql -U postgres -d my_database -c \"SELECT * FROM users LIMIT 5;\"\n```\nThis is extremely useful for shell scripting and automation tasks."
    },
    {
        "category": "DevOps",
        "cat_slug": "devops",
        "file": "docker-stats.md",
        "title": "Checking Resource Usage of Docker Containers",
        "content": "# Checking Resource Usage of Docker Containers\n\nTo view a live stream of container resource usage statistics (CPU, memory, network I/O, etc.), use:\n\n```bash\ndocker stats\n```\nTo get stats for a specific running container:\n```bash\ndocker stats container_name\n```\nTo format the output to show only specific fields:\n```bash\ndocker stats --format \"table {{.Name}}\\t{{.CPUPerc}}\\t{{.MemUsage}}\"\n```"
    }
]

def update_readme(entry):
    with open("README.md", "r") as f:
        content = f.read()
    
    category_header = f"## {entry['category']}\n\n"
    if category_header not in content:
        # Fallback just in case
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
