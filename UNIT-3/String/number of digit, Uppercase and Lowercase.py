def string_test(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0,"DIGIT":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] +=1
        elif c.islower(): 
            d["LOWER_CASE"] +=1
        elif c in range(0,20):
            d["DIGIT"] +=1
        else:
            pass
    print("Original String: ",s)
    print("No. of Upper Case Characters: ",d["UPPER_CASE"])
    print("No. Of Lower Case Characters: ",d["Lower_Case"])
    print("No. of Digits: ",d["DIGIT"])
string_test("Kartikey Is A Good Boy")    

