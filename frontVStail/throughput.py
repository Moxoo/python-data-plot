import matplotlib.pyplot as plt
import numpy as np
print("plot")

data1 = np.loadtxt('throughput_tail/throughput_20.plotme')
data2 = np.loadtxt('throughput_front/throughput_20.plotme')

plt.figure(dpi=400)
plt.plot(data1[0:200, 0], data1[0:200, 1]/1000, color='sienna', label="tail mark", linewidth=1)
plt.plot(data2[0:200, 0], data2[0:200, 1]/1000, color='violet', label="front mark", linewidth=1)
plt.legend()
plt.title('Throughput Front vs Tail, N=20')
plt.xlabel('Time (S)')
plt.ylabel('Throughput (Gbps)')
#x_ticks = np.arange(0, 0.05)
#plt.xticks(x_ticks)
y_ticks = np.arange(0, 1.1, 0.1)
plt.yticks(y_ticks)

plt.show()