import pytest

# Test if True is True
def test_boolean():
    assert True is True

# Test if 3 is equal to 3
def test_equality():
    assert 3 == 3

# Test if a string is the same as another string
def test_string_comparison():
    assert "hello" == "hello"

# Test if a list contains an expected value
def test_list_contains():
    numbers = [1, 2, 3, 4, 5]
    assert 3 in numbers

# Test if a dictionary has a specific key
def test_dict_key():
    data = {"name": "Alice", "age": 30}
    assert "name" in data

# Test if a function returns the expected result
def add(x, y):
    return x + y

def test_function():
    assert add(2, 3) == 5

# Test if an exception is raised
def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
