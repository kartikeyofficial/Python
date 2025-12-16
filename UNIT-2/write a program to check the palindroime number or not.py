n= int(input("Enter The Number:"))
num=n
rev=0
while(n>0):
    d=n%10
    rev= (rev*10+d)
    n=n//10
if(rev==num):
        print(num,"This Number Is Palindrome Number")
else:
        print(num,"This Number Is not a Palindrome Number")