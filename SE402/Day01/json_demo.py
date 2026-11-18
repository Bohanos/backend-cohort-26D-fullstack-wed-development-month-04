# JSON files 
import json
import os
os.chdir("SE402/Day01")

# Save a list of dictionary using dump
items = [{"name": "Pen", "qty": 12}, {"name": "Book", "qty": 15}]
with open("inventory.json", "w") as f:
    json.dump(items, f, indent=2)


# load from the file 
with open ("inventory.json") as f:
    data = json.load(f)
print(data[0]["name"])
for item in data:
    print(item["name"], item["qty"])


# Dumping texts 
text = json.dumps({"name": "Pen", "ok": True, "note": None})
print(text)

# loading the texts
back = json.loads(text)
print(back["note"])

print(type(text))

# dump() writes to a file while dumps() makes a 
# string for printing or sending through an API

