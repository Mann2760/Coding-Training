# for i in range(1, 5):
#     print(i)

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)

# for i,j in zip(range(1, 6), range(5, 0, -1)):
#     print(i,'\t', j)

# username = ""
# password = ""

# while username != "admin" and password != "admin":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

# n = int(input("Enter number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i + 1
# print("Sum of first n numbers is", sum)

# name="Prashant"
# newname="Prashnt"
# for i in name:
#     if i not in newname:
#         newname=newname+i
# print(name)
# print(newname)

# mycart = [10, 20, 200, 300, 800, 60, 700]
# for i in mycart:
#     if i > 400:
#         print("This is my ourchased item")
#         continue
#     print(i)

# i = str(input("Enter Number: "))
# j = i[::-1]
# if i == j:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# i = str(input("Enter String: "))
# j = str(input("Enter String: "))
# if len(i) == len(j):
#     if sorted(i) == sorted(j):
#         print("Anagram")
#     else:
#         print("Not Anagram")
# else:
#     print("Not Anagram")