"""
4. Write a Python program to calculate the area of a parallelogram.
Note : A parallelogram is a quadrilateral with opposite sides parallel (and therefore opposite angles equal). A quadrilateral with equal sides is called a rhombus, and a parallelogram whose angles are all right angles is called a rectangle.
Test Data:
Length of base : 5
Height of parallelogram : 6
Expected Output: Area is : 30.0
"""
base = int(input("Length of base : "))
Height = int(input("Height of parallelogram : "))

result = base * Height
print("Area is : ", result)