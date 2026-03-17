# def add():
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     sum = n1 + n2
#     mul = n1 * n2
#     sub = n1 - n2
#     div = n1 / n2
#     return sum, mul, sub, div

# result = add()
# print(result)

# def personalInfo(fname, lname):
#     print("First Name: ", fname)
#     print("Last Name: ", lname)

# fname = "Mann"
# lname = "Parekh"
# personalInfo(fname, lname)

# def cityName(city = "nagpur"):
#     print(city)

# cityName("Mumbai")
# cityName("Delhi")
# cityName()

def studentNames(*name):
    print(name)

studentNames("Mann", "Yash", "Ayush")