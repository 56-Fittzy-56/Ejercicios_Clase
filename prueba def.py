def sum(num1, num2):
    return num1 + num2
def minus(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
a = int(input("ingrese numero: "))
b = int(input("ingrese numero: "))
operation = input("ingrese operacion: ")

Total=0
has_error = False
if operation == "+":
    Total=sum(a, b)
elif operation == "-":
    Total=minus(a, b)
elif operation == "*":
    Total=multiply(a, b)
elif operation == "/":
    Total=divide(a, b)
else:
    has_error = True
    print("operacion no valida")
if not has_error:
    print(Total)


