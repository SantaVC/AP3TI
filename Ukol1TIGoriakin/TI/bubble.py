import time
import matplotlib.pyplot as plt
import numpy as np
import copy
import random

start = time.time()
x = random.sample(range(9000),9000)

def bubble(y):
    # shallow copy -- jinak se promenna predava jen jako reference
    # a tim bych vstupni pole mel setridene pro, ale ja jej chci vyuzit
    # i v dalsich tridicich algoritmech
    x = copy.copy(y)
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x

print("puvodni pole: " + str(x))
# setrideny vysledek
print("setridene pole pomoci BubbleSort: " + str(bubble(x)))
# pro kontrolu, x je stale nesetridene
# kdybych zakomentoval radek v bubble() 'x = copy.copy(y)', tak bude x setridene
print("Kontrola, puvodni pole je stale nesetridene: " + str(x))

end = time.time()
print(end - start)

x = [1000,3000,5000,9000]
y = [0.0468,0.3967,1.1084,3.6507]
plt.plot(x,y)
plt.xlabel("počet iterací")
plt.ylabel("počet času")
plt.title("graf")
plt.show()

coef = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(coef)

plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')

plt.xlim(0, 10000)
plt.ylim(0, 4)
plt.show()