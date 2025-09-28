def count_lines(filename):
    with open(filename,"r") as file:
        lines = file.readlines()
    return len(lines)
filename = "karthik.txt"
num_lines= count_lines(filename)
print(f"The number Of lines in the File:",num_lines)