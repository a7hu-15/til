# Iterating Multiple Lists with Zip

`zip()` takes multiple iterables and aggregates them into tuples.

```python
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```