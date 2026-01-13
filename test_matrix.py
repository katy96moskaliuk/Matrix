import pytest
from matrix import Matrix, SquareMatrix

def test_addition():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    result = A + B
    assert result == Matrix([[6, 8], [10, 12]])
    
def test_sub_matrices():
    A = Matrix([[10, 10], [10, 10]])
    B = Matrix([[1, 1], [1, 1]])
    result = A - B
    assert result == Matrix([[9, 9], [9, 9]])
    
def test_mul_by_number():
    A = Matrix([[1, 1], [1, 1]])
    assert A * 2 == Matrix([[2, 2], [2, 2]])
    assert 2 * A == Matrix([[2, 2], [2, 2]])
    
def test_transpose():
    A = Matrix([[2, 2, 2], [1, 1, 1]])
    assert A.transpose == Matrix([[2, 1], [2, 1], [2, 1]])
    
def test_matmull():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    result = A @ B
    assert result == Matrix([[19, 22], [43, 50]])
    
def test_determinant_squsre_matrix():
    M = SquareMatrix([[2, 2], [2, 2]])
    assert M.determinant == 0