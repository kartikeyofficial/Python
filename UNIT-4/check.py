# file=open("rajput.txt","w+")
# file.write("Hello world")
# file.seek(0)
# data = file.read()
# print(data)
# file.close()
# a=0.1
# b=0.2
# c= a+b
# print(c)
# file=open("rajput.txt","w")
# l=["Aman\n","Harshit\n","Rohit\n","Aditya\n"]
# file.writelines(l)
# file.close()
# file=open("rajput.txt","r")
# print(file.read())
# file.close()
# def append_text(filename,text):
#     with open(filename,"a") as file:
#         file.write(text+"\n")
# def display_text(filename):
#     with open(filename,"r")as file:
#         file_content=file.read()
#     print(file_content)
# filename=("rajput.txt")
# text=("Kartikey is a good boy")
# append_text(filename,text)
# display_text(filename)


# def read_lastline(filename,n):
#     with open(filename,"r")as file:
#         lines=file.readlines()
#         last_n_lines= lines[-n:]
#         for i in last_n_lines:
#             print(i,end="")
# filename=("rajput.txt")
# n=3
# read_lastline(filename,n)
# def count(s):
#     for str in s.split():
#         s="&".join(str)
#     return s
# print(count("Kartikey"))
# def count_string(input_string):
#     digit=0
#     letters=0
#     for char in input_string:
#         if char.isdigit():
#             digit+=1
#         elif char in input_string:
#             letters +=1
#     return (letters,digit)
# def read_the_file(filename,letters,digit):
#     with open(filename,"w")as file:
#         file.write(f"letters are present{letters}\n")
#         file.write(f"digits are Present {digit}")
# input_string=("Kartikey is a Good Boy and 1223345678")
# filename=("rajput.txt")
# letters,digit=count_string(input_string)
# read_the_file(filename,letters,digit)
# def file_into_array(filename):
#     array=[]
#     with open(filename,"r")as file:
#         for line in file:
#             array.append(line.strip())
#         return array
# filename="rajput.txt"
# lines= file_into_array(filename)
# for line in lines:
#     print(line)

# def longest_word_in_the_file(filename):
#     with open(filename,"r")as file:
#         content=file.read()
#         word=content.split()
#         longest_word=max(word,key=len)
#     return longest_word
# filename=("rajput.txt")
# long=longest_word_in_the_file(filename)
# print(f"longest word in the file {filename} is {long}")
# def count_lines(filename):
#     with open(filename,"r")as file:
#         lines=file.readlines()
#     return len(lines)
# filename="rajput.txt"
# num_lines= count_lines(filename)
# print("The Number of lines in the file",num_lines)
# from collections import Counter
# def word_counter(fname):
#     with open(fname,"r")as file:
#         return Counter(file.read().split())
# print("Number of words in the file",word_counter("rajput.txt"))
# import random
# def random_lines(filename):
#     lines=open(filename).read().splitlines()
#     return random.choice(lines)
# print(random_lines("rajput.txt"))
# with open("rajput.txt","w")as file:
#     file.write("21\n")
#     file.write("8\n")
#     file.write("19\n")
#     file.write("10\n")
#     file.write("22\n")
#     file.write("23\n")
# file1=open("rajput.txt","r")
# for i in file1:
#     if i.strip:
#         num=int(i)
#         if num%2==0:
#             even1=open("even1.txt","a")
#             even1.write(str(num))
#             even1.write("\n")
#         else:
#             odd1=open("odd1.txt","a")
#             odd1.write(str(num))
#             odd1.write("\n")
# file.close()
# with open("rajput.txt","w")as file:
#     file.write("Your Name: John Doe\n")
#     file.write("Your Father's Name:\n")
# print("file rajput.txt created and names written.")
# with open("rajput.txt","r")as file:
#     content=file.read()
#     print("Content of rajput.txt")
#     print(content)
# with open("rajput.txt","r")as file:
#     line=file.readline()
#     print("First Read:",line)
#     file.seek(0)
#     line=file.readlines()
#     print("After Seek:",line)
# with open("rajput.txt","r+")as file:
#     file.write("This is The first Line:\n")
#     file.seek(20)
#     file.write("This is the new Line\n")
#     file.seek(0)
#     content=file.read()
#     print(content)
import random
test=[1,2,3,4,5,6]
random.shuffle(test)
print("The shuffled list:",test)