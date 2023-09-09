def calculate_factorial(n):
    if n < 0:
        return None
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial

l = int(input())
i = 1
while i <= l:
    result = calculate_factorial(i)
    print("Factorial of " + str(i) + ": " + str(result))
    i += 1