def append_text_to_file(file_name,text):
    with open(file_name,"a") as file:
        file.write(text + "\n")
def display_file_content(file_name):
    with open(file_name,"r") as file:
        file_content = file.read()
    print(file_content)
file_name="karthik.txt"
text_to_append= input("Enter The Line:")
append_text_to_file(file_name, text_to_append)
display_file_content(file_name)