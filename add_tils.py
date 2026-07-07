import os
import subprocess
import re

tils = [
    {
        "category": "Git",
        "cat_slug": "git",
        "file": "git-bisect.md",
        "title": "Finding Bugs with Git Bisect",
        "content": "# Finding Bugs with Git Bisect\n\n`git bisect` is a binary search tool to find the commit that introduced a bug.\n\n```bash\ngit bisect start\ngit bisect bad  # current commit is bad\ngit bisect good <commit-hash>  # a known good commit\n```\nGit will checkout intermediate commits, and you mark them as `git bisect good` or `git bisect bad` until it finds the exact commit."
    },
    {
        "category": "Git",
        "cat_slug": "git",
        "file": "git-reflog.md",
        "title": "Recovering Lost Commits with Reflog",
        "content": "# Recovering Lost Commits with Reflog\n\nIf you accidentally delete a branch or hard reset, `git reflog` is your friend. It records all changes to the tip of branches.\n\n```bash\ngit reflog\n```\nFind the commit hash you want to return to, then:\n```bash\ngit checkout <commit-hash>\n# or\ngit reset --hard <commit-hash>\n```"
    },
    {
        "category": "Linux",
        "cat_slug": "linux",
        "file": "grep-context.md",
        "title": "Grep Context Flags",
        "content": "# Grep Context Flags\n\nWhen searching with `grep`, you often want to see the surrounding lines for context.\n\n- `-A <num>`: Print <num> lines of trailing context **A**fter matching lines.\n- `-B <num>`: Print <num> lines of leading context **B**efore matching lines.\n- `-C <num>`: Print <num> lines of output **C**ontext.\n\n```bash\ngrep -C 3 'error' /var/log/syslog\n```"
    },
    {
        "category": "Linux",
        "cat_slug": "linux",
        "file": "chmod-numeric.md",
        "title": "Numeric Permissions in Chmod",
        "content": "# Numeric Permissions in Chmod\n\nNumeric mode uses 3 digits for Owner, Group, and Others.\n\n- 4 = Read (r)\n- 2 = Write (w)\n- 1 = Execute (x)\n\nAdd them up to set combinations:\n- `7` = 4+2+1 = Read/Write/Execute\n- `6` = 4+2 = Read/Write\n- `5` = 4+1 = Read/Execute\n\nExample: `chmod 755 script.sh`"
    },
    {
        "category": "DevOps",
        "cat_slug": "devops",
        "file": "docker-cleanup.md",
        "title": "Cleaning Up Docker Resources",
        "content": "# Cleaning Up Docker Resources\n\nTo free up space by removing all stopped containers, unused networks, dangling images, and build cache, use:\n\n```bash\ndocker system prune\n```\n\nTo also remove all unused images (not just dangling ones) and volumes:\n\n```bash\ndocker system prune -a --volumes\n```"
    },
    {
        "category": "DevOps",
        "cat_slug": "devops",
        "file": "kubectl-port-forward.md",
        "title": "Kubectl Port Forwarding",
        "content": "# Kubectl Port Forwarding\n\nYou can access internal Kubernetes services or pods directly from your local machine.\n\n```bash\nkubectl port-forward svc/my-service 8080:80\n```\nThis forwards your local port 8080 to the service's port 80."
    },
    {
        "category": "Git",
        "cat_slug": "git",
        "file": "git-commit-amend.md",
        "title": "Amending the Last Commit",
        "content": "# Amending the Last Commit\n\nIf you forgot to add a file or made a typo in the last commit message:\n\n```bash\ngit add forgotten_file.txt\ngit commit --amend -m \"new commit message\"\n```\nNote: Do not amend commits that have already been pushed to a shared remote."
    },
    {
        "category": "Linux",
        "cat_slug": "linux",
        "file": "tar-extract.md",
        "title": "Extracting Tar Gz Archives",
        "content": "# Extracting Tar Gz Archives\n\nThe most common way to extract a `.tar.gz` file:\n\n```bash\ntar -xzvf archive.tar.gz\n```\n- `x`: eXtract\n- `z`: filter through gZip\n- `v`: Verbose output\n- `f`: File name follows"
    }
]

def update_readme(entry):
    with open("README.md", "r") as f:
        content = f.read()
    
    # Add link to category
    category_header = f"## {entry['category']}\n\n"
    if category_header in content:
        link = f"- [{entry['title']}]({entry['cat_slug']}/{entry['file']})\n"
        if "- _Coming soon_\n" in content.split(category_header)[1].split("##")[0]:
            content = content.replace(category_header + "- _Coming soon_\n", category_header + link)
        else:
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

for entry in tils:
    os.makedirs(entry['cat_slug'], exist_ok=True)
    with open(f"{entry['cat_slug']}/{entry['file']}", "w") as f:
        f.write(entry['content'])
        
    update_readme(entry)
    
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"docs({entry['cat_slug']}): add TIL on {entry['title'].lower()}"], check=True)
    
print("Running git push...")
subprocess.run(["git", "push"], check=True)
