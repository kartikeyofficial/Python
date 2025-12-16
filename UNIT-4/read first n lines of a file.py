def read_first_n_lines(file_name,n):
    with open(file_name,"r") as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line,end="")
file_name ="karthik.txt"
n= int(input("Enter The Lines n:"))
read_first_n_lines(file_name,n)
