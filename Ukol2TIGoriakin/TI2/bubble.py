import time
import copy
import random
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(20000)

arr = random.sample(range(9000), 9000)
start = time.time()


def bubble_sort(y):
    x = copy.copy(y)
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x


print("Původní pole: " + str(arr))
print("Sorted by Bubble sort: " + str(bubble_sort(arr)))
end = time.time()

print(end - start)

#Recursive

arrRecur = random.sample(range(9000), 9000)
start = time.time()


def recursive_bubble_sort(list_data: list, length: int = 0) -> list:
    length = length or len(list_data)
    swapped = False
    for i in range(length - 1):
        if list_data[i] > list_data[i + 1]:
            list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
            swapped = True

    return list_data if not swapped else recursive_bubble_sort(list_data, length - 1)

print("Původní pole: " + str(arrRecur))
print("Sorted by recursive Bubble Sort: ", recursive_bubble_sort(arrRecur))
end = time.time()

print(end - start)



x = [1000, 4000, 7000, 9000]
y = [0.0281, 0.4467, 1.3256, 2.2341]
plt.plot(x, y)
plt.xlabel("počet iterací")
plt.ylabel("počet času")
plt.title("Graf")

x = [1000, 4000, 7000, 9000]
y = [0.0379, 0.6418, 1.9780, 3.2774]

coef = np.polyfit(x, y, 3)
poly1d_fn = np.poly1d(coef)
plt.plot(x, y, 'yo', x, poly1d_fn(x), '--k')
plt.show()