def count_letters_and_digits(input_string):
    letter_count= 0
    digit_count= 0
    for char in input_string:
        if char.isalpha():
            letter_count +=1
        elif char.isdigit():
            digit_count +=1
    return letter_count, digit_count
def write_count_to_file(filename,letter_count,digit_count):
    with open(filename,'w')as file:
        file.write(f"Numbers Of Letters:{letter_count}\n")
        file.write(f"Numbers Of Digits:{digit_count}\n")
input_string= "karthik loves 1000 times"
filename= "karthik.txt"
letter_count, digit_count = (count_letters_and_digits(input_string))
write_count_to_file(filename,letter_count,digit_count)
