"""
13. Write a Python program to find out if the given number is abundant.
Note: In number theory, an abundant number or excessive number is a number for which the sum of its proper divisors is
greater than the number itself. The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a
total of 16.

Test Data:
If is_abundant(12)
If is_abundant(13)
Expected Output:
True
False
"""

number = int(input("Please enter the number: "))
num = 1  # Start with 1 as the first divisor
divisors = []

while num < number:
    if number % num == 0:
        divisors.append(num)
    num += 1

total = sum(divisors)

if total > number:
    print(True)
else:
    print(False)
