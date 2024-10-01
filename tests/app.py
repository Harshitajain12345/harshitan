# tests/test_app.py
import pytest
from src.maths_operation import add, sub

# Test the add function
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Test the sub function
def test_sub():
    assert sub(5, 3) == 2
    assert sub(1, 1) == 0
    assert sub(0, 5) == -5

    