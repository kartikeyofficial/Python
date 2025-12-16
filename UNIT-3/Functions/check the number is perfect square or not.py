import math
def count_sqrt(N):
    if N<1:
        return 0
    largest_number= int(math.sqrt(N))
    return largest_number
N=55
print("Count the Perfect Square Less Than or Equal to: ",count_sqrt(N))