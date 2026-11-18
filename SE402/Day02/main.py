# modules and imports 
# module = one .py file | package = folder of modules 
# __main__ = runs only when run directly
import os # a standard library module
os.chdir("SE402/Day02") # set working directory to this folder

import json # a standard library module
import utils # a module in the same folder
from storage import load # pulling a function from a module
import utils as u # give a module a short name (alias)

# write a data file before any step reads it 
with open("data/inventory.json", "w") as f:
    json.dump([{"name": "Pen", "qty": 12}], f, indent=2)

# call the funtion in the utils module
print(utils.money(0.5)) 

# # from-import needs no prefix
print(load("data/inventory.json"))

# # checking if short name (alias) is the same, and not a copy
print(u.money(2), u is utils)

# # the __main__guard
print("main.py: __name__ is", __name__)
if __name__ == "__main__":
    print("main.py was run directly")

