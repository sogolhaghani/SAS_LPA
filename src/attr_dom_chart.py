import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,5,10,100,500,1000])


fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x,  np.array([0.72061,0.723595,0.74072,0.72696,0.72549,0.7245]), color='#bc5090',linestyle='--', marker='o', label='v=0.3')
ax1.set_xlabel("Number of Attribute", fontsize=16)
ax1.set_ylabel("NMI", fontsize=16)
ax1.legend( fontsize=16)
ax1.grid(linestyle='dotted')
ax1.set_ylim([0.7,0.8])


ax2.plot(x,  np.array([0.363955026629233, 0.360570009,0.341733636,0.347206517,0.361336181,0.364311984
]) ,color='#bc5090',linestyle='--', marker='o', label='v=0.3')
ax2.set_xlabel("Number of Attribute", fontsize=16)
ax2.set_ylabel("Entropy", fontsize=16)
ax2.legend( fontsize=16)
ax2.grid(linestyle='dotted')
ax2.set_ylim([0.2,0.8])
plt.show()