print("Welcome to Pizza Services")
print("Choose The Pizza Size= S,M,L=")
print("Small Pizza=15$")
print("Medium Pizza= 20$")
print("Large Pizza= 25$")
size=input("Enter The Size= ")
bill=0
if(size=='S'):
    bill= 15
elif(size=='M'):
    bill= 20
elif(size=='L'):
    bill= 25
else:
    {
        print("Please Enter In Upper Case:")
    }
print("You Want Pepparani:")
pepprani= input("'Y'or'N':")
if(pepprani=='Y'):
        if(size=='s'):
             bill+=2
        else:
             bill+=3
else:
     {
          print("You Not Want Pepprani")
     }
print("You Want Extra Cheese:")
cheese= input("'Y'or'N':")
if(cheese=='Y'):
     bill+=1
else:
     {
          print("You Not Want To be Cheese:")
     }
print("Total Bill Of Pizza= $",bill)
        
    


    