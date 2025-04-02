# Test if True is True
def test_boolean() -> None:
    """Test to check if True is True."""
    if True is not True:
        raise ValueError("True is not True")


# Test if 3 is equal to 3
def test_equality() -> None:
    """Test to check if 3 is equal to 3."""
    if 3 != 3:
        raise ValueError("3 is not equal to 3")


# Test if a string is the same as another string
def test_string_comparison() -> None:
    """Test to check if a string is the same as another string."""
    if "hello" != "hello":
        raise ValueError("Strings are not equal")


# Test if a list contains an expected value
def test_list_contains() -> None:
    """Test to check if a list contains an expected value."""
    numbers = [1, 2, 3, 4, 5]
    if 3 not in numbers:
        raise ValueError("3 is not in the list")


# Test if a dictionary has a specific key
def test_dict_key() -> None:
    """Test to check if a dictionary has a specific key."""
    data = {"name": "Alice", "age": 30}
    if "name" not in data:
        raise ValueError("'name' key is not in the dictionary")


# Test if a function returns the expected result
def add(x: int, y: int) -> int:
    """Function to add two numbers."""
    return x + y


def test_function() -> None:
    """Test to check if the add function works correctly."""
    if add(2, 3) != 5:
        raise ValueError("Function did not return the expected result")


# Test if an exception is raised
def test_exception() -> None:
    """Test to check if a ZeroDivisionError is raised."""
    try:
        _ = 1 / 0  # Assigning the result to a variable
    except ZeroDivisionError:
        pass
    else:
        raise ValueError("ZeroDivisionError was not raised")
