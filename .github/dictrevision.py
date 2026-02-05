marks = {
"mohit": 85,
"rohit":88,
"mehul" :90,
"rahul":100,   
}
# print(marks,type(marks))
# print(marks["mohit"]) # access marks of mohit
print(marks.keys()) # print all keys
print(marks.values()) # print all values
print(marks.items()) # print all key-value pairs
# wap to update marks of mohit to 95
marks["mohit"] = 95
print(marks)
# wap to add marks of a new student 'sahil' with marks 80
marks["sahil"] = 80
print(marks)
# wap to remove marks of 'rohit'
del marks["rohit"]
print(marks)
# wap to check if 'mehul' is in the marks dictionary
print("mehul" in marks) # check if 'mehul' is in the dictionary
# wap to print the number of students in the marks dictionary
print(len(marks)) # print number of students
# wap to clear all marks from the dictionary
marks.clear() # clear all marks
print(marks)
# wap to create a dictionary of 5 countries and their capitals and print it
countries = {
"India": "New Delhi",  
"USA": "Washington D.C.",
"France": "Paris",
"Japan": "Tokyo",
}
print(countries)


