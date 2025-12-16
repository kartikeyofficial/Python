import numpy as np
arr1= np.zeros((10))
arr2=np.arange((10))
arr3=np.linspace(0,20,10)
n= len(arr1)
print("Length is:",n)
for i in range(len(arr1)):
    print(arr1[i],end=" ")
print()
n= len(arr2)
print("Length is:",n)
for i in range(len(arr2)):
    print(arr2[i],end=" ")
print()
n= len(arr3)
print("Lenght is:",n)
for i in range(len(arr3)):
    print(arr3[i])