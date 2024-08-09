import module

def simplefunction():
    print("Welcome to Function topic")


def sum_data(a,b):
    print(a+b)


def mul_data(a,b): #return statement is used in order to apply conditions
   c = a*b
   return c

mul_val = mul_data(5,10)
print(mul_val)
sum_data(10,20)
simplefunction()

print(module.add(45,0.5))