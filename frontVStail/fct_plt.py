import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('FCT/mean_1MB')

label_list = ['Mean', '50th', '95th']
num_front = data[0:, 0]
num_tail = data[0:, 1]
left = range(len(num_front))

plt.figure(dpi=400)
rects1 = plt.bar(x=left, height=num_front, width=0.2, alpha=0.8, color='black', label='front')
rects2 = plt.bar(x=[i+0.2 for i in left], height=num_tail, width=0.2, color='silver', label='tail')

plt.ylim(0, 100)
plt.ylabel('Flow Completion Time (ms)')

plt.xticks([index + 0.1 for index in left], label_list)
plt.xlabel('Percentile')
plt.title('FCT of 1MB short flow under long-lived flow in 10Gb')
plt.legend()

for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha='center', va='bottom')

for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha='center', va='bottom')

plt.show()
