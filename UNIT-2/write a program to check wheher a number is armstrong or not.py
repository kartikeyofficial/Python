n= int(input("Enter The Number:"))
num= n
sum= 0
while(n>0):
    d= n%10
    sum = sum+(d*d*d)
    n=n//10
if(sum==num):
    print(num,"Is an Armstrong Number")
else:
    print(num,"Is not an Armstrong Number")
