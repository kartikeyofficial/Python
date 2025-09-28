with open("karthik.txt","w")as file:
    file.write("18\n")
    file.write("24\n")
    file.write("13\n")
    file.write("12\n")
    file.write("9\n")
file1= open("karthik.txt","r")
for i in file1:
    if i.strip:
        num = int(i)
        if(num%2==0):
            even= open("even.txt","a")
            even.write(str(num))
            even.write("\n")
        else:
            odd= open("odd.txt","a")
            odd.write(str(num))
            odd.write("\n")
