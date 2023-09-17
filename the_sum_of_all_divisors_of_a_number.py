"""
15. Write a Python program to return the sum of all divisors of a number.
Test Data:
If number = 8
If number = 12
Expected Output:
7
16
"""


number = int(input("enter the number : "))

num = 1

num_list = []

while num < number:
    if number % num == 0 :
        num_list.append(num)
    num += 1

result = sum(num_list)

print("sum of all divisors : ",result)
#SOLVED
