import os
import subprocess
import re

tils = [
    {
        "category": "Python",
        "cat_slug": "python",
        "file": "python-enumerate.md",
        "title": "Using Enumerate in Python",
        "content": "# Using Enumerate in Python\n\nWhen looping over an iterable, `enumerate()` allows you to keep track of the index automatically.\n\n```python\nnames = ['Alice', 'Bob', 'Charlie']\nfor i, name in enumerate(names):\n    print(f\"{i}: {name}\")\n```\nThis is much cleaner than using `range(len(names))`."
    },
    {
        "category": "Python",
        "cat_slug": "python",
        "file": "python-zip.md",
        "title": "Iterating Multiple Lists with Zip",
        "content": "# Iterating Multiple Lists with Zip\n\n`zip()` takes multiple iterables and aggregates them into tuples.\n\n```python\nnames = ['Alice', 'Bob']\nages = [25, 30]\nfor name, age in zip(names, ages):\n    print(f\"{name} is {age} years old\")\n```"
    },
    {
        "category": "DevOps",
        "cat_slug": "devops",
        "file": "docker-compose-up-d.md",
        "title": "Docker Compose Detached Mode",
        "content": "# Docker Compose Detached Mode\n\nTo run your docker-compose services in the background without tying up your terminal, use the `-d` (detached) flag:\n\n```bash\ndocker-compose up -d\n```\nYou can later view logs with `docker-compose logs -f`."
    },
    {
        "category": "Linux",
        "cat_slug": "linux",
        "file": "bash-brace-expansion.md",
        "title": "Bash Brace Expansion",
        "content": "# Bash Brace Expansion\n\nBrace expansion allows you to generate arbitrary strings. It's great for creating multiple files or directories.\n\n```bash\nmkdir -p project/{src,test,build,docs}\n```\nThis creates 4 subdirectories at once."
    },
    {
        "category": "DevOps",
        "cat_slug": "devops",
        "file": "aws-s3-sync.md",
        "title": "Syncing Folders with AWS S3",
        "content": "# Syncing Folders with AWS S3\n\nThe `aws s3 sync` command only uploads files that are new or have changed.\n\n```bash\naws s3 sync ./local-folder s3://my-bucket/path/\n```\nAdd `--delete` to remove files in the bucket that were deleted locally."
    },
    {
        "category": "Open Source",
        "cat_slug": "open-source",
        "file": "react-useeffect-cleanup.md",
        "title": "React useEffect Cleanup",
        "content": "# React useEffect Cleanup\n\nIf you set up a subscription or a timer in `useEffect`, return a cleanup function to prevent memory leaks.\n\n```javascript\nuseEffect(() => {\n  const timer = setInterval(() => console.log('Tick'), 1000);\n  return () => clearInterval(timer);\n}, []);\n```"
    },
    {
        "category": "Open Source",
        "cat_slug": "open-source",
        "file": "css-grid-center.md",
        "title": "Centering a Div with CSS Grid",
        "content": "# Centering a Div with CSS Grid\n\nCSS Grid provides the shortest way to perfectly center an element both vertically and horizontally.\n\n```css\n.container {\n  display: grid;\n  place-items: center;\n  height: 100vh;\n}\n```"
    },
    {
        "category": "Git",
        "cat_slug": "git",
        "file": "git-cherry-pick.md",
        "title": "Cherry-Picking Commits",
        "content": "# Cherry-Picking Commits\n\n`git cherry-pick <commit-hash>` applies the changes introduced by a specific commit onto your current branch.\n\nThis is useful when you want a specific bug fix from another branch without merging the entire branch."
    },
    {
        "category": "Git",
        "cat_slug": "git",
        "file": "git-stash-pop.md",
        "title": "Stashing Changes in Git",
        "content": "# Stashing Changes in Git\n\nIf you need to switch branches but aren't ready to commit your current work, stash it!\n\n```bash\ngit stash\n```\nWhen you come back, re-apply your changes with:\n```bash\ngit stash pop\n```"
    },
    {
        "category": "Linux",
        "cat_slug": "linux",
        "file": "linux-top-cmd.md",
        "title": "Monitoring Processes with Top",
        "content": "# Monitoring Processes with Top\n\nThe `top` command displays a real-time view of running processes.\n\nUseful shortcuts inside `top`:\n- `M`: Sort by memory usage\n- `P`: Sort by CPU usage\n- `k`: Kill a process (prompts for PID)\n- `q`: Quit"
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
subprocess.run(["git", "push"], check=True)
