print("\n\n-----------------------------")
print("-WYKRESY - MatPlotLib------------------")
print("-----------------------------\n")

import numpy as np
import matplotlib.pyplot as plt

dane = np.arange(0.0, 2.0, 0.01)
fs = 1+np.sin(2*np.pi*dane) #niby petla

fig,ax = plt.subplots() #wykres
ax.plot(dane, fs)
ax.set(xlabel="czas [s]", ylabel="napiecie pradu [V]", title="rozkład napiecia pradu w czasie") #opis osi
ax.grid() #właczenie siatki
fig.savefig("wykres.png")
plt.show()
