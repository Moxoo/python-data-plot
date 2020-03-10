import matplotlib.pyplot as plt
import numpy as np
print("plot")

data1 = np.loadtxt('mark_ratio_data.plotme')
plt.figure(dpi=400)
plt.plot(data1[0:, 0], data1[0:, 1]*100, 'o', color='y', label="DCTCP", linewidth=2)
plt.plot(data1[0:, 0], data1[0:, 2]*100, 'p', color='g', label="CUBIC", linewidth=2)
plt.legend()
plt.title('Marking ratio')
plt.xlabel('Flow num')
plt.ylabel('%')
#x_ticks = np.arange(0, 0.051)
#plt.xticks(x_ticks)
y_ticks = np.arange(0, 101, 10)
plt.yticks(y_ticks)

plt.show()
