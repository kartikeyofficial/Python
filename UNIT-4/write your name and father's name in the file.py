with open("p.txt","w") as file:
    file.write("Your Name: Kumar Kartikey\n")
    file.write("Father's Name: Sanjeev Kumar\n")
print("File p.txt created and Names Written.")
with open("p.txt","r") as file:
    contents = file.read()
    print("content of p.txt:")
    print(contents)