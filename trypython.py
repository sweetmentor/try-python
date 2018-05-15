# print('Hello World')
# print('Welcome To Python')
# response = input("what's your name? ")
# print('Hello' + response)

# 
# print('please enter two numbers')
# a = int(input('enter number 1:'))
# b = int(input('enter number 2:'))
# print(a + b)

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# total = num1 + num2
# print (str(num1))

#print(str(num1) + " plus " + str(num2) + " = " + str(total))

# print("Before the function")
#--------------------------------------
# def add(x, y):
#     print(x)
#     print(y)
#     return x + y

# print("After the function")

# print("Before calling the function")
    
# r = add(5, 4)

# print("After calling the function")

# print(r)

# print("After printing the result")

# text = input("what is your name:")
# text = text.upper()

# print(text)

#-------------------challenge47----
# num = int(input("please enter your number"))
# if num <= 10:
#     print ("Small")
# else:
#     print ("Big")
#-------------------challenge48----
# num1 = int(input("enter num1:"))
# num2 = int(input("enter num2:"))
# if num1 == num2:
#     print ("Same")
# else:
#     print ("Different")
#-------------challenge49-------
# num = input("enter a number:")
# if num == "1":
#     name = input("please enter your name")
#     print ("Your name is %s" % name)
# if num == "2":
#     age = input("enter your age: ")
    
#     age_int = int(age)
#     print ("Your age is " + age)
#   print("done")
#----------------------------

# i = 0
# while i < 100:
#     print(i)
#     i += 2
# i = 0
# while i < 100:
#     print(i)
#     i += 1
# i = 0
# while i < 100:
#     i += 1
#     print(i)
#----------------------------------
# people = {
#     "Joe": 23, 
#     "Ann": 24, 
#     "Barbara": 67, 
#     "Pete": 55, 
#     "Tim": 34, 
#     "Sam": 13, 
#     "Josh": 5
# }

# name = input("Enter name: ")
# print (people[name])
#-----------------------------------

# people = {
#     "Joe": {"age": 23, "eyes": "blue", "height": 134, "nationality": "Irish"}, 
#     "Ann": {"age": 13, "eyes": "green", "height": 172, "nationality": "Irish"}, 
#     "Bob": {"age": 23, "eyes": "red", "height": 234, "nationality": "Turkmenistan"}, 
#     "Sam": {"age": 45, "eyes": "grey", "height": 134, "nationality": "French"}, 
#     "Tina": {"age": 46, "eyes": "blue", "height": 154, "nationality": "American"}, 
# }

# name = input("Enter name: ")
# person = people[name]

# what = input("What do you want to know? ")
# print (person[what])
#--------------------------------------------

# total = 0
# for i in range(10):
#     number = int(input("Enter a number: "))
#     total += number
    
# print(total)
#---------------------Challenge 50 solution
#-----getting total in a dictionary-----
# total = 0
# for name in people:
#   total += people[name]['height']
# print(total)
#----------53-----------
# def add(a, b):
#     return a + b
# i = add(3, 5)
# print (i)
#--------------------54-------

# def add(a, b):
#     return a + b
# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# i = add(a, b)
# print (i)
# #-----------------------55-----------------

# def function(n):
#     if n %2 == 0:
#         return True
#     else:
#         return False
#-----or return n %2 == 0:  
# print(function(4))

    
# --------------------------56------------------        
    
# def message():
#     return ("This is the message")
    
# print(message())

#---------------------------------57------------------

# # r = list(range(0, 99))
# r = list(range(16, 10, 2)): 
# print(r)
# # print(r[50])
# --------------------------
# # r = range(10, 51, 2)
# # print(list(r))
# -----------------------------

# outerlist = []
# for i in range (7):
#     innerlist = list(range(i))
#     outerlist.append(innerlist)
# print(outerlist)
#--------------60------------------------
#-------- Unrolled Loop solution for 60 
# outerList = []

# innerList = list(range(1))
# outerList.append(innerList)

# innerList = list(range(2))
# outerList.append(innerList)

# innerList = list(range(3))
# outerList.append(innerList)

# innerList = list(range(4))
# outerList.append(innerList)

# innerList = list(range(5))
# outerList.append(innerList)

# innerList = list(range(6))
# outerList.append(innerList)

# innerList = list(range(7))
# outerList.append(innerList)

# print(outerList)
# ---------Loop solution for 60 
# outerList = []

# for i in range(1, 8):
#     innerList = list(range(i))
#     outerList.append(innerList)


# print(outerList)
# items = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
# # print(item[2:6])
# print(items[:-1])

# ---63----
# student = { 'name': 'Richard', 'age': 21, 'nationality': 'Irish', 'subjects': ['Maths', 'Art', 'History']}
# students = [
#     { 'name': 'Richard', 'age': 21, 'nationality': 'Irish', 'subjects': ['Maths', 'Art', 'History']},
#     { 'name': 'Mary', 'age': 22, 'nationality': 'Oz', 'subjects': ['Maths', 'Art', 'History']},
#     { 'name': 'Anne', 'age': 23, 'nationality': 'Spanish', 'subjects': ['Maths', 'Art', 'History']},
#     { 'name': 'Joe', 'age': 24, 'nationality': 'USA', 'subjects': ['Maths', 'Art', 'History']}
#     ]
    
student = { 'name': 'Richard', 'age': 21, 'nationality': 'Irish', 'subjects': ['Maths', 'Art', 'History']}
students = {
    'Richard':{ 'name': 'Richard', 'age': 21, 'nationality': 'Irish', 'subjects': ['Maths', 'Art', 'History']},
    'Mary':{ 'name': 'Mary', 'age': 22, 'nationality': 'Oz', 'subjects': ['Maths', 'Art', 'History']},
    'Anne':{ 'name': 'Anne', 'age': 23, 'nationality': 'Spanish', 'subjects': ['Maths', 'Art', 'History']},
    'Joe':{ 'name': 'Joe', 'age': 24, 'nationality': 'USA', 'subjects': ['Maths', 'Art', 'History']}
    }  
    
for subject in student['subjects']:
    print(subject)
    


