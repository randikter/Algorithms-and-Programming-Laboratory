#Expenditure program for
for a in range(7,0,-1):
    for b in range(a):
        print(a, end="")
    print()

#Program to determine the month using a while loop
a = int(input("Enter the month number (1-12): "))
b = int(input("Enter the year: "))
while a < 1 or a > 12:
    print("Invalid month!")
    a = int(input("Enter the month number (1-12): "))
if a == 2:
    if (b%400==0) or (b%4==0 and b%100!=0):
        c = 29
    else:
        c = 28
elif a == 4 or a == 6 or a == 9 or a == 11:
    c = 30
else:
    c = 31
print("The number of days in month", a, "year", b, "is", c)
