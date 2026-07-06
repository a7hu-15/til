# How to Review a Pull Request

When reviewing a PR on GitHub, here's what to look for:

## The Basics

1. **Read the PR description** — Understand what the PR is trying to do
2. **Check the "Files changed" tab** — See what code was added/removed
3. **Look at the tests** — Are there tests for the new code?
4. **Check for edge cases** — What could go wrong?

## What to Comment

- ✅ **Good:** "This looks clean, nice use of error handling"
- ✅ **Good:** "Could this cause issues if the input is empty?"
- ❌ **Bad:** "LGTM" (with no context)
- ❌ **Bad:** "This is wrong" (without explaining why)

## Types of Reviews

| Type | When to use |
|------|-------------|
| **Comment** | General feedback, questions, or suggestions |
| **Approve** | Code looks good, ready to merge (only if you're a collaborator) |
| **Request Changes** | Something needs to be fixed before merging |

## Pro Tips

- Be kind and constructive — the author put effort into this
- Ask questions instead of making demands
- If you don't understand something, say so — it's okay!
- Suggest improvements, don't just point out problems

## My First Review

Today I reviewed [Trivy PR #10923](https://github.com/aquasecurity/trivy/pull/10923) — a fix for OpenTofu language block support. It was a small, focused change (just 2 files) which made it easy to understand.

**Key takeaway:** Start with small PRs. Reading 2 changed files is way less scary than 20.
