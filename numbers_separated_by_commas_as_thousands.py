"""
26. Write a Python program to display numbers separated by commas as thousands.

"""
number = int(input("enter the number : "))

if number >= 1000:
    result = str(number)
    result[-4] = ","
    print(result)