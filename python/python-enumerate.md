# Using Enumerate in Python

When looping over an iterable, `enumerate()` allows you to keep track of the index automatically.

```python
names = ['Alice', 'Bob', 'Charlie']
for i, name in enumerate(names):
    print(f"{i}: {name}")
```
This is much cleaner than using `range(len(names))`.