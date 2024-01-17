########## motivation: the invalid portion of evicted blocks. 
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (64, 128, 256, 384, 512)
y1 = [641.991, 471.077, 291.541, 205.949, 159.912]
y2 = [17.709, 36.601, 69.748, 84.610, 95.690]

bar_width = 0.3 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  

plt.bar(a, y1, width=bar_width, color='lightcoral', hatch='/', edgecolor='black', label='Insert Numbers')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='Invalid Numbers')



plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Block Cache Size(MB)', weight='bold')  
plt.ylabel('Numbers(k)', weight='bold')

plt.show()


########## motivation: the invalid portion of retained in the cache. 
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')

# 输入统计数据
x = (64, 128, 256, 512, 1024, 2048)
y1 = [16.384, 32.768, 65.536, 131.072, 262.144, 524.288]
y2 = [5.654, 11.687, 23.374, 47.126, 67.777, 91.724]

bar_width = 0.3 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  

plt.bar(a, y1, width=bar_width, color='lightcoral', hatch='/', edgecolor='black', label='Total Numbers')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='Invalid Numbers')


plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Secondary Cache Size(MB)', weight='bold')  
plt.ylabel('Numbers(k)', weight='bold')

plt.show()

########## ops: the effectiveness of secondary cache(useful when cache hit ratio is high)
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (5, 15, 25)
y1 = [645, 1734, 2691]
y2 = [770, 1416, 2069]
y3 = [161, 401, 642]
y4 = [260, 511, 729]

bar_width = 0.2 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='WS-Cache(HDFS)')
plt.bar(b, y2, width=bar_width, color='lightyellow', hatch='-', edgecolor='black', label='DS-Cache(HDFS)')
plt.bar(c, y3, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='WS-Cache(HDD)')
plt.bar(d, y4, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='DS-Cache(HDD)')


plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Read Random Exp Range', weight='bold')  
plt.ylabel('Operations per Second', weight='bold')

plt.show()


########## cache hit ratio: the effectiveness of secondary cache(useful when cache hit ratio is high)
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (5, 15, 25)
y1 = [0.6591686089, 0.8565154843, 0.8944451846]
y2 = [0.9048086836, 0.94077857, 0.9459309219]
y3 = [0.7111191863, 0.587196931, 0.499367443]

bar_width = 0.25 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='WS-Cache(Overall)')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='/', edgecolor='black', label='DS-Cache(Overall)')
plt.bar(c, y3, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='DS-Cache(Secondary Cache)')


plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Read Random Exp Range', weight='bold')  
plt.ylabel('Cache Hit Ratio', weight='bold')

plt.show()