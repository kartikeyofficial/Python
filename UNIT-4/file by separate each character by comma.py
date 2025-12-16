def separate_character_by_comma(file_name):
    with open(file_name,"r")as file:
        content = file.read()
    separate_content = ",".join(content)
    with open(file_name,"w") as file:
        file.write(separate_content)
file_name = "karthik.txt"
separate_character_by_comma(file_name)