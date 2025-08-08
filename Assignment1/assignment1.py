num1 = int(input("Enter the first number: "))
num2 = int(input ("Enter the second number: "))

operator = input("Enter the operator(i.e. + or - or * or /): ")

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")