import array
def read_file_to_array(filename):
    lines = array.array('u')
    with open(filename,"r") as file:
        for line in file:
            lines.append(line.strip())
    return lines

filename = 'karthik.txt'
lines = read_file_to_array(filename)
print(lines)
