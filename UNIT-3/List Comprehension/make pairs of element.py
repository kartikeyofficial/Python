def makepair(list1,list2):
    x=len(list1)
    y=len(list2)
    if x==y:
        pairlist=[(list1[i],list2[i]) for i in range(0,x)]
    return pairlist
print(makepair([1,2,3,4],[5,6,7,8]))
