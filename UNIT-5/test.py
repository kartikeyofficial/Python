# def f1():
#     print("This Function is in my library")
#     print("Function name is f1")
# def f2(string):
#     lst=string.split()
#     return lst
# import numpy as np
# arr1=np.array([1,2,3,4,5,6,7])
# print(arr1)
# arr2=np.zeros((3,3))
# print(arr2)
# arr3=np.arange(10)
# print(arr3)
# arr4=np.linspace(0,100,10)
# print(arr4)
# total=np.sum(arr1)
# print(total)

# sort=np.sort(arr1)
# print(sort)
# unique=np.unique(arr1)
# print(unique)
# import numpy as np
# arr=np.array([12,14,15,13,19,17])
# n=len(arr)
# print(n)
# m1=min(arr)
# m2=max(arr)
# print("Minimum Number",m1)
# print("Maximum Value",m2)
# for i in range(len(arr)):
#     print(arr[i])
# import numpy as np
# arr1=np.zeros((10))
# arr2=np.arange((10))
# arr3=np.arange(0,100,10)
# n=len(arr1)
# print("Length of the array:",n)
# for i in range(len(arr1)):
#     print(arr1[i],end=",")

# n=len(arr2)
# print("Length of the arr2:",n)
# for i in range(len(arr2)):
#     print(arr2[i],end=",")
# import numpy as np
# arr1=np.array([45,12,34,67,56,61,31])
# sorting=np.sort(arr1)
# print(sorting)
# import numpy as np
# arr= np.array(
#     [
#         [33,34,35,36],
#         [44,45,46,47],
#         [55,56,57,58]
#     ]
# )
# for i in range(3):
#     for j in range(4):
#         print(arr[i][j],end=" ")
# import numpy as np
# arr=np.array([10,20,30,40,50,60,70,80,90,12,34,47])
# arr1=np.sqrt(arr)
# print(arr1)
# arr2=np.log(arr)
# print(arr2)
import tkinter as tk
w=tk.Tk()
l1=tk.Label(text="Enter The First Name:")
l2=tk.Label(text="Enter The Middle Name:")
l3=tk.Label(text="Enter The Last Name:")
t1=tk.Entry(width=40)
t2=tk.Entry(width=40)
t3=tk.Entry(width=40)
l1.grid(row=0,column=0,padx=10,pady=10)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0,padx=10,pady=10)
t2.grid(row=1,column=1)
l3.grid(row=2,column=0,padx=10,pady=10)
t3.grid(row=2,column=1)
w.minsize(500,400)
w.mainloop()
