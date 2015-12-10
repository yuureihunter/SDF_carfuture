import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.suptitle('Graph of stock car in september 2010 - 2015', fontsize=14, fontweight='bold')
ax1.set_title('show stock car and future stock car')
ax1.set_xlabel('year201X')
ax1.set_ylabel('value(billion of stock car data, million of diff car data)')

x = [0,1,2,3,4,5]
y = [2.81,2.99,3.18,3.42,3.56,3.65]
ax1.plot(x,y,c='#1C86EE',label='stock car')
for x,y in zip(x,y):
    plt.text(x, y, '%.2f' % y, ha='left', va= 'bottom',\
    bbox={'facecolor':'#B0E0E6', 'alpha':0.5, 'pad':2.5})
w = [5,6]
z = [3.65,3.7] #ค่าสุดท้ายยังไม่ใช่ค่าจริงๆ
ax1.plot(w,z,c='#FF6347',label='future stock car')
for x,y in zip(w,z):
    plt.text(x, y, '%.2f' % y, ha='left', va= 'bottom',\
    bbox={'facecolor':'#FA8072', 'alpha':0.5, 'pad':2.5})

a = [1,2,3,4,5]
b = [1.7,1.8,2.4,1.3,0.9]
ax1.plot(a,b,c='#32CD32',label='diff car')
for x,y in zip(a,b):
    plt.text(x, y, '%.1f' % y, ha='left', va= 'bottom',\
    bbox={'facecolor':'#54FF9F', 'alpha':0.5, 'pad':2.5})
g = [5,6]
h = [0.9,1.5] #ค่าสุดท้ายยังไม่ใช่ค่าจริงๆ
ax1.plot(g,h,c='#FF7F00',label='future diff car')
for x,y in zip(g,h):
    plt.text(x, y, '%.1f' % y, ha='left', va= 'bottom',\
    bbox={'facecolor':'#FF8C69', 'alpha':0.5, 'pad':2.5})

leg = ax1.legend(loc='lower left')
plt.show()



leg = ax1.legend(loc='lower left')
plt.show()
