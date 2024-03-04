
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def modulo(x, y):
    return x % y


while True:
    print("Steven's Calculator")
    print("")
    print("Enter First Digit: ")
    num1 = int(input())
    print("Enter Operator: ")
    print("[1] +")
    print("[2] -")
    print("[3] *")
    print("[4] /")
    print("[5] %")
    operator = int(input())
    print("Enter Second Digit: ")
    num2 = int(input())

    if operator == 1:
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
        print("")
    elif operator == 2:
        result = sub(num1, num2)
        print(f"{num1} - {num2} = {result}")
        print("")
    elif operator == 3:
        result = mul(num1, num2)
        print(f"{num1} * {num2} = {result}")
        print("")
    elif operator == 4:
        result = div(num1, num2)
        print(f"{num1} / {num2} = {result}")
        print("")
    elif operator == 5:
        result = modulo(num1, num2)
        print(f"{num1} % {num2} = {result}")
        print("")
    else:
        print("Invalid Input please try again.")