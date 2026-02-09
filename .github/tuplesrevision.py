# Create a tuple of 5 numbers and print it.
a = (1 , 2 , 3 , 4 , 5)
print(type(a)) # tuple are immutable

#  wap Create a tuple of your favorite colors
colors = ('red', 'blue', 'green', 'yellow', 'purple', 'red')
print(colors)
# wap lenght of tuple
print(len(colors)) # length of tuple
print(colors[0]) # access first color
print(colors[0:3]) # slicing
# wap to reverse the tuple
print(colors[::-1]) # reverse the tuple
colors = colors.index('yellow') # find index of 'green'
print(colors)
colors = colors.count('red') # count occurrences of 'red'
print(colors)

#wap to create a list of fruits entered by the user and print it
fruits = []
f1 = input("enter fruit name")
# fruits.append(f1)
f2 = input("enter fruit name")
fruits.append(f2)   
f3 = input("enter fruit name")
fruits.append(f3)
f4 = input("enter fruit name")
fruits.append(f4)
f5 = input("enter fruit name")
fruits.append(f5)
f6 = input("enter fruit name")
fruits.append(f6)
f7 = input("enter fruit name")
fruits.append(f7)
print(fruits)

#wap to  create to accept marks of 6 students and display them in a sorted manner
marks = []
f1 = input("enter marks")
marks.append(f1)
f2 = input("enter marks ")
marks.append(f2)  
f3 = input("enter marks ")
marks.append(f3)
f4 = input("enter marks ")
marks.append(f4)
f5 = input("enter marks ")
marks.append(f5)
f6 = input("enter marks ")
marks.append(f6)
marks.sort() # sort the marks
print(marks)