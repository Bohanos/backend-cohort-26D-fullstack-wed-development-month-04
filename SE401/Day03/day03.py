# stock_status function 
def stock_status(quantity: int) ->str:
    """This function accepts only integers and returns strings which is the stock label."""
    if quantity == 0:
        return "Out of stock"
    if quantity <= 5:
        return "Low stock"
    return "In stock"

# List 
# A list is an ordered group of values in square brackets []
# Tuple 
# A tuple in an ordered group of values in parenthese ()

items = ["pen", "book", "ruler"]
print(items)
print(len(items))

# Append an item to the list
items.append("bag") 
print(items)

print(items[0], items[-1], items[-3], len(items))
items.remove("bag")
items.pop(0)
for item in items:
    print(item)


tuple_items = ("egg", "beaf", "mutton", "turkey", "chicken")
print(tuple_items)
for tuple_item in tuple_items:
    print(tuple_item)

sliced_tuple = tuple_items[ : : -1]
steped_tuple = tuple_items[1:4:2]

print(sliced_tuple)
print(steped_tuple)

for i in range(1, 10, 3):
    print(i)


# dictionary
# a dictionary is an unorderd group of key and value pairs in curly braces {}
# set
# a set is a group of unique values in curly braces {} with no order and no position

item = {
    "name": "pen", 
    "quantity": 11,
}

item["name"] = "book"
item["price"] = 600
item["quantity"] = 7
print(item)

name = item["name"]
print(name)


# set
for key, value in item.items():
    print(f"{key}: {value}")

tags = {"school", "office", "state", "school"}
print(len(tags))
print(tags)

for index, value in enumerate(tags):
    print(f"Index {index}: {value}")

for tag in tags:
    print(tag)

# list of dictionaries
inventory = [
    {"name": "Pen", "qty": 12, "price": 0.2},
    {"name": "Book", "qty": 13, "price": 1.6}
]

total = 0
for item in inventory:
    print(item["name"]),
    stock_status(item["qty"])
    total += item["qty"] * item["price"]
print(total)