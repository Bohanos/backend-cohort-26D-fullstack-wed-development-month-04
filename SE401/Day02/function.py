# Functions

#Empty function
def add(length, width):
    pass

print(add(5, 7))


# function for toatl value
def total_value(quantity, unit_price=40):
    return quantity * unit_price


print(total_value(9))


# function to add two number that returns a value
def add(a: int, b: int):
    return a + b


# function to subtract two numbers but doesn't return a value
def subtract(a, b):
    print("So Good")


added_numbers = add(9, 7)
print(added_numbers)

num = subtract(6, 4)


num1 = 9
num2 = 10


def multiply(a, b) -> int:
    return a * b

print(multiply(num1, num2))


def division():
    num5 = 20
    num7 = 5
    return num5 / num7


print(division())

def power(a, b):
    return a ** b

print(power(num1, num2))


# Type Hints/function documentation/decomposition
# This function accepts only integers and returns strings
def stock_status(quantity: int) ->str:
    """This function accepts only integers and returns strings which is the stock label."""
    if quantity == 0:
        return "Out of stock"
    if quantity <= 5:
        return "Low stock"
    return "In stock"

print(stock_status(5))

# function decomposition
def iseven(a):
    num = a * 3
    if num % 2 == 0:
        print ("The number you entered is an even number")
    else:
        print("You just entered an odd number")

# the below mul_input() and check_even() functions still 
# return the same output as the is_even() function.
# This is an example of function decomposition
def mul_input(a):
    return a * 3

def check_even(a):
    num = mul_input(a = 7)
    if num % 2 == 0:
        print ("The number you entered is an even number")
    else:
        print("You just entered an odd number")


iseven(7)
check_even(7)
