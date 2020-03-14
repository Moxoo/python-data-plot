import matplotlib.pyplot as plt
import numpy as np
print("plot")

data = np.loadtxt('throughputPerSec')
queue_data = np.loadtxt('percentile_99')

label_list = ['20', '40', '60', '80', '85', '90', '100', '150', '200', '250']
queue_tail = queue_data[0:, 1]
queue_front = queue_data[0:, 2]
data_tail = data[0:, 0]
data_front = data[0:, 1]
plt.figure(dpi=400)
plt.plot(label_list, data_tail, '--+--', color='r', label='tail mark throughput', linewidth=0.6)
plt.plot(label_list, data_front, '--*--', color='black', label='front mark throughput', linewidth=0.6)
y_ticks = np.arange(850, 1001, 10)
plt.yticks(y_ticks)
plt.xlabel('Server Num')
plt.ylabel('Throughput (Mbps)')
plt.legend()
ax=plt.twinx()
ax.plot(label_list, queue_tail, '--+--', color='cornflowerblue', label='99th tail mark QueueSize', linewidth=0.6)
ax.plot(label_list, queue_front, '--*--', color='y', label='99th front mark QueueSize', linewidth=0.6)
plt.ylabel('Queue Length (Pkts)')
plt.legend()

plt.title('DCTCP Throughput And 99th QueueSize')

# x_ticks = np.arange(0, 45.1, 5)
# plt.xticks(x_ticks)
plt.show()
