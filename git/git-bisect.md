# Finding Bugs with Git Bisect

`git bisect` is a binary search tool to find the commit that introduced a bug.

```bash
git bisect start
git bisect bad  # current commit is bad
git bisect good <commit-hash>  # a known good commit
```
Git will checkout intermediate commits, and you mark them as `git bisect good` or `git bisect bad` until it finds the exact commit.