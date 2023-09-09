"""
8. Write a Python program to calculate the area of the sector.
Note: A circular sector or circle sector, is the portion of a disk enclosed by two radii and an arc, where the smaller area is known as the minor sector and the larger being the major sector.
Test Data:
Radius of a circle : 4
Angle measure : 45
Expected Output:
Sector Area: 6.285714285714286
"""

check = True


x = int(input("If the angle measure is in radians, type 1; if it's in degrees, type 0: "))


if x == 0:
    check = False  # degrees

angle_measure = float(input("Please enter the angle measure: "))
radius = float(input("Radius: "))


def area_in_radians(angle, r):
    return 0.5 * angle * r**2

def area_in_degrees(angle, r):
    return (angle / 360) * 3.1416 * r**2

if check:
    result = area_in_radians(angle_measure, radius)
    print("Sector Area: ",result)
else:
    result = area_in_degrees(angle_measure, radius)
    print("Sector Area: ",result)
