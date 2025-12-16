def read_file_to_list(filename):
    lines= []
    with open(filename,"r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            lines.append(line.strip()) # strip function is used for remove the \n from the list
    return lines
filename = "karthik.txt"
a = read_file_to_list(filename)
print(a)