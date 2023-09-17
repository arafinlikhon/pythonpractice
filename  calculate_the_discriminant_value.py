"""
9. Write a Python program to calculate the discriminant value.
Note: The discriminant is the name given to the expression that appears under the square root (radical) sign in the quadratic formula.
Test Data:
The x value : 4
The y value : 0
The z value : -4
Expected Output:
Two Solutions. Discriminant value is : 64.0
"""

#b2 – 4ac

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

def Discriminant(a,b,c):
    return (b*2) - (4 * a * c)
result = float(Discriminant(a,b,c))

print("Discriminant value is : ", result)

#solved