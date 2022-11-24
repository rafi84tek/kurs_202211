import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
x,y = np.random.randn(2,100)
fig,[ax1,ax2] = plt.subplots(2,1,sharex=True)
ax1.xcorr(x,y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.grid(True)

ax2.acorr(x, usevlines=True, maxlags=50, normed=True, lw=2)
ax2.grid(True)


plt.show()

