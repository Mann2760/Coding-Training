#WAP to perform arithemetic operations using functional programming approach
# Functions help us to achieve modularity approach
# import sys
# def addition(num1, num2):  #Called function
#     print("Addition = ", num1 + num2)

# def subtraction(num1, num2):  #Called function
#     print("Subtraction = ", num1 - num2)

# def multiplication(num1, num2):  #Called function
#     print("Multiplication = ", num1 * num2)

# def division(num1, num2):  #Called function
#     if num2 != 0:
#         print("Division = ", num1 / num2)
#     else:
#         print("Error: Division by zero is not allowed.")


# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     choice = int(input("Enter your choice from the above options: "))
#     if choice == 5:
#         sys.exit()
#     val1 = int(input("Enter the first value: "))
#     val2 = int(input("Enter the second value: "))
#     if choice == 1:
#         addition(val1, val2)
#     elif choice == 2:
#         subtraction(val1, val2)
#     elif choice == 3:
#         multiplication(val1, val2)
#     elif choice == 4:
#         division(val1, val2)
#     else:
#         print("You have entered an invalid choice")

#Nested function
# def outer_function():
#     print("This is the outer function")
#     def inner_function():
#         print("This is the inner function")
#     inner_function()  #Calling the inner function
# outer_function()  #Calling the outer function

#WAP to count the word
# name  = "Prashant is good programmer"
# count = 1
# for i in name:
#     if i == " ":
#         count += 1
#     else:
#         continue
# print("The number of words in the string is: ", count)

# init_tuple = ()
# print(init_tuple.__len__())

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a == init_tuple_b)

# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')
# print(init_tuple_a + init_tuple_b)

# l = [1, 2, 3]
# init_tuple = ('Python',) * (l.__len__() - l[::-1][0])

# init_tuple = ('Python') * 3
# print(type(init_tuple))

# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple)

# init_tuple = ((1, 2),) * 7
# print(len(init_tuple[3:8]))

# s =""
# s1 = s.replace("Difficult", "Easy")
# print(s1)
# # All occurences will be replaced
# s = "abababababababa"
# s1 = s.replace("a", "b")
# print(s1)

#Removing spaces from the string
# 1. rstrip() - removes spaces from the right hand side
# 2. lstrip() - removes spaces from the left hand side
# 3. strip() - removes spaces from both sides
# city = input("Enter your city name: ")
# scity = city.strip()
# if scity == "Hyderabad":
#     print("Hello Hyderabadi.. Adab")
# elif scity == "Chennai":
#     print("Hello Madarasi.. Vanakkam")
# elif scity == "Bangalore":
#     print("Hello Kannadiga.. Shubhodaya")
# else:
#     print("Your entered city is invalid")

# s = [i*i for i in range(1, 11)]
# print(s)

# val = [2**i for i in range(1, 6)]
# print(val)

# val2 = [i for i in s if i % 2 == 0]
# print(val2)

# squares = {x: x*x for x in range(1, 6)}
# print(squares)

doubles = {x: x**2 for x in range(1, 6)}
print(doubles)