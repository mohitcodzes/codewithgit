# QUES1.Write a program to find the greatest of four numbers entered by the user
# a = int(input("enter your number:"))
# b = int(input("enter your number:"))
# c= int(input("enter your number:"))
# d = int(input("enter your number:"))
# if(a>b and a>c and a>d):
#     (" the greatest number is a:", a)
          
# elif(b>a and b>c and b>d):
#     ("greatest number is b:",b)

# elif(c>a and c>b and c>d ):
#     ("c is the greatest number:" , c) 

# elif(d>a and d>b and d>c):
#     ("d is the greatest number")

#QUES2.Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# marks1 = int(input("enter marks 1:"))
# marks2 = int(input("enter marks 2:"))
# marks3 = int(input("enter marks 3:"))

# total_percentage = (100*(marks1 + marks2 +marks3)/300)
# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     ("you are passed,congratulations:",total_percentage)

# else:
#     ("you are fail:","TRY again next year:",total_percentage)

#  QUES3.A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

# p1 = ("make a lot of money")
# p2 = ("buy now ")
# p3 = ("subscribe this")
# p4 = ("click this")

# message  = input("enter your message :")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     ("THIS IS A SPAM ")
# else:
#     ("THIS IS NOT A SPAM")


#QUES4.Write a program to find whether a given username contains less than 10
# characters or not.

# username = input("enter your username:")

# if(len(username)<10):
#     ("your username contains less than 10 characters")
# else:
#     ("your username contains more than 10 characters")

#QUES5.Write a program which finds out whether a given name is present in a list or not.

# l1 = ["mohit","rohit","hasim","dushyant"]

# name= input("enter name")
# if(name in l1):
#     ("list contains that name")
# else:
#     ("name not present in the list")

# QUES66. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# marks = int(input("Enter marks: "))

# if (marks >= 90 and marks <= 100):
#     grade = "Ex"
# elif (marks >= 80 and marks <=90):
#     grade = "A"
# elif (marks >= 70 and marks <= 80 ):
#     grade = "B"
# elif (marks >= 60 and marks <=70):
#     grade = "C"
# elif (marks >= 50 and marks <= 60):
#     grade = "D"
# elif (marks<50):
#     grade = "f"
# print("Your grade is:", grade)

# QUES7Write a program to find out whether a given post is talking about “Harry” or not.
post = input('enter your discription:')

if("Mohit".lower() in post.lower()):
    print("this post is talking about mohit ")
else:
   print ("this post is not talking about mohit")







