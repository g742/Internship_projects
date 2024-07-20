
print("  ============ (Basic Calculator) =============")
a = int(input("Enter the first value: "))
n = input("Enter the operator(+ , - , /, *): ")
b = int(input("Enter the second value: "))
if n == "+":
    c = int(a + b)
    print("Sum of the given number is:",c)
elif n == "-":
    c = int(a - b)
    print("Substraction of the given number is:",c)
elif n == "*":
    c = int(a * b)
    print("Multiplication of the given number is:",c)
elif n == "/":
    c = int(a / b)
    print("Division of the given number is:",c)
else:
    print("Invalid operator")

