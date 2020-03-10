import matplotlib.pyplot as plt
import numpy as np
print("plot")

data1 = np.loadtxt('queue_size/queue_size_tail_n=20.plotme')
data2 = np.loadtxt('queue_size/queue_size_front_n=20.plotme')

plt.figure(dpi=400)
plt.plot(data1[0:, 0], data1[0:, 1], color='black', label="tail mark", linewidth=0.5)
plt.plot(data2[0:, 0], data2[0:, 1], color='r', label="front mark", linewidth=0.5)

plt.legend()
plt.title('Queue Length')
plt.xlabel('Time (S)')
plt.ylabel('Inst. Queue Len(Pkts)')
#x_ticks = np.arange(0, 1)
#plt.xticks(x_ticks)
y_ticks = np.arange(0, 201, 50)
plt.yticks(y_ticks)

plt.show()