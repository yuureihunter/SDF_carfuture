import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.suptitle('Graph', fontsize=14, fontweight='bold')
ax1.set_xlabel('year201X')
ax1.set_ylabel('value()')

x = [0,1,2,3,4,5]
y = [2.9,3.1,3.4,3.5,3.6,4]
ax1.plot(x,y,c='#1C86EE',label='stock car')
for x,y in zip(x,y):
    plt.text(x, y, '%.2f' % y, ha='left', va= 'bottom',\
    bbox={'facecolor':'#B0E0E6', 'alpha':0.5, 'pad':2.5})

a = [0,1,2,3,4,5]
b = [1.7,1.8,2.4,1.3,0.9,1]
ax1.plot(a,b,c='#32CD32',label='diff car')
for x,y in zip(a,b):
    plt.text(x, y, '%.2f' % y, ha='left', va= 'bottom',\
    bbox={'facecolor':'#54FF9F', 'alpha':0.5, 'pad':2.5})

leg = ax1.legend(loc='upper left')
plt.show()
