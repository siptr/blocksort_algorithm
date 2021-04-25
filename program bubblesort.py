from random import randint
import time

def randomarray(len,max):
    array=[randint(0,max) for _ in range(len)]
    return array

start_time = time.time()

def bubblesort(A):
    swap = True
    while swap:
        swap = False
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swap = True
    return A

x=randomarray(10,10)
print(x)
bubblesort(x)
print(x)
print("N=10")

print("\n--- %s seconds ---" % (time.time() - start_time))