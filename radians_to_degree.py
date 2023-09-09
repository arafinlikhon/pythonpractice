"""
2. Write a Python program to convert radians to degrees.
Test Data:
Radian : .52
Expected Result : 29.781818181818185
"""

#solve : 

radian = float(input("Enter the radian number: "))
degree_formula = 180 / 3.1416
degree = radian * degree_formula
print("The degree is:", degree)
