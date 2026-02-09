if else conditions in python.
a = int(input("enter your age:"))

if(a>=18):
    print("you are above the age of consent")
    print("you are good" )
          
else:
   print("you are below the age of consent")



 
"elif" condition in python.
a = int(input("enter your age:"))

if(a>=18):
    print("you are above the age of consent") # first check if
    print("you are good" )

    
elif(a==0):
    print("you are not entering a valid age") #then elif

elif(a<0):
    print("not a valid age to enter") # second elif

else:
   print("you are below the age of consent") #at last else
   

print("end of program")


wap to print yes if age is above 18.

age = int(input("enter your age:"))
if(age>=18):
    print("yes")
else:
    print("no")




# multiple if prgram.

a = int(input("enter your age:")) #this is independent If condition
if(a%2 == 0):  # first it will run.
    print("a is even")


if(a>=18):
    print("you are above the age of consent") # SECOND If condition having "elif else".
    print("you are good" )  # after first condition this will run and checks all else and elif.

    
elif(a==0):
    print("you are not entering a valid age") #then elif

elif(a<0):
    print("not a valid age to enter") # second elif

else:
   print("you are below the age of consent") #at last else
   

print("end of the program")  # not in any condition . this syntax is independent because its out of loop





        
 
