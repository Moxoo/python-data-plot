import numpy as np

data = np.loadtxt('fairness')
data1 = data[0:, 0]
data2 = data[0:, 1]

a = 0
for i in data1:
    a = a + i
a = a * a
#print(a)

b = 0
for j in data1:
    b = b + j * j

c = a/(len(data1)*b)

print('fairness of front: ', c)

a1 = 0
for p in data2:
    a1 = a1 + p
a1 = a1 * a1
#print(a1)

b1 = 0
for q in data2:
    b1 = b1 + q * q

c1 = a1/(len(data2)*b1)

print('fairness of tail: ', c1)