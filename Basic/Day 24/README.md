# [Learning Python-Basic course: Day 24, String Methods Part-3](https://dev.to/aatmaj/learning-python-basic-course-day-24-string-methods-part-3-1mg9)

Originally published on the dev.t platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-24-string-methods-part-3-1mg9)

## Today we will finally finish up with string methods. In case you missed the previous [part 1](https://dev.to/aatmaj/learning-python-basic-course-day-22-string-methods-part-1-9j8) and [part 2](https://dev.to/aatmaj/day-23-fi9) of string methods, then you can check them out.

String manipulation in Python can be implemented in a very easy way with the use of inbuilt, methods. This comes very handy when we need to manipulate strings while working with complex operations. For example, this saves a lot of code while working with 'front-endish' applications like GUI. Let's say we are writing a password management system and want to check if only alphanumeric vakyes are present. In such cases, the inbuilt functions save code wile compared to long nested for loops.

Another feature of string slicing can be very handy and save a lot of code, say when you want to reverse strings or take only a part of whole sentences.

---

In this part, I am presenting only sample programs, as the methods do not require much explaination and code is commented wherever necessary.

## Trimming Strings

We will now use inbuilt functions to trim strings into parts.

```python
print("\n 1. left justified")
str ="Python".ljust(10,".")
print(str)
print("\n 2. Right justified")
str ="Python".rjust(10,".")
print(str)
print("\n 3. Center Aligned")
str ="Python".center(10,".")
print(str)


#lstrip()	Returns a left trim version of the string
#rstrip()	Returns a right trim version of the string
#strip()	Returns a left and right trim version of the string


```

output-

```
 1. left justified
Python....

 2. Right justified
....Python

 3. Center Aligned
..Python..

```

## Stripping Strings

```python
print("\n****** left strip()*****\n")
st="   Python Level 2    "
print(st)
print("length = ", len(st))


lst =st.lstrip()     #trim
print(lst)
print("length = ", len(lst))


print(lst, "after the left strip method")

print("\n****** right strip()*****\n")

rst =st.rstrip()     #trim
print("length = ", len(rst))

print(rst, "after the right strip method")

print("\n****** strip()*****\n")

sst =st.strip()     #trim
print("length = ", len(sst))

print(sst, "after the strip method")
```

OUTPUT

```
****** left strip()*****

   Python Level 2
length =  21
Python Level 2
length =  18
Python Level 2     after the left strip method

****** right strip()*****

length =  17
   Python Level 2 after the right strip method

****** strip()*****

length =  14
Python Level 2 after the strip method

```

## Slicing Strings

```python
print("\n****** slicing of strings *****\n")

st = "Python Fundamentals"
print(st, "\t\tLength = ", len(st))

s1= st[2:8]
print("st[2:8]".ljust(20), s1)


s1= st[0:len(st)]
print("st[0:len(st)]".ljust(20), s1)

s1= st[0:4]
print("st[0:4]".ljust(20), s1)

s1= st[4:len(st)]
print("st[4:len(st)]".ljust(20), s1)

s1= st[3:-5]
print("st[3:-5]".ljust(20), s1)

s1= st[4:0]
print("st[4:0]".ljust(20), s1)

s1= st[4:]
print("st[4:]".ljust(20), s1)

s1= st[8:-1]
print("st[8:-1]".ljust(20), s1)

s1= st[8:-3]
print("st[8:-3]".ljust(20), s1)
```

OUTPUT

```
****** slicing of strings *****

Python Fundamentals 		Length =  19
st[2:8]              thon F
st[0:len(st)]        Python Fundamentals
st[0:4]              Pyth
st[4:len(st)]        on Fundamentals
st[3:-5]             hon Fundame
st[4:0]
st[4:]               on Fundamentals
st[8:-1]             undamental
st[8:-3]             undament

```

## Reversing of strings

```python
st="Learning Python Course"
# :: and -ve index to reverse the string
s1= st[4::-1]
print("st[4::-1]".ljust(20), s1)

s1= st[8::-2]
print("st[8::-2]".ljust(20), s1)

s1= st[::-1]
print("st[::-1]".ljust(20), s1)

s1= st[::-2]
print("st[::-2]".ljust(20), s1)

s1= st[1::-1]
print("st[1::-1]".ljust(20), s1)

s1= st[5:10][::-1]
print("st[5:10][::-1]".ljust(20), s1)

s1= st[4::3]
print("st[4::3]".ljust(20), s1)


```

OUTPUT

```
st[4::-1]            nraeL
st[8::-2]             nnaL
st[::-1]             esruoC nohtyP gninraeL
st[::-2]             ero otPgire
st[1::-1]            eL
st[5:10][::-1]       P gni
st[4::3]             ngyoCr
```

So friends that's all for this part. 😊 Hope you all are enjoying.😎 Please let me know in the [comment section on dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-24-string-methods-part-3-1mg9) if you liked it or not. 🧐 And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments there or gmail me. 😉
Thank you for being so patient.👍
