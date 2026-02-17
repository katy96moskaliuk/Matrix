# Matrix and SquareMatrix

This project contains a simple implementation of matrix operations in Python and a test suite written with pytest.

## Files

- `matrix.py` – implementation of the `Matrix` and `SquareMatrix` classes
- `test_matrix.py` – unit tests for the matrix classes

---

## matrix.py

### Matrix

`Matrix` represents a 2D matrix based on a list of lists.

Example:

```python
from matrix import Matrix

A = Matrix([[1, 2], [3, 4]])
```

### Supported operations

- Matrix addition

```python
A + B
```

- Matrix subtraction

```python
A - B
```

- Multiplication by a number (scalar)

```python
A * 2
2 * A
```

- In‑place multiplication by a number

```python
A *= 2
```

- Matrix multiplication (using the @ operator)

```python
A @ B
```

- Transpose (property)

```python
A.transpose
```

- Equality comparison

```python
A == B
```

### Validation

- An empty matrix is not allowed.
- All rows must have the same length.
- Matrix addition and subtraction require matrices of the same size.
- Matrix multiplication requires compatible shapes.

---

### SquareMatrix

`SquareMatrix` is a subclass of `Matrix` and represents only square matrices.

```python
from matrix import SquareMatrix

M = SquareMatrix([[1, 2], [3, 4]])
```

#### Determinant

The determinant is available as a property and is currently implemented only for 2×2 matrices.

```python
M.determinant
```

---

## test_matrix.py

This file contains automated tests written with `pytest`.

The tests cover:

- matrix addition
- matrix subtraction
- multiplication by a scalar
- transpose
- matrix multiplication using `@`
- determinant of a square matrix
- validation errors for invalid and empty matrices

---

## How to run the tests

Install pytest (if it is not installed):

```bash
pip install pytest
```

Run the tests from the project directory:

```bash
pytest
```

---

## Python version

Python 3.10 or newer is recommended.
