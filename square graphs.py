import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,100)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x,y)
plt.plot(y,x)
plt.xlim(-3,3)
plt.ylim(-3,3)

ax.set_aspect('equal', adjustable='box')

plt.xlabel("x")
plt.ylabel("sinx")

plt.show()