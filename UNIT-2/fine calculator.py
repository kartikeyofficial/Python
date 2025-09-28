print("You wanna be bunk of class")
print("go to Dean Sir Office ")
print("Class_Bunk(C)=200/day")
print("LABs(L)=400/day")
print("Seminar(S)=1000/day")
fine = 0
classes = input("You Bunk The Class(Y/N):")
days=int(input("Enter The Days You Are Not come in: "))

if(classes =='Y'):
    fine= (200 * days)
elif(classes=='N'):
    print=("No Problem")
else:
    print("Please Enter In Upper Case:")

LABs= input("You Bunk The LABs(Y/N):")
days=int(input("Enter The Days You Are Not come in: "))

if(LABs=='Y'):
    fine += (400 * days)
elif(LABs=='N'):
    print=("No Problem")
else:
    print("Please Enter In Upper Case:")

seminar= input("You Bunk The Seminar(Y/N):")
days=int(input("Enter The Days You Are Not come in: "))

if(seminar=='Y'):
    fine += (1000 * days)
elif(seminar=='N'):
    print=("No Problem")
else:
    print("Please Enter In Upper Case:")

print("Total fine of your bunk= ",fine)
print("DEAN ACADEMICS")