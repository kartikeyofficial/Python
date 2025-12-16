a=int(input("Enter The Angle:"))
b=int(input("Enter The Angle:"))
c=int(input("Enter The Angle:"))
if ( a>0 and b>0 and c>0):
    print("Valid")
    if(a==b and b==c and c==a):
        print("Euilateral Triangle")
    elif (a==b or b==c or c==a):
        print("Isosceles Triangle")
    elif(a==90 or b==90 or c==90):
        print("Right Angle Triangle")
    else:
        print("Invalid Input")