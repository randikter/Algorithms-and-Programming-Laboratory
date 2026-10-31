import math

#Computer arithmetic program
a = float(input("Enter the value of a = "))
b = float(input("Enter the value of b = "))
print("The sum of a and b is", a+b)
print("The difference between a and b is", a-b)
print("The product of a and b is", a*b)
print("The remainder when a is divided by b is", a%b)
print("The result of a divided by b is", a/b)
print(f"The result of log(a) is {math.log(a)}")
print("The result of a raised to the power of b is", a**b)

#Pythagoras calculation program
print("=== PYTHAGORAS CALCULATION PROGRAM ===")
a = float(input("Enter the length of the base side (a): "))
b = float(input("Enter the length of the height side (b): "))
c = math.sqrt(a**2 + b**2)
print("\nThe length of the hypotenuse (c) is:", c)

#Program for calculating cylinder dimensions
a = float(input("Enter the radius of the cylinder (r): "))
b = float(input("Enter the height of the cylinder (t): "))
print(f"\nThe volume of a cylinder is: {math.pi*a**2*b:.2f}")
print(f"The surface area of ​​a cylinder is: {2*math.pi*a*(a+b):.2f}")
