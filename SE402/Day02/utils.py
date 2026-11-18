# utils.py (a module: a .py file other files can import)
print("utils.py is running; __name__ is:", __name__)

def money(amount):
    return f"${amount:.2f}"

if __name__ == "__main__":
    #only runs when you type: python utils.py
    print("self-test:", money(78))