import numpy as np
arr=np.array([12,374,56,6,78,34,89])
n= len(arr)
print("Lenght is:",n)
m1= min(arr)
m2= max(arr)
print("Minimum is:",m1)
print("Max is:",m2)
for i in range(len(arr)):
    print(arr[i])