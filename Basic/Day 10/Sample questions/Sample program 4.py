names=["Aatmaj", "123", "zephyr","163","1723"]
#1
print("Names in the list :")
print(names)

print("\n Frequency of 'zephyr' in the list\n")
print(names.count("zephyr"))

print("\n Index of '163' in the list\n")
print(names.index("163"))

print("Adding A in the list")
names.append("A")
print("No. of values in the list = ", len(names))
print(names)
print("New list as last names")
lastnames=["L","M","N"]
print(lastnames)
print("names.extend(lastnames)")
names.extend(lastnames)
print("New values in the names list")
print(names)
print("Inserting new names O, at index 4 ")
names.insert(4, "O")
print(names)
print("Removing A from the list ")
names.remove("A")
print(names)
print("pop() function removes the last value from the list")
names.pop()
print(names)
#names.remove(2) #error msg
print("pop() accepts index and string as an argument")
names.pop(3)
print(names)
print("Reverse of a string")
names.reverse()
print(names)
