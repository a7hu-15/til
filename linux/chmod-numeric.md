# Numeric Permissions in Chmod

Numeric mode uses 3 digits for Owner, Group, and Others.

- 4 = Read (r)
- 2 = Write (w)
- 1 = Execute (x)

Add them up to set combinations:
- `7` = 4+2+1 = Read/Write/Execute
- `6` = 4+2 = Read/Write
- `5` = 4+1 = Read/Execute

Example: `chmod 755 script.sh`