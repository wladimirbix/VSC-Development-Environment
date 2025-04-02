import math

# Variablen
pi_value = math.pi
radius = 5
circle_area = pi_value * radius**2

# Liste
fruits = ["apple", "banana", "cherry"]

# Dictionary
person = {"name": "John", "age": 30, "city": "New York"}


# Funktion
def greet(name: str) -> str:
    """Creates the function to Greet the user."""
    return f"Hello, {name}!"


# Funktion aufrufen
greeting = greet(person["name"])

# Ausgabe
print(f"The area of the circle is: {circle_area}")
print(f"Fruits list: {fruits}")
print(f"Person details: {person}")
print(greeting)
print("testing another prepush")
