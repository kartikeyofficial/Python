a=int(input("Enter The First Number:"))
b=int(input("Enter The First Number:"))
c=int(input("Enter The First Number:"))
if(a>b):
    if(a>c):
        print(a,"is The Largest Number")
    else:
        print(c,"is the Largest Number")
else:
    if(b>c):
        print(b,"is the Largest Number")
    else:
        print(c,"is The Largest Number")