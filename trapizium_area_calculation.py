"""
3. Write a Python program to calculate the area of a trapezoid.
Note : A trapezoid is a quadrilateral with two sides parallel. The trapezoid is equivalent to the British definition of the trapezium. An isosceles trapezoid is a trapezoid in which the base angles are equal so.
Test Data:
Height : 5
Base, first value : 5
Base, second value : 6
Expected Output: Area is : 27.5
"""

h = int(input("the Height : "))
a = int(input("the Base, first value : "))
b = int(input("the Base, second value : "))
sum = a + b
dividing = sum / 2
result = dividing * h
print("Area is : ", result)