a = (1, 2, 3, 4, 5)
print(type(a))  # tuple 

a=(1,)  # single element tuple
print(type(a))

b=(1)  # not a tuple
print(type(b))

a = (1, 2, False, 4.5, "akash")
a[0] = 34  # tuples are immutable

print(a[0])  # accessing elements in tuple  

