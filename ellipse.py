import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-7,7,900)
def func1(a,b,x):
    return b*np.sqrt(1-pow(x/a,2))
def func2(a,b,x):
    return -b*np.sqrt(1-pow(x/a,2))
y1=func1(7,3,x)
y2=func2(7,3,x)
fig,ax=plt.subplots()
ax.set_ylim(-3.5,3.5)
ax.set_xlim(-7.5,7.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('ellipse')
plt.axhline(0,color='red',linestyle='--')
plt.axvline(0,color='red',linestyle='--')
plt.plot(x,y1,color='orange')
plt.plot(x,y2,color='orange')

plt.show()

  
