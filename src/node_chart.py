import matplotlib.pyplot as plt
import numpy as np

x = np.array([1000, 5000, 10000, 50000])


fig, (ax1, ax2, ax3 , ax4) = plt.subplots(1, 4, constrained_layout=True)
ax1.plot(x,  np.array([1,0.9988,0.998,0.9988]), color='#bc5090',linestyle='--', marker='o')
ax1.set_xlabel("Number of Node", fontsize=16)
ax1.set_ylabel("NMI", fontsize=16)
# ax1.legend( fontsize=16)
ax1.grid(linestyle='dotted')
ax1.set_ylim([0.5,1])


ax2.plot(x,  np.array([0.143975611206936,0.146711964317136, 0.148033023144415,0.146401 ]) ,color='#bc5090',linestyle='--', marker='o')
ax2.set_xlabel("Number of Node", fontsize=16)
ax2.set_ylabel("Entropy", fontsize=16)
# ax2.legend( fontsize=16)
ax2.grid(linestyle='dotted')
ax2.set_ylim([0,1])

ax3.plot(x,  np.array([0.899369790607847,0.894727998319681, 0.896763604225411, 0.8934]) ,color='#bc5090',linestyle='--', marker='o')
ax3.set_xlabel("Number of Node", fontsize=16)
ax3.set_ylabel("Density", fontsize=16)
# ax3.legend( fontsize=16)
ax3.grid(linestyle='dotted')
ax3.set_ylim([0,1])

ax4.plot(x,  np.array([1.62, 16.36, 47.50, 734.65 ]) ,color='#bc5090',linestyle='--', marker='o')
ax4.set_xlabel("Number of Node", fontsize=16)
ax4.set_ylabel("Time(s)", fontsize=16)
# ax4.legend( fontsize=16)
ax4.grid(linestyle='dotted')


plt.show()