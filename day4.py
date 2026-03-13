# for i in range(1, 5):
#     print(i)

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)

# for i,j in zip(range(1, 6), range(5, 0, -1)):
#     print(i,'\t', j)

username = ""
password = ""

while username != "admin" and password != "admin":
    username = input("Enter username: ")
    password = input("Enter password: ")