low=int(input("Enter the low range:"))
high=int(input("Enter The High Range:"))
for num in range(low,high+1):
    sum=0
    temp=num
    while temp>0:
        d=temp%10
        sum= sum+(d*d*d)
        temp=temp//10
        if num==sum:
            print(num)
