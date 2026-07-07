# Recovering Lost Commits with Reflog

If you accidentally delete a branch or hard reset, `git reflog` is your friend. It records all changes to the tip of branches.

```bash
git reflog
```
Find the commit hash you want to return to, then:
```bash
git checkout <commit-hash>
# or
git reset --hard <commit-hash>
```