def add(num1,num2):
    return num1+num2
def substract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def devide(num1,num2):
    return num1/num2
print("Please Select the Operator:\n"
      "1. Add\n"
      "2. Substract\n"
      "3. Multiply\n"
      "4. Devide\n")

select = int(input("Select The Operations form 1,2,3,4: "))
number1= int(input("Enter The First Number: "))
number2=int(input("Enter The Second Number: "))
if select==1:
    print(number1,"+", number2,"=",add(number1,number2))
elif select==1:
    print(number1,"-", number2,"=",substract(number1,number2))
elif select==1:
    print(number1,"*", number2,"=",multiply(number1,number2))
elif select==1:
    print(number1,"/", number2,"=",devide(number1,number2))

else:
    print("Invalid Input")