import time
import matplotlib.pyplot as plt
import numpy as np
import sys
import random

sys.setrecursionlimit(20000)

start = time.time()

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



arr = random.sample(range(9000),9000)
print("puvodni pole: "+ str(arr))
insertionSort(arr)
lst = []

for i in range(len(arr)):
    lst.append(arr[i])
print("Sorted by insertion: " + str(lst))

end = time.time()
print(end - start)

start = time.time()

def insertionSortRecursive(arr, n):
    if n <= 1:
        return

    # Sort first n-1 elements
    insertionSortRecursive(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last



arr = random.sample(range(9000),9000)
print("puvodni pole: " + str(arr))
n = len(arr)
insertionSortRecursive(arr, n)
print("Sorted by recursive insertion: " + str(arr))
end = time.time()
print(end - start)

x = [1000, 4000, 7000, 9000]
y = [0.0187, 0.2919, 0.8992, 1.4728]
plt.plot(x, y)
plt.xlabel("počet iterací")
plt.ylabel("počet času")
plt.title("počet času")

x = [1000, 4000, 7000, 9000]
y = [0.0183, 0.2820, 0.8585, 1.4340]

coef = np.polyfit(x, y, 3)
poly1d_fn = np.poly1d(coef)
plt.plot(x, y, 'yo', x, poly1d_fn(x), '--k')
plt.show()