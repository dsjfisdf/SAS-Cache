############# overall hdd latency P99
# import matplotlib.pyplot as plt
# import numpy as np

# plt.rc('font', family='Times New Roman') 
# plt.rcParams.update({'font.size': 32})
# plt.rc('font', weight='bold')


# x = ['WS-Cache','DS-Cache1','DS-Cache5','SAS-Cache1','SAS-Cache5'] #点的横坐标
# y1 = [45947.18, 18588.34, 15539.8, 13922.1, 11105.71] #线1的纵坐标
# y2 = [29263.40976, 13622.80566, 11801.03101, 13476.07385, 10545.35497] #线2的纵坐标

# bar_width = 0.3 # Make bars narrower
# a = np.arange(len(x))
# b = a + bar_width


# plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='128MB')
# plt.bar(b, y2, width=bar_width, color='lightyellow', hatch='-', edgecolor='black', label='256MB')


# plt.legend()
# plt.xticks(a + bar_width / 2, x) 

# plt.xlabel('Schemes', weight='bold')  
# plt.ylabel('P99 Response Time(us)', weight='bold')

# plt.show()

########### overall hdfs latency P99
# import matplotlib.pyplot as plt
# plt.rcParams.update({'font.size': 32})
# plt.rc('font', weight='bold')

# plt.rc('font', family='Times New Roman') 

# x = ['WS-Cache','DS-Cache1','SAS-Cache1','SAS-Cache1','SAS-Cache5'] #点的横坐标
# y1 = [5300.345187, 5906.182927, 5176.660149, 5318.669297, 4586.899965] #线1的纵坐标
# y2 = [4244.087904, 4272.728619, 3771.061887, 4124.065097, 3771.061887] #线2的纵坐标

# bar_width = 0.3 # Make bars narrower
# a = np.arange(len(x))
# b = a + bar_width


# plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='128MB')
# plt.bar(b, y2, width=bar_width, color='lightyellow', hatch='-', edgecolor='black', label='256MB')


# # plt.legend()
# plt.xticks(a + bar_width / 2, x) 

# plt.xlabel('Schemes', weight='bold')  
# plt.ylabel('P99 Response Time(us)', weight='bold')

# plt.show()


############# overall hdd latency P99
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (128, 256)
y1 = [45947.18343, 29263.40976]
y2 = [18588.33619, 13622.80566]
y3 = [15539.80127, 11801.03101]
y4 = [13922.10412, 13476.07385]
y5 = [11105.70554, 10545.35497]

bar_width = 0.15 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='WS-Cache')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='DS-Cache1')
plt.bar(c, y3, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='SAS-Cache1') 
plt.bar(d, y4, width=bar_width, color='lightcoral', hatch='/', edgecolor='black', label='DS-Cache5')
plt.bar(e, y5, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='SAS-Cache5')


plt.legend()
plt.xticks(a + bar_width*2, x) 

plt.xlabel('Block Cache Size(MB)', weight='bold')  
plt.ylabel('P99 Response Time(us)', weight='bold')

plt.show()


########### overall hdfs latency P99
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})

plt.rc('font', weight='bold')

# 输入统计数据
x = (128, 256)
y1 = [5616.069555, 4244.087904]
y2 = [5506.182927, 4272.728619]
y3 = [5076.660149, 3771.061887]
y4 = [5318.669297, 4124.065097]
y5 = [4586.899965, 3615.127543]

bar_width = 0.15 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='WS-Cache')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='DS-Cache1')
plt.bar(c, y3, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='SAS-Cache1') 
plt.bar(d, y4, width=bar_width, color='lightcoral', hatch='/', edgecolor='black', label='DS-Cache5')
plt.bar(e, y5, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='SAS-Cache5')


plt.legend()
plt.xticks(a + bar_width*2, x) 


plt.xlabel('Block Cache Size(MB)', weight='bold')  
plt.ylabel('P99 Response Time(us)', weight='bold')

plt.show()





########## overall hdfs throughput
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (128, 256)
y1 = [955, 1655]
y2 = [1009, 1472]
y3 = [1252, 1924]
y4 = [1028, 1508]
y5 = [1348, 2046]

bar_width = 0.15 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='WS-Cache')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='DS-Cache1')
plt.bar(c, y3, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='SAS-Cache1') 
plt.bar(d, y4, width=bar_width, color='lightcoral', hatch='/', edgecolor='black', label='DS-Cache5')
plt.bar(e, y5, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='SAS-Cache5')


plt.legend()
plt.xticks(a + bar_width*2, x) 

plt.xlabel('Block Cache Size(MB)', weight='bold')  
plt.ylabel('Operations per Second', weight='bold')

plt.show()

########## overall hdd throughput
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})

plt.rc('font', weight='bold')

# 输入统计数据
x = (128, 256)
y1 = [145, 299]
y2 = [394, 647]
y3 = [446, 769]
y4 = [446, 664]
y5 = [531, 893]

bar_width = 0.15 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='WS-Cache')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='DS-Cache1')
plt.bar(c, y3, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='SAS-Cache1') 
plt.bar(d, y4, width=bar_width, color='lightcoral', hatch='/', edgecolor='black', label='DS-Cache5')
plt.bar(e, y5, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='SAS-Cache5')


plt.legend()
plt.xticks(a + bar_width*2, x) 


plt.xlabel('Block Cache Size(MB)', weight='bold')  
plt.ylabel('Operations per Second', weight='bold')

plt.show()



########## overall cache hit ratio
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})

plt.rc('font', weight='bold')

# 输入统计数据
x = (128, 256)
y1 = [0.7586385394, 0.876407384]
y2 = [0.9240695453, 0.9361891615]
y3 = [0.9641445663, 0.9726827839]
y4 = [0.9380747821, 0.9394021054]
y5 = [0.9762752291, 0.9765659431]

bar_width = 0.15 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='WS-Cache')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='DS-Cache1')
plt.bar(c, y3, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='SAS-Cache1') 
plt.bar(d, y4, width=bar_width, color='lightcoral', hatch='/', edgecolor='black', label='DS-Cache5')
plt.bar(e, y5, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='SAS-Cache5')


plt.legend()
plt.xticks(a + bar_width*2, x) 
plt.ylim(0.5, 1)


plt.xlabel('Block Cache Size(MB)', weight='bold')  
plt.ylabel('Overall Cache Hit Ratio', weight='bold')

plt.show()


########## Block cache hit ratio
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})

plt.rc('font', weight='bold')

# 输入统计数据
x = (128, 256)
y1 = [0.7586385394, 0.876407384]
y2 = [0.7576385394, 0.878407384]
y3 = [0.7586383945, 0.87604384]
y4 = [0.7586338594, 0.876420784]
y5 = [0.7586348539, 0.876470384]

bar_width = 0.15 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='WS-Cache')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='DS-Cache1')
plt.bar(c, y3, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='SAS-Cache1') 
plt.bar(d, y4, width=bar_width, color='lightcoral', hatch='/', edgecolor='black', label='DS-Cache5')
plt.bar(e, y5, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='SAS-Cache5')


plt.legend()
plt.xticks(a + bar_width*2, x) 


plt.xlabel('Block Cache Size(MB)', weight='bold')  
plt.ylabel('Block Cache Hit Ratio', weight='bold')

plt.show()


############# secondary cache hit ratio
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Times New Roman') 
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')


x = ['256/5120','256/1024','256/512','128/5120','128/1024','128/512'] #点的横坐标
y1 = [0.6613986628, 0.6470630309, 0.5811746559, 0.8191788917, 0.7825289396, 0.6890589766] #线1的纵坐标
y2 = [0.9998483729, 0.9999691738, 0.9996064867, 0.9998520162, 0.9999769707, 0.9996769565] #线2的纵坐标

bar_width = 0.3 # Make bars narrower
a = np.arange(len(x))
b = a + bar_width


plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='DS-Cache')
plt.bar(b, y2, width=bar_width, color='lightyellow', hatch='-', edgecolor='black', label='SAS-Cache')


plt.legend()
plt.xticks(a + bar_width / 2, x) 

plt.xlabel('Block Cache Size/Secondary Cache Hit Ratio(MB)', weight='bold')  
plt.ylabel('Secondary Cache Hit Ratio', weight='bold')

plt.show()