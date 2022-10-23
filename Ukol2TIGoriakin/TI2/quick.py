import time
import matplotlib.pyplot as plt
import numpy as np
import copy
import random


start = time.time()
x = random.sample(range(9000),9000)

def quick(y):
    # kontrola pro ukonceni rekurzivniho volani
    if len(y) <=1:
        return y
    x = copy.copy(y)

    # vyber 'prostredniho' prvku pole
    # priprava poli A, B, C
    pivot = int(len(x)/2)
    A = []
    B = [x[pivot]]
    C = []

    # pruchod vsech prvku v poli x
    for i in range(len(x)):
        # pokud se jedna o uz jednou zpracovany prvek, preskakuji
        if i == pivot:
            continue
        # presun prvku do spravneho pole
        if x[i] < x[pivot]:
            A.append(x[i])
        else:
            C.append(x[i])

    # rekurzivni volani funkce
    A = quick(A)
    C = quick(C)

    # vraceni spojenych setridenych poli
    return A+B+C

print("puvodni pole: " + str(x))
print("setridene pole pomoci QuickSort: " + str(quick(x)))

end = time.time()

print(end - start)

start = time.time()
def partition(lst, start, end):
    pos = start


    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos]

    return pos

def quick_sort_recursive(lst, start, end):
    if start < end:
        pos = partition(lst, start, end)
        quick_sort_recursive(lst, start, pos - 1)
        quick_sort_recursive(lst, pos + 1, end)

example = random.sample(range(9000),9000)
print("puvodni pole: " + str(example))
quick_sort_recursive(example, 0, len(example) - 1)
print("setridene pole pomoci QuickSort: " + str(example))

end = time.time()

print(end - start)


x = [1000, 4000, 7000, 9000]
y = [0.0017, 0.0081, 0.0132, 0.0197]
plt.plot(x, y)
plt.xlabel("počet iterací")
plt.ylabel("počet času")
plt.title("počet času")

x = [1000, 4000, 7000, 9000]
y = [0.0012, 0.0056, 0.0115, 0.0141]

coef = np.polyfit(x, y, 3)
poly1d_fn = np.poly1d(coef)
plt.plot(x, y, 'yo', x, poly1d_fn(x), '--k')
plt.show()