a={
    "list":[1,2,3,4],
    "tuple":(1,2,3,4)
}
print(a)
print(a["list"])
print(a["tuple"])
a["list"].append(a["tuple"])
print(a)
