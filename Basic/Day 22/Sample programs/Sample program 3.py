#1.Print the word "computer", taking up the space of 25 characters,
#with "computer" in the middle:
txt = "computer"
x = txt.center(25)

print("hello", x, "world")
# 2 default spaces+25 total characters. so distance between hello and world must be 27 characters.

#2. Return the number of times the value "act" appears in the string:
txt = "I love programming, programming is my favorite activity"
print(txt)
x = txt.count('i')

print("Frequency of the value =", x)
#case matters. Capital I and small i are treated differently.

#3. Check if the string ends with a punctuation sign .
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

#4. Set the tab size to 5 whitespaces:
print("First\tsecond")
txt1 = "ACADEMY"

txt = "A\tC\tA\tDE\tM Y"  # backslah t (i.e. \t) represents tab space.
x = txt.expandtabs(6)  #expands the tab spaces
print(x)

#5. Locates the word "welcome" in the string and returns the index:
txt = "Hello, welcome to my world."
print(txt)
x = txt.find("welcome")
print(x)
#output : 7
#if the result is -1, string does not exist in the sentence
