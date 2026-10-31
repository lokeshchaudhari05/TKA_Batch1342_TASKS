# check whether number iis even or odd
# num = int(input("Enter the number: "))
# if num % 2 == 0:
#     print(f"{num} is Even number. ")
# else:
#     print(f"{num} is Odd number. ")


# Check the num is positive, negative or Zero.
# num = int(input("Enter the number: "))
# if num == 0:
#     print(f"{num} is zero ")
# elif num > 0:
#     print(f"{num} is positive number. ")
# else:
#     print(f"{num} is negative number. ")

#reverse the num using for and while both a = 12345
# a = 12345
# rev = 0

# for i in str(a):
#     rev = int(i) + rev * 10

# print("Reverse number:", rev)


#Check num is palindrome or not
# a = 121
# temp = a
# rev = 0

# while a > 0:
#     digit = a % 10
#     rev = rev * 10 + digit
#     a = a // 10

# if temp == rev:
#     print("Palindrome Number")
# else:
#     print("Not Palindrome")
  

#Check the num is prime or not
# num = int(input("Enter the num: "))
# if num <= 0:
#     print(f"{num} is not prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f"{num} is not prime number")
#             break
#     else:
#         print(f"{num} is prime number")


# print 1 to 100 prime number
# Print prime numbers from 1 to 100
# for num in range(2, 101):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)


# find factorial
# num = int(input("Enter the number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)


# print square and cube of perticular number
# num = 7
# square = num ** 2
# cube = num ** 3

# print(f"Square of {num} is {square}")
# print(f"Cube of {num} is {cube}")


#Reverse a string without using slicing
# str1 = "python"
# rev =""

# for i in str1:
#     rev = i+rev
# print(rev)


#Print even & odd from the list 
# my_list = [12, 19, 23, 37, 45, 54, 68, 76]
# for ii in my_list:
#     if ii % 2 == 0:
#         print(f"{ii} is an even number")
#     else:
#         print(f"{ii} is an odd number")


# count even & odd from list
# even_count = 0
# odd_count = 0


# my_list = [12, 19, 23, 37, 45, 54, 68, 76]

# for ii in my_list:
#     if ii % 2 == 0:
#         print(f"{ii} is an even number")
#         even_count += 1
#     else:
#         print(f"{ii} is an odd number")
#         odd_count += 1

# print("Even count is",even_count)
# print("Odd count is",odd_count)


# reverse the list without defining the predefining function
# my_list = [12, 19, 23, 37, 45, 54, 68, 76]
# for i in my_list:
#     print(my_list[::-1])
#     break



#print prime nums from list
# my_list = [12, 19, 23, 37, 45, 54, 68, 76]
# for j in my_list:
#     if j <= 0:
#         print(f"{j} is not prime number")
#     else:
#         for i in range(2, j):
#             if j % i == 0:
#                  print(f"{j} is not prime number")
#             break
# else:
#       print(f"{j} is prime number")


# print only string from the list
# my_list = [12, 'ramesh', 19, 23, 'suresh', 37, 45, 54, 68, 76]
# for item in my_list:
#     if isinstance(item, str):
#         print(item)


# print int values from list
# my_list = [12, 'ramesh', 19, 23, 'suresh', 37, 45, 54, 68, 76]
# for item in my_list:
#     if isinstance(item, int):
#          print(item)


# find max in tuple
# my_tup = (17, 23, 37, 59)
# my_list = list(my_tup)
# # print(my_list)
# max_num = max(my_list)
# print(max_num)


# find min in tuple
# my_tup = (17, 23, 37, 59)
# my_list = list(my_tup)
# # print(my_list)
# min_num = min(my_list)
# print(min_num)


# find sum in tuple
# my_tup = (17, 23, 37, 59)
# my_list = list(my_tup)
# sum_tup = sum(my_list)
# print(sum_tup)


# find the length of the tuple without using len()
# my_tup = (12, 'ramesh', 19, 23, 'suresh', 37, 45, 54, 68, 76)
# length = 0
# for i in my_tup:
#     # print(i)
#     length += 1
# print("length of the tuple is",length)


# find the sum of the tuple elements
# my_tup = (12, 19, 23, 37, 45, 54, 68, 76)
# total = 0
# for item in my_tup:
#     total += item
# print(total)


# Display only even numbers from the tuple
# my_tup = (12, 19, 23, 37, 45, 54, 68, 76)
# for item in my_tup:
#     if item % 2 == 0:
#         print(item)


# Display all keys and values from dictionary
# my_dict = {"name" : "Rahul", "Age" : 24, "city" : "mumbai", "salary" : 55000}
# print(my_dict.items())


# find the total marks of all students
# my_dict = {"Aarav": [92, 88, 79, 85, 98],  "Diya": [78, 91, 88, 93, 95]}
# for name, marks in my_dict.items():
#     total = sum(marks)
# print(total)


# # display students who scored above 60
# students = {"Aman": 75, "Rohan": 55, "Priya": 88, "Neha": 60, "Kabir": 92}
# for name, score in students.items():
#     if score > 60:
#         print(f"{name}:{score}")

# count the number of students who passed 
# students = {"Aman": 75, "Rohan": 35, "Priya": 88, "Neha": 33, "Kabir": 92}
# for name, score in students.items():
#     if score > 35 :
#         print(f"{name}:Passed")
#     else:
#         print(f"{name}:failed")


# Find the highest marks in dictionary
# students = {"Aman": 75, "Rohan": 35, "Priya": 88, "Neha": 33, "Kabir": 92}
# highest_marks = max(students.values())
# print(highest_marks)