operator=(input("Choose Operator: +,-,*,/ ="))
print(operator)
x=float(input("Enter the Number:"))
print(x)
y=float(input("Enter the Second Number:"))
print(y)
if (operator == '+') :
    result = x+y
    print(f"{x}+{y}= {result}")
elif (operator == '-'):
    result = x-y
    print(f"{x}-{y}={result}")
elif (operator == '*'):
    result = x*y
    print(f"{x}*{y}={result}")
elif (operator == '/'):
    result = x/y
    print(f"{x}/{y}={result}")
