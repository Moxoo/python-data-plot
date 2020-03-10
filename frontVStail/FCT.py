import matplotlib.pyplot as plt
import numpy as np

print("plot")

data = np.loadtxt('FCT/FCT_1MB_10Gb')
data1 = data[0:, 0]
data2 = data[0:, 1]

sum1 = 0
for fct in data1:
    sum1 = sum1 + fct
avg1 = sum1/len(data1)
avg1 = round(avg1)
print('num of data1: ', len(data1))
print('mean fct of front n=10: ', avg1)
print('\n')

sum2 = 0
for fct in data2:
    sum2 = sum2 + fct
avg2 = sum2/len(data2)
avg2 = round(avg2)
print('num of data2: ', len(data2))
print('mean fct of tail n=10:', avg2)
print('\n')

data1.sort()
data2.sort()

th_50_1 = data1[len(data1)//2]
th_50_1 = round(th_50_1)
th_50_2 = data2[len(data2)//2]
th_50_2 = round(th_50_2)
print('50th percentile of front: ', th_50_1)
print('50th percentile of tail: ', th_50_2)
print('\n')

th_95_1 = data1[int(len(data1)*0.95)]
th_95_1 = round(th_95_1)
th_95_2 = data2[int(len(data2)*0.95)]
th_95_2 = round(th_95_2)
print('95th percentile of front: ', th_95_1)
print('95th percentile of tail: ', th_95_2)

#
# plt.figure(dpi=400)
# plt.plot(10, avg1, '^-', color='cornflowerblue', label="front mark", linewidth=1)
# plt.plot(10, avg2, 'o-', color='indianred', label="tail mark", linewidth=1)
# plt.legend()
# plt.title('FCT')
# plt.xlabel('Number of server')
# plt.ylabel('Flow Completion Time (ms)')
# # x_ticks = np.arange(5, 25.1, 5)
# # plt.xticks(x_ticks)
# # y_ticks = np.arange(0, 51, 5)
# # plt.yticks(y_ticks)
# plt.show()
