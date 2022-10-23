import time
import matplotlib.pyplot as plt
import numpy as np
import copy
import random

start = time.time()
x = random.sample(range(18000),18000)

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

# test quicksort
# puvodni nesetridene pole
print("puvodni pole: " + str(x))
# setrideny vysledek
print("setridene pole pomoci QuickSort: " + str(quick(x)))

end = time.time()
print(end - start)

x = [5000,8000,13000,18000]
y = [0.0143,0.0238,0.0489,0.0649]
plt.plot(x,y)
plt.xlabel("počet iterací")
plt.ylabel("počet času")
plt.title("graf")
plt.show()

coef = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(coef)

plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')

plt.xlim(0, 19000)
plt.ylim(0, 0.1)
plt.show()