def ret_smaller(l):
    if not l:
        return[]
    smallest_list=l[0]
    for sublist in l[1:]:
        if len(sublist)< len(smallest_list):
            smallest_list=sublist
    return smallest_list
nested_list=[[10,20,30,40],[10,20,30],[10,20],[10]]
print(ret_smaller(nested_list))