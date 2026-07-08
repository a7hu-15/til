# Strict Zip in Python

In Python 3.10+, you can use `strict=True` with `zip()` to ensure all iterables are the same length. It raises a `ValueError` if they are not.

```python
list1 = [1, 2]
list2 = ['a', 'b', 'c']
# This will raise a ValueError
for x, y in zip(list1, list2, strict=True):
    print(x, y)
```