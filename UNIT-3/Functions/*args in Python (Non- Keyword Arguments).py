def sum(*args):
    resultfinal=0
    for num in args:
        resultfinal= resultfinal+num
    return resultfinal
print(sum(10,20,30))
print(sum(10,20,30,40))
print(sum(10,20,30,40,50))