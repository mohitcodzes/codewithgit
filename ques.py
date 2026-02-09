#wap to create a dictonary of hindi words with values as their english translation.provide user with an option to look it up.

# words = {
# "kal": "tommorow",
# "aaj": "today",
# "paani": "water",
# "raat": "night",
# }
# word = input("enter the word you want:")
# print(words[word])

#wap to input 8 numbers from the user and display all unique numbers once.

# s = set()
# n = input("enter number 1")
# s.add(int(n))
# n = input("enter number 2")
# s.add(int(n))
# n = input("enter number 3")
# s.add(int(n))
# n = input("enter number 4")
# s.add(int(n))
# n = input("enter number 5")
# s.add(int(n))
# n = input("enter number 6")
# s.add(int(n))
# n = input("enter number 7")
# s.add(int(n))
# n = input("enter number 8")
# s.add(int(n))
# print(s)

#wap a set having 18 integer and 18 string

s = set()
s.add(18)
s.add("18") #yes we can have both value because each one is different.
print(s)


# wapWhat will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# s= set()
# s.add(20)
# s.add(20.0) # Gives only two values "20"str, 20 int. BECAUSE the value of 20.0 is numerically
# s.add('20') #same as 20.0 . the len of this seet is 2.
# print(len(s))

#Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique
d = {}
name = input("enter friend name:")
lang = input ("enter language:")
d.update({name : lang})
name = input("enter friend name:")
lang = input ("enter language:")
d.update({name : lang})
name = input("enter friend name:")
lang = input ("enter language:")
d.update({name : lang})
name = input("enter friend name:")
lang = input ("enter language:")
d.update({name : lang})
print(d)