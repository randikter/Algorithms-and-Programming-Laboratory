#Program to determine the type of triangle
a = float(input("Enter the side length A: "))
b = float(input("Enter the side length B: "))
c = float(input("Enter the side length C: "))
if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or c == a:
    print("Isosceles triangle")
elif a + b <= c or b + c <= a or c + a <= b:
    print("Not a triangle")
else:
    print("Scalene triangle")

#Value-based categorization program
a = float(input("Enter a numerical value: "))
if a > 100 or a < 0:
    b = ("Invalid value (must be in the range 0–100)")
elif a == 100:
    b = ("S")
elif a >= 90:
    b = ("A")
elif a >= 80:
    b = ("B")
elif a >= 70:
    b = ("C")
elif a >= 60:
    b = ("D")
else:
    b = ("E")
print("Letter Grade:", b)

#Discount program with coupons
print("---USAKTIF Shopping Discount Calculation Program---")
a = input("\nEnter Name : ")
b = str(input("Enter Student ID Number : "))
c = float(input("Enter Your Total Purchase Amount : "))
d = input("Pay using a coupon? y/n : ").lower()
f = 0
if d in ("y", "yes"):
    e = input("Enter coupon code : ")
    if e == "IKL6309":
        f = 100
    else:
        print("!-Sorry, the code you used is incorrect or has expired.-!")
        raise SystemExit
elif d in ("n", "no"):
    if c >= 390000:
        f = 80
    elif c >= 190000:
        f = 60
    elif c >= 90000:
        f = 40
    elif c >= 40000:
        f = 20
    elif c < 0:
        print("!-Enter the total purchase amount correctly-!")
        raise SystemExit
    else:
        f = 0
else:
    print("!-Enter your selection correctly-!")
    raise SystemExit
if f == 100:
    g = ("TOTALLY FREE")
else:
    g = f"Rp.{c - (c * (f / 100)):.0f}"
if f > 0:
    print(f"\n--CONGRATULATIONS, YOU HAVE RECEIVED A DISCOUNT {f}%--")
else:
    print("\n--YOU DO NOT RECEIVE A DISCOUNT--")
print("\n------------Shopping Details------------")
print(f"{a} - {b}")
print(f"Your total purchase     : Rp.{c}")
print(f"Discounts               : Rp.{c * (f / 100):.0f}")
print(f"Total payment           : {g}")
print("\nThank you for shopping :)")
