# a=int(input("Enter the first Number:"))
# b=int(input("Enter the Second Number:"))
# print("Value of a:",a)
# print("Value of b:",b)
# c=a
# a=b
# b=c
# print("After The Swapping Value of a:",a)
# print("After The Swapping Value of b:",b)
# a=int(input("Enter the first Number:"))
# b=int(input("Enter the Second Number:"))
# print("Value of a:",a)
# print("Value of b:",b)
# a=a+b
# b=a-b
# a=a-b
# print("After The Swapping Value of a:",a)
# print("After The Swapping Value of b:",b)

# n=5
# for i in range(n): 
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# n=5 
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
# 
# n=4
# for i in range(n-1):
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
# import numpy as np
# arr=np.array([
#     [10,20,30,40],
#     [40,50,38,47],
#     [12,34,56,78]
# ])
# for i in range(3):
#     for j in range(4):
#         print(arr[i][j],end=' ')
#     print()
n=5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for i in range(i,n):
        print("*",end=" ")
    print()