import time
import matplotlib.pyplot as plt
import numpy as np
import random

start = time.time()
x = random.sample(range(90000),90000)

def chunk(my_list, size):
    return [my_list[i:i+size] for i in range(0,len(my_list), size)]
my_list = x
print(chunk(my_list, 2))



end = time.time()
print(end - start)

x = [10000,30000,50000,90000]
y = [0.0105,0.0242,0.0400,0.0667]
plt.plot(x,y)
plt.xlabel("počet iterací")
plt.ylabel("počet času")
plt.title("graf")
plt.show()

coef = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(coef)

plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')

plt.xlim(0, 100000)
plt.ylim(0, 0.1)
plt.show()