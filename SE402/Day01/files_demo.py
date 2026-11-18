import os
os.chdir("SE402/Day01")
# Reading and Writing Files

# open(path, mode)

f = open("notes.txt", "w")
f.write("pen,12\n")
f.close()


g = open("notes.txt", "r")
for line in g:
    print(line.strip())
g.close()


# Risk of opening and closing files manually 
# h = open("SE402/Day01/notes.txt", "w")
# try:
#     h.write(10)
# finally:
#     h.close()


# Avoiding the risks of files not closing, if an error was encountered
with open("notes.txt", "w") as f:
    f.write("New beginning\n")

with open("notes.txt", "w") as f:
    f.write("New beginning\n")

with open("notes.txt") as f:
    for line in f:
        print(line.strip())


# blank lines inside the file 
with open("notes.txt", "w") as f:
    f.write("pen,12\n\n\nBook,5\n")



# Appending to a file 
with open("notes.txt", "a") as f:
    f.write("Pencil,20\n")


with open("notes.txt") as f:
    for line in f:
        line = line.strip()
        if line != "":
            print(line)


