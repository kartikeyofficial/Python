file= open("karthik.txt","w")
l= ["\nThis is Delhi \n","This Is India\n","I am here Greater Noida\n"]
s= "Hello World"
print(file.write(s))
print(file.writelines(l))
file.close()

file= open("karthik.txt","r")
print(file.read())
file.close()