#A function program for calculating the average of values ​​according to letter categories
a = 0.0
b = 0
c = input("Enter a value: ")
while c in ["A","A-","B+","B","B-","C+","C","C-","D","E"]:
    if c == "A":
        d = 4
    elif c == "A-":
        d = 3.75
    elif c == "B+":
        d = 3.5
    elif c == "B":
        d = 3
    elif c == "B-":
        d = 2.75
    elif c == "C+":
        d = 2.5
    elif c == "C":
        d = 2
    elif c == "C-":
        d = 1.75
    elif c == "D":
        d = 1.5
    elif c == "E":
        d = 1.25
    print("value:", d)
    a += d
    b += 1
    c = input("Enter a value: ")
print("the average is: ", a/b)

#A program to calculate zoo admission tickets based on age, including payment processing
a = 0.0
b = input("Enter age: ")
while b != "":
    b = int(b)
    if b < 3:
        c = 0.00
    elif b >= 3 and b <= 12:
        c = 14.00
    elif b >= 65:
        c = 18.00
    else:
        c = 23.00
    if c < 1:
        print("Free")
    else:
        print(f"Price $ {c:.2f}")
    print(f"Running total: {a + c:.2f}")
    a += c
    b = (input("Enter age: "))
d = float(input("Enter the amount of money: "))
print(f"Running Change: {d - a:.2f}")

#Student class grade summary program
a = int(input("Enter the number of students: "))
b = 1
c = 0.0
d = []
e = []
f = 0
while b <= a:
    print("\nStudent no.", b)
    g = input("  Name: ")
    h = float(input("  Value " + g +"(0-100): "))
    d.append(g)
    e.append(h)
    if h >= 60:
        i = "PASSED"
        f += 1
    else:
        i = "NOT PASS"
    print(f"{g}: value {h} | {i}")
    c += h
    b += 1
    idx_max = e.index(max(e))
    idx_min = e.index(min(e))
print("\n===== CLASS GRADE SUMMARY =====")
print(f"Number of students : {a}")
print(f"Class average      : {c/a:.2f}")
print(f"The highest score  : {max(e)} ({d[idx_max]})")
print(f"Lowest value       : {min(e)} ({d[idx_min]})")
print(f"Number of passes   : {f} dari {a}")
