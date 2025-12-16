file= open("karthik.txt","r")
file_content= ""
for line in file:
    file_content += line
file.close()
print(file_content)
print(type(file_content))

