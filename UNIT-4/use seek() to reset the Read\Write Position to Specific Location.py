with open("karthik.txt",'r+' ) as file:
    file.write("This is The First Line.\n")
    file.write("This Is The Second Line.\n")
    file.seek(20)
    file.write("This Is the New Second Line.\n")
    file.seek(0)
    content = file.read()
    print(content)