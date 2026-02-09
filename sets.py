# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
s = {1,2,34,5,5,3,5,88}
print(type(s))
print(s) # repetition is not allowed in set

# Set operations and methods

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2)) # union of two sets 

print(s1.intersection(s2)) # intersection of two sets

s1.add(10) # add an element in set
print(s1)

s1.remove(2) # remove an element from set
print(s1)

s1.clear() # clear the set
print(s1)