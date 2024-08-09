import random
num1 = int(input("Enter your number:"))
num2 = random.randrange(0,100)
print(num1)
print(num2)

if num1 > num2:
    print("your guess number is high")
elif num2 > num1:
    print("your guess number is low")

else:
    print("your guess number is equal")