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
