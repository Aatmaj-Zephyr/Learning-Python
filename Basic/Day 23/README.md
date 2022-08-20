# [Learning Python-Basic course: Day 23, String Methods Part-2](https://dev.to/aatmaj/day-23-fi9)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/day-23-fi9)

## Today we cover more about string functions.

---

String functions are inbuilt methods to modify and change strings. In case you missed yesterday's part, [click here](https://dev.to/aatmaj/learning-python-basic-course-day-22-string-methods-part-1-9j8).

## String functions for GUI.

>

- isalpha()- to check if all characters are alphabets.
- isalnum()- to check if all characters are alphanumeric.
- isdigit()- to check if all characters are digits.
- islower()- to check if all characters are lower case.
- isspace()- to check if all characters are blank spaces.
- istitle()- to check if all characters [follow title rules](<https://www.w3schools.com/python/ref_string_title.asp#:~:text=The%20title()%20method%20returns,be%20converted%20to%20upper%20case.>).
- isupper()-to check if all characters are upper case.

The methods above are useful especially when we deal with GUI. For example, when we want the users to enter only alphanumeric values for passwords, alphabets for names and only digits for pin-codes These are useful to prevent errors in complex operations like OOP, GUI or file reading which we will cover in the next module.

```python

txt=" Computer Academy"
print(txt)

#Returns True if all characters in the string are alphabets
print("1.", "\tisalpha()\t", txt.isalpha())


#Returns True if all characters in the string are only alphanumeric
txt="Level1"
print("\n",txt)
print("2.", "\tisalnum()\t", txt.isalnum())


#Returns True if all characters in the string are digits
txt="1154"
print("\n",txt)
print("3.", "\tisdigit()\t", txt.isdigit())


#Returns True if all characters in the string are lower case
txt="computer academy"
print("\n",txt)
print("4.", "\tislower()\t", txt.islower())


#Returns True if all characters in the string are whitespaces
txt="computer academy"
print("\n",txt)
print("5.", "\tisspace()\t", txt.isspace())


#Returns True if the string follows the rules of a title
txt="Computer Academy"
print("\n",txt)
print("6.", "\tistitle()\t", txt.istitle())


#Returns True if all characters in the string are upper case
txt="PYTHON PROGRAMMING"
print("\n",txt)
print("7.", "\tisupper()\t", txt.isupper())
```

Output-

```
 Computer Academy
1. 	isalpha()	 False

 Level1
2. 	isalnum()	 True

 1154
3. 	isdigit()	 True

 computer academy
4. 	islower()	 True

 computer academy
5. 	isspace()	 False

 Computer Academy
6. 	istitle()	 True

 PYTHON PROGRAMMING
7. 	isupper()	 True

```

## Exercise-

Write a program to check if a string is alphabetic, numeric or alphanumeric or none.. answer in the [Learning Python repo](https://github.com/Aatmaj-Zephyr/Learning-Python)

---

So friends that's all for this part. 😊 Hope you all are enjoying.😎
Please let me know in the [comment section on dev.to](https://dev.to/aatmaj/day-23-fi9) if you liked it or not.
🧐 And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the [comments on dev.to](https://dev.to/aatmaj/day-23-fi9) or gmail me. 😉
Thank you for being so patient.👍
