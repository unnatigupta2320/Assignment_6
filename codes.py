import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-5, 5, 1000)
x1 = np.linspace(-6, 6, 1000) 
x2 = np.linspace(0, 5, 1000)
y = 3*x*x/4.0
y1 = (3*x1+12)/2

#coordinates of each point
k = np.array([-2,3])
l = np.array([4,12])
n = np.array([-2,0])
m = np.array([4,0])
c = np.array([0,0])

#plotting 
plt.plot(c[0], c[1], 'o',color='g')
plt.text(c[0] +0, c[1] - 1.3, 'C', weight='bold')
plt.plot(k[0], k[1], 'o',color='g')
plt.text(k[0] + 0.6, k[1] + 0.6, 'K',weight='bold')
plt.plot(l[0], l[1], 'o',color='g')
plt.text(l[0] + 0.3, l[1] + 0.3, 'L',weight='bold')
plt.plot(m[0], m[1], 'o',color='g')
plt.text(m[0] + 0.3, m[1] + 0.3, 'M')
plt.plot(n[0], n[1], 'o',color='g')
plt.text(n[0] - 1.3, n[1] + 0.3, 'N')

plt.plot(x1, y1, '-', label='$2y = 3x+12$',color='b')
plt.plot(x, y, '-', label='$3x^2 = 4y$',color='r')
plt.axvline(x=-2,color='gray',linestyle='--')
plt.axvline(x=4,color='gray',linestyle='--')




#labelling each points
plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
