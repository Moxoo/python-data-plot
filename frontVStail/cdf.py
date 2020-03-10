# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# data1 = np.loadtxt('queue_size/queue_size_tail_5.plotme')
# data2 = np.loadtxt('queue_size/queue_size_front_5.plotme')
# data = {
#     'tail': data1[0:, 1],
#     'front': data2[0:, 1],
# }
# df = pd.DataFrame(data)
# df.plot.box(title="queue size")
# plt.grid(linestyle='--', alpha=0.3)
# plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
#
# data1 = np.loadtxt('queue_size/queue_size_tail_5.plotme')
# data2 = np.loadtxt('queue_size/queue_size_front_5.plotme')
#
# data = {
#     'tail': data1[0:, 1],
#     'front': data2[0:, 1],
# }
# df = pd.DataFrame(data)
# sns.catplot(kind="boxen", data=df)
# plt.show()

data1 = np.loadtxt('queue_size_10Gb/queue_size_45_tail.plotme')
data2 = np.loadtxt('queue_size_10Gb/queue_size_45_front.plotme')

data1 = data1[0:, 1]
data2 = data2[0:, 1]

rse1 = stats.relfreq(data1, numbins=50)
x1 = rse1.lowerlimit + np.linspace(0, rse1.binsize*rse1.frequency.size, rse1.frequency.size)
y1 = np.cumsum(rse1.frequency)

rse2 = stats.relfreq(data2, numbins=50)
x2 = rse2.lowerlimit + np.linspace(0, rse2.binsize*rse2.frequency.size, rse2.frequency.size)
y2 = np.cumsum(rse2.frequency)


plt.figure(dpi=400)
plt.plot(x1, y1, color='black', label="tail mark", linewidth=1)
plt.plot(x2, y2, color='r', label="front mark", linewidth=1)
plt.legend()
plt.title('CDF of queue length, N=45 10Gb')
plt.xlabel('Queue Length(packets)')
plt.ylabel('Cumulative Fraction')
plt.show()



