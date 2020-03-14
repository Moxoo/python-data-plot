import numpy as np
import math

data = np.loadtxt('queuesize')
queue = data[0:, 1]
queue.sort()
a = len(queue)
b = math.floor(a*0.99)
print(a)
print(b)
print(queue[b])