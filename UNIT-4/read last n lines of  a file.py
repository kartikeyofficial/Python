def read_last_n_lines(file_name, n):
    with open(file_name,"r")as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]
        for line in last_n_lines:
            print(line, end="")
file_name = "karthik.txt"
n = int(input("Enter The Number of from Last Line:"))
read_last_n_lines(file_name,n)