# Viewing Commit History as a Graph

To visualize branch structures, merges, and commit history directly in the terminal, use the `--graph` flag with `git log`.

```bash
git log --oneline --graph --all
```
You can create a custom alias for this to make it easier to run:
```bash
git config --global alias.adog "log --all --decorate --oneline --graph"
```
Now running `git adog` gives a beautiful text representation of your commit graph.