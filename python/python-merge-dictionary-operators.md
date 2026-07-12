# Merged Dictionary Operators in Python 3.9

Python 3.9 introduced the union operators to `dict`. You can use `|` to merge two dictionaries and `|=` to update a dictionary in place.

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dictionaries
merged = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}

# Update in place
dict1 |= dict2  # dict1 is now {'a': 1, 'b': 3, 'c': 4}
```
This is cleaner than using `{**dict1, **dict2}` or `dict1.update(dict2)`.