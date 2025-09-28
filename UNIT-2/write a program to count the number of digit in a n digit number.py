num= int(input("Enter The Number:"))
count = 0
while(num>0):
    num= num//10
    count = count+1
    print("Number of digit:",count)