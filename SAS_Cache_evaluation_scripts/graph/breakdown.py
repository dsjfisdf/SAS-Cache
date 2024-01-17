########## hdfs throughput
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})

plt.rc('font', weight='bold')

# 输入统计数据
x = ('DS-Cache', 'DS+CF', 'DF-IC', 'DS+CR', 'SAS-Cache')
y1 = [1508, 1792, 1628, 1899, 2046]
y2 = [1472, 1688, 1569, 1782, 1924]

bar_width = 0.3 # Make bars narrower
a = np.arange(len(x))
b = a + bar_width


plt.bar(a, y1, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='5GB')
plt.bar(b, y2, width=bar_width, color='lightyellow', hatch='-', edgecolor='black', label='1GB')


plt.legend()
plt.xticks(a + bar_width / 2, x) 

plt.xlabel('Schemes', weight='bold')  
plt.ylabel('Operations per Second', weight='bold')

plt.show()



########## hdfs latency 
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})

plt.rc('font', weight='bold')

# 输入统计数据

x = ('DS-Cache', 'DS+CF', 'DF-IC', 'DS+CR', 'SAS-Cache')
y1 = [4124.065097, 3843.985249, 4028.81621, 3932.346198, 3615.127543]
y2 = [4272.728619, 3931.824488, 4130.957274, 4046.823043, 3771.061887]

bar_width = 0.3 # Make bars narrower
a = np.arange(len(x))
b = a + bar_width


plt.bar(a, y1, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='5GB')
plt.bar(b, y2, width=bar_width, color='lightyellow', hatch='-', edgecolor='black', label='1GB')


# plt.legend()
plt.xticks(a + bar_width / 2, x) 


plt.xlabel('Schemes', weight='bold')  
plt.ylabel('P99 Response Time(us)', weight='bold')

plt.show()


########## hdfs overall cache ratio  
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})

plt.rc('font', weight='bold')

# 输入统计数据
x = ('DS-Cache', 'DS+CF', 'DF-IC', 'DS+CR', 'SAS-Cache')
y1 = [0.9394021054, 0.9384021054, 0.9494021054, 0.9674127977, 0.9774127977]
y2 = [0.9361891615, 0.935947712, 0.9418383392, 0.9586827839, 0.9726827839]


bar_width = 0.3 # Make bars narrower
a = np.arange(len(x))
b = a + bar_width


plt.bar(a, y1, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='5GB')
plt.bar(b, y2, width=bar_width, color='lightyellow', hatch='-', edgecolor='black', label='1GB')


# plt.legend()
plt.xticks(a + bar_width / 2, x) 
plt.ylim(0.8, 1)

plt.xlabel('Schemes', weight='bold')  
plt.ylabel('Overall Cache Hit Ratio', weight='bold')

plt.show()

########## hdfs secondary cache ratio  
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})

plt.rc('font', weight='bold')

# 输入统计数据
x = ('DS-Cache', 'DS+CF', 'DF-IC', 'DS+CR', 'SAS-Cache')
y1 = [0.6613986628, 0.9989896758, 0.7197027345, 0.809461172, 0.9998483729]
y2 = [0.6470630309, 0.99789508, 0.6908044904, 0.7868858064, 0.9989691738]


bar_width = 0.3 # Make bars narrower
a = np.arange(len(x))
b = a + bar_width


plt.bar(a, y1, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='5GB')
plt.bar(b, y2, width=bar_width, color='lightyellow', hatch='-', edgecolor='black', label='1GB')


# plt.legend()
plt.xticks(a + bar_width / 2, x) 




plt.xlabel('Schemes', weight='bold')  
plt.ylabel('Secondary Cache Hit Ratio', weight='bold')

plt.show()



########## Secondary Cache Access and Hit Numbers
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})

plt.rc('font', weight='bold')

# 输入统计数据
x = ('DS-Cache', 'DS+CF', 'DF-IC', 'DS+CR', 'SAS-Cache')
y1 = [583.586, 387.441, 583.586, 582.338, 461.659]
y2 = [385.983, 387.437, 406.665, 450.380, 461.589]


bar_width = 0.3 # Make bars narrower
a = np.arange(len(x))
b = a + bar_width


plt.bar(a, y1, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='Access Numbers')
plt.bar(b, y2, width=bar_width, color='lightyellow', hatch='-', edgecolor='black', label='Hit Numbers')


plt.legend()
plt.xticks(a + bar_width / 2, x) 


plt.xlabel('Schemes', weight='bold')  
plt.ylabel('Access and Hit Numbers(k)', weight='bold')

plt.show()