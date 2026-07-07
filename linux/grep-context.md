# Grep Context Flags

When searching with `grep`, you often want to see the surrounding lines for context.

- `-A <num>`: Print <num> lines of trailing context **A**fter matching lines.
- `-B <num>`: Print <num> lines of leading context **B**efore matching lines.
- `-C <num>`: Print <num> lines of output **C**ontext.

```bash
grep -C 3 'error' /var/log/syslog
```