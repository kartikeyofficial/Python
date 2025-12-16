n=int(input("Enter the Term of Fabonacci Series:"))
first=0
second=1
print("Fibonacci Series:")
print(first,end=",")
for i in range(0,n-1):
    next= first + second
    print(next,end=",")
    first= second
    second= next