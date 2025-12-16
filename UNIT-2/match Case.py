print("Enter 1-Monday,2-Tuesday,3-Wednesday,$-Thursday,5-Friday,6-Saturday,7-sunday")
x=input("Enter The Day Number:")
match x:
    case"1":
        print("Monday")
    case"2":
        print("Tuesday")
    case"3":
        print("Wednesday")
    case"4":
        print("Thursday")
    case"5":
        print("Friday")
    case"6":
        print("Saturday")
    case"7":
        print("Sunday")
    case _:
        print("Ivalid Input")