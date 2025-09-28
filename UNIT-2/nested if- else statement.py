a=int(input("Enter The Value Of a:"))
b=int(input("Enter The Value Of b:"))
c=int(input("Enter The Value Of c:"))
if(a>b):
    if(a>c):
        print(a,"Is the Largest Number")
    else:
        print(c,"Is the Largest Number")
else:
    if(b>c):
        print(b,"Is the Largest Number")
    else:
        print(c,"Is the Largest Number")