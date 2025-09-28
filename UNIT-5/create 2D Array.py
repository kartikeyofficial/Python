import numpy as np
arr=np.array(
    [
        [34,56,23,78]
        [23,45,67,85]
        [12,23,34,45]
    ]
)
for i in range(2):
    for j in range(3):
        print(arr[i][j],end=" ")
    print()