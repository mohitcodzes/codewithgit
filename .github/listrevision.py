#wap to create a list of friends with mixed data types and print it
friends = ['Alice', 'Bob', 'Charlie', 'Diana',345.07, True]
print(friends)
#wap to access and update elements in the list
print(friends[0])  # Print first friend
friends[0] =  'mohit' # Update first friend
print(friends)# list are mutable
print(friends[1:3]) #slicing
#wap to add and remove elements from the list
friends.append('Eve') # add element at the end
friends.remove('Bob') # remove element
print(friends)
friends.extend(['Frank', 'Grace']) # add multiple elements
print(friends)
#wap Insert an element at index 2
friends.insert(4, 'Zara')
print(friends)
#Remove the last element using pop().
friends.pop()
print(friends) # remove last element
# Remove any specific element by value using remove().
friends.remove('Charlie')
print(friends)