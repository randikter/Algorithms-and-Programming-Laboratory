#The program displays address data and other information.
print("Enter your data accordingly!")
a = input("Enter your full name: ")
b = input("Enter address/residence address: ")
c = input("Enter the name of the campus : ")
d = input("Enter your major: ")
e = input("Where is the campus building for your major (e.g., A) located?: ")
print("\nHere is your data!")
print(f"\nHello, my name is {a}. I live in {b}, and I am a student at {c}, \nmajoring in {d}. I attend classes in building {e}, \nand I am ready to participate in the algorithms laboratory session.")

#Room area calculation program
print("Calculate Room Area")
a = float(input("Enter Room Length: "))
b = float(input("Enter Room Width: "))
c = input("Enter Unit (Meters/Inches): ")
print(f"The area of ​​a room with length {a} and width {b} is {a*b} {c}")

#Body Mass Index (BMI) calculation program
print("Calculate Body Mass Index (BMI)")
a = input("Enter your name: ")
b = float(input("Enter your height (cm): "))
b = b/100
c = float(input("Enter your weight (kg): "))
print (f"{a} Your BMI score is {c/(b**2):.1f}")
