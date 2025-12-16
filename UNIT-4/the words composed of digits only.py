def create_input_file(filename):
    user_input= input("Enter A Sequence of Words Separated by whitespace: ")
    with open(filename,"w") as file:
        file.write(user_input)
def find_digit_words(filename):
    with open(filename,"r") as file:
        content = file.read()
        words = content.split()
        digit_words= [word for word in words if word.isdigit()]
        print("words Composed of Digits only:")
        for word in digit_words:
            print(word)
filename="karthik.txt"
create_input_file(filename)
find_digit_words(filename)
