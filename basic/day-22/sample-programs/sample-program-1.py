#Interpreting the string as an array of characters.
txt = "Python"
print(txt)
print("Length of the txt = ", len(txt))

#display string using in keyword
for ch in txt:
    print(ch)

#display the string in original form using range()
for ch in range(0, len(txt)):
    print(txt[ch], end=" ")

print()
#to display in reverse order
for ch in range(len(txt) - 1, -1, -1):
    print(txt[ch], end="")

#We cannot append a character or pop using the standered length functions.
txt.append("a")
print(txt)
