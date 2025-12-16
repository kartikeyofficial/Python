x=int(input("Enter The Year:"))
if (x%400==0):
    print(x,"is a Leap Year")
elif(x%100==0):
    print(x,"is Not a Leap Year")
elif(x%4==0):
    print(x,"is a Leap Year")
else:
    print(x,"is Not a Leap Year")