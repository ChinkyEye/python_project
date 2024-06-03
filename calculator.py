num1 = int(input("Enter value 1: "))
num2 = int(input("Enter value 2: "))
oper = input("Enter the oper: ")
if oper=="+":
    print(num1 + num2)
elif oper=="-":
    print(num1-num2)
elif oper=="*":
    print(num1*num2)
elif oper=="/":
    print(num1/num2)

else:
    print("invalid operation")