number = int(input("enter the numer : "))

prime = True
num = 2
while number % num != 0 and num <= number:
    prime = False
    num += 1

if prime == False:
    print("number is not prime ")
elif prime == True:
    print("number is prime ")