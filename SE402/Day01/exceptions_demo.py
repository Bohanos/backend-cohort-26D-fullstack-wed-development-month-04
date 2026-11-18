# Exceptions
import json
import os
os.chdir("SE402/Day01")

# Accepting user input without handling error
qty = int(input("Quantity: "))
print("You typed", qty)


# Accepting user input and handling error
try:
    qty = int(input("Quantity: "))
except ValueError:
    print("Enter a whole number.")
else:
    print("Ok:", qty)
finally:
    print("Done")


# Opening a file while catching error
try:
    open("missing.json")
except FileNotFoundError:
    print("File found")


# Catching and printing error as a variable
try:
    int("abc")
except ValueError as t:
    print("Value cannot be converted to integer.", t)
finally:
    print("Conversion was successful")


# error handling inside functions
def set_qty(q):
    if isinstance(q, str):
        raise TypeError("Enter a number")
    elif q < 0:
        raise ValueError("qty cannot be negative.")
    return q

try:
    print(set_qty(-20))
except TypeError as e:
    print(f"Input type error: {e}")
except ValueError as e:
    print(f"Input value error: {e}")