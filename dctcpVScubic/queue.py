import matplotlib.pyplot as plt
import numpy as np
print("plot")

data1 = np.loadtxt('queue_size_dctcp.plotme')
data2 = np.loadtxt('queue_size_cubic.plotme')

plt.figure(dpi=400)
plt.plot(data1[0:400, 0], data1[0:400, 1]*1.028, color='black', label="DCTCP", linewidth=1)
plt.plot(data2[0:400, 0], data2[0:400, 1]*1.028, '--', color='r', label="CUBIC-RED", linewidth=1)

plt.legend()
plt.title('Queue Length')
plt.xlabel('Time (S)')
plt.ylabel('Inst. Queue Len(KB)')
#x_ticks = np.arange(0, 1)
#plt.xticks(x_ticks)
y_ticks = np.arange(0, 301, 50)
plt.yticks(y_ticks)

plt.show()