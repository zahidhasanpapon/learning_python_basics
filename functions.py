# crate a function

def sayHello(name):
    print(f'Hello {name}')

def sayHello2 (name = "Murchhana"):
    print(f"Hello {name}")


# Return values 

def getSum(num1, num2):
    total = num1+num2
    return total


num = getSum(3,4)

# lamda function

getSum = lambda num1 , num2 : num1 + num2

print(getSum(10,3))