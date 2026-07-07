# Amending the Last Commit

If you forgot to add a file or made a typo in the last commit message:

```bash
git add forgotten_file.txt
git commit --amend -m "new commit message"
```
Note: Do not amend commits that have already been pushed to a shared remote.