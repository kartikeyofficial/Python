l=[1,2,3,4,5,6,7,8,9]
result= l[::-1][:-1]
print(result)
slice1= l[-1:-3:-1]
print(slice1)
result2=l[2:-1]
print(result2)
result3=l[0::2]
print(result3) 
middle_index= len(l)//2
result4=l[middle_index:]
print(result4)
result5=l[:middle_index+1][::-1]+l[middle_index+1:]
print(result5)
result6=[x%2 for x in l]
print(result6) 
