########## ops: the effectiveness of Cache Filter
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (5, 15, 25)
y1 = [770, 1416, 2069]
y2 = [835, 1513, 2237]
y3 = [886, 1607, 2351]
y4 = [918, 1695, 2406]
y5 = [923, 1703, 2416]

bar_width = 0.15 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='DS-Cache')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='DS+CF(2)')
plt.bar(c, y3, width=bar_width, color='blue', hatch='-', edgecolor='black', label='DS+CF(4)')
plt.bar(d, y4, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='DS+CF(8)')
plt.bar(e, y5, width=bar_width, color='red', hatch='-', edgecolor='black', label='DS+CF(16)')


plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Read Random Exp Range', weight='bold')  
plt.ylabel('Operations per Second', weight='bold')

plt.show()


########## secondary cache hit ratio: the effectiveness of Cache Filter
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (5, 15, 25)
y1 = [0.7111191863, 0.587196931, 0.499367443]
y2 = [0.8256597954, 0.7291011571, 0.6999654607]
y3 = [0.9402621399, 0.893651339, 0.8903423017]
y4 = [0.9959245858, 0.9923164897, 0.9926401532]
y5 = [0.999963007, 0.9999444822, 0.9999314834]

bar_width = 0.15 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='DS-Cache')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='DS+CF(2)')
plt.bar(c, y3, width=bar_width, color='blue', hatch='-', edgecolor='black', label='DS+CF(4)')
plt.bar(d, y4, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='DS+CF(8)')
plt.bar(e, y5, width=bar_width, color='red', hatch='-', edgecolor='black', label='DS+CF(16)')




plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Read Random Exp Range', weight='bold')  
plt.ylabel('Secondary Cache Hit Ratio', weight='bold')
plt.ylim(0.4, 1.02)

plt.show()

########## Compaction Replacement : ops
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (512, 1024, 5120, 10240)
y1 = [1431, 1472, 1508, 1517]
y2 = [1598, 1782, 1889, 1893]

bar_width = 0.25 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  

plt.bar(a, y1, width=bar_width, color='blue', hatch='/', edgecolor='black', label='DS-Cache')
plt.bar(b, y2, width=bar_width, color='red', hatch='-', edgecolor='black', label='DS+CR')


plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Secondary Cache Size(MB)', weight='bold')  
plt.ylabel('Operations per Second', weight='bold')

plt.show()


########## Compaction Replacement : secondary cache hit ratio
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (512, 1024, 5120, 10240)
y1 = [0.5816918267, 0.647470249, 0.6624643893, 0.662721145]
y2 = [0.6553460307, 0.7617361335, 0.7977313132, 0.7969173674]

bar_width = 0.25 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  

plt.bar(a, y1, width=bar_width, color='blue', hatch='/', edgecolor='black', label='DS-Cache')
plt.bar(b, y2, width=bar_width, color='red', hatch='-', edgecolor='black', label='DS+CR')


plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Secondary Cache Size(MB)', weight='bold')  
plt.ylabel('Secondary Cache Hit Ratio', weight='bold')

plt.ylim(0, 1)

plt.show()


########## Insertion Control: Secondary Cache Hit Ratio
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (512, 1024, 5120)
y1 = [0.5822947272, 0.6493832217, 0.6631168583]
y2 = [0.6022947272, 0.65493832217, 0.6731168583]
y3 = [0.6122947272, 0.6693832217, 0.6931168583]
y4 = [0.6302947272, 0.6858044904, 0.7131168583]
y5 = [0.6322947272, 0.6908044904, 0.7197027345]

bar_width = 0.15 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3
e = a + bar_width*4

plt.bar(a, y1, width=bar_width, color='lightyellow', hatch='/', edgecolor='black', label='DS-Cache')
plt.bar(b, y2, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='DS+IC(2)')
plt.bar(c, y3, width=bar_width, color='blue', hatch='-', edgecolor='black', label='DS+IC(4)')
plt.bar(d, y4, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='DS+IC(6)')
plt.bar(e, y5, width=bar_width, color='red', hatch='-', edgecolor='black', label='DS+IC(10)')


plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Secondary Cache Size(MB)', weight='bold')  
plt.ylabel('Secondary Cache Hit Ratio', weight='bold')
plt.ylim(0.5, 0.802)

plt.show()

########## Insertion Control: reduced insertion ratio
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman
plt.rcParams.update({'font.size': 32})
plt.rc('font', weight='bold')



# 输入统计数据
x = (512, 1024, 5120)
y1 = [0.07397963165, 0.08219442901, 0.08528972724]
y2 = [0.1572638286, 0.1741916077, 0.1791781135]
y3 = [0.1961286738, 0.2179586156, 0.2255315204]
y4 = [0.2102858975, 0.2355984345, 0.2411182565]

bar_width = 0.2 # Make bars narrower

a = np.arange(len(x))
b = a + bar_width  
c = a + bar_width*2
d = a + bar_width*3

plt.bar(a, y1, width=bar_width, color='lightblue', hatch='-', edgecolor='black', label='DS+IC(2)')
plt.bar(b, y2, width=bar_width, color='blue', hatch='-', edgecolor='black', label='DS+IC(4)')
plt.bar(c, y3, width=bar_width, color='lightcoral', hatch='-', edgecolor='black', label='DS+IC(6)')
plt.bar(d, y4, width=bar_width, color='red', hatch='-', edgecolor='black', label='DS+IC(10)')




plt.legend()
plt.xticks(a + bar_width/2, x) 

plt.xlabel('Secondary Cache Size(MB)', weight='bold')  
plt.ylabel('Reduced Block Insertion Ratio', weight='bold')
plt.ylim(0, 0.402)

plt.show()