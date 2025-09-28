with open ("karthik.txt","r") as file:
    line= file.readlines()
    print("first Read:",line)
    file.seek(0)
    line = file.readlines()
    print("After Seek:", line)