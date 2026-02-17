# nested_getitem

A small utility function for retrieving values from nested Python data structures
(lists and dictionaries) using a sequence of keys and/or indices.

## Description

The `nested_getitem` function allows you to access elements inside nested `list`
and `dict` objects by providing a path to the target element as a list or tuple.

Conceptually, it is a safe and readable wrapper around chained indexing like:

```
data[k1][k2][k3] ...
```

## Function signature

```python
def nested_getitem(data: list | dict, keys: tuple | list) -> object:
    ...
```

- `data` — the source data structure (a list or a dictionary)
- `keys` — a sequence of keys and/or indices describing the path
- returns the extracted value

## Implementation

```python
def nested_getitem(data: list | dict, keys: tuple | list) -> object:
    current = data
    for key in keys:
        current = current[key]
    return current
```

## Usage examples

```python
nested_getitem([99], (0,))
# 99

nested_getitem([[333, 555], [44, 22]], (0, 1))
# 555

nested_getitem({'a': 222}, ('a',))
# 222

nested_getitem({'a': {'b': 333}}, ('a', 'b'))
# 333

nested_getitem({'a': {'b': [88, 99]}}, ('a', 'b', 1))
# 99

nested_getitem([{}, {'c': 111}], (1, 'c'))
# 111
```

## Purpose

This function is useful when working with:

- JSON data
- configuration files
- API responses
- deeply nested Python data structures

## Limitations

The function does not perform additional validation of keys or indices.
If the provided path is invalid, standard Python exceptions will be raised
(`KeyError`, `IndexError`, or `TypeError`).

## Requirements

- Python 3.10+
