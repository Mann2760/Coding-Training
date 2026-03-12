# mylist = [44, 22, 77, 0, 9, 68]
# mylist.sort()
# print(mylist)

# math = 50
# phy = 50

# print(id(math))
# print(id(phy))

# for i in range(1, 11):
#     print(i*1, '\t', i*2, '\t', i*3, '\t', i*4, '\t', i*5, '\t', i*6, '\t', i*7, '\t', i*8, '\t', i*9, '\t', i*10)

# print('\n')

# for i in range(1, 11):
#     print(i*11, '\t', i*12, '\t', i*13, '\t', i*14, '\t', i*15, '\t', i*16, '\t', i*17, '\t', i*18, '\t', i*19, '\t', i*20)

#Simple if
#WAP to accept any digit and check that pos, neg, zero
# num = int(input('Enter a number: '))
# if num > 0:
#     print('Positive')
# if num < 0:
#     print('Negative')
# if num == 0:
#     print('Zero')

# day = str(input('Enter a day number: '))
# if day == 'Saturday' or day == 'Sunday' or day == 'saturday' or day == 'sunday':
#     print('Holiday')
# else:
#     print('Working day')

#WAP to accept three paper marks and calculate total, percentage and if percentage is greater than 60 then print he/she is eligible for placement

# mark1 = int(input('Enter paper 1 marks: '))
# mark2 = int(input('Enter paper 2 marks: '))
# mark3 = int(input('Enter paper 3 marks: '))

# total = mark1 + mark2 + mark3
# percentage = (total / 300) * 100

# print('Total marks:', total)
# print('Percentage:', percentage)

# if percentage > 60:
#     print('He/she is eligible for placement')
# else:
#     print('He/she is not eligible for placement')

#WAP to accept five different value in 5 different variable and check max value and print by using "simple if statement"
a = int(input('Enter value 1: '))
b = int(input('Enter value 2: '))
c = int(input('Enter value 3: '))
d = int(input('Enter value 4: '))
e = int(input('Enter value 5: '))

if a > b and a > c and a > d and a > e:
    print('Maximum value is:', a)

if b > a and b > c and b  > d and b > e:
    print('Maximum value is:', b)

if c > a and c > b and c > d and c > e:
    print('Maximum value is:', c)

if d > a and d > b and d > c and d > e:
    print('Maximum value is:', d)

if e > a and e > b and e > c and e > d:
    print('Maximum value is:', e)
