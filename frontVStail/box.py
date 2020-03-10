# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

# data1 = np.loadtxt('queue_size/queue_size_5_tail.plotme')
# data2 = np.loadtxt('queue_size/queue_size_5_front.plotme')
# data3 = np.loadtxt('queue_size/queue_size_10_tail.plotme')
# data4 = np.loadtxt('queue_size/queue_size_10_front.plotme')
# data5 = np.loadtxt('queue_size/queue_size_15_tail.plotme')
# data6 = np.loadtxt('queue_size/queue_size_15_front.plotme')
# data7 = np.loadtxt('queue_size/queue_size_20_tail.plotme')
# data8 = np.loadtxt('queue_size/queue_size_20_front.plotme')
# data9 = np.loadtxt('queue_size/queue_size_25_tail.plotme')
# data10 = np.loadtxt('queue_size/queue_size_25_front.plotme')
#
# data = {
#     '05 T': data1[0:, 1],
#     '05 F': data2[0:, 1],
#     '10 T': data3[0:, 1],
#     '10 F': data4[0:, 1],
#     '15 T': data5[0:, 1],
#     '15 F': data6[0:, 1],
#     '20 T': data7[0:, 1],
#     '20 F': data8[0:, 1],
#     '25 T': data9[0:, 1],
#     '25 F': data10[0:, 1]
# }

data1 = np.loadtxt('queue_size_10Gb/queue_size_45_tail.plotme')
data2 = np.loadtxt('queue_size_10Gb/queue_size_45_front.plotme')
data = {
    'tail':  data1[0:, 1],
    'front':  data2[0:, 1],
}
df = pd.DataFrame(data)
sns.catplot(kind="box", data=df, color='coral', height=7, width=0.7)
plt.title('BOX of queue length,N=45 10Gb')
plt.xlabel('Server number And Mark mode')
plt.ylabel('Inst. Queue Len(Pkts)')
plt.show()