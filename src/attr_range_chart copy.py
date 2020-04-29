import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.1, 0.5, 0.9])


fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x,  np.array([0.73116, 0.75758, 0.72258]) ,color='#003f5c',marker='o', label='R=2')
ax1.plot(x,  np.array([0.73582,0.74787, 0.72692]) ,color='#7a5195',marker='*', label='R=5')
ax1.plot(x,  np.array([0.72412,0.71219,0.71741 ]) ,color='#ef5675',marker='s', label='R=10')
ax1.plot(x,  np.array([0.71637, 0.72302, 0.7037]) ,color='#ffa600',marker='X', label='R=50')
ax1.set_xlabel("Attribute Noise", fontsize=16)
ax1.set_ylabel("NMI", fontsize=16)
ax1.legend( fontsize=16)
ax1.grid(linestyle='dotted')
ax1.set_ylim([0.6,1])


ax2.plot(x,  np.array([0.09533133, 0.132715016, 0.10280015]),color='#003f5c',marker='o', label='R=2')
ax2.plot(x,  np.array([0.261641959,0.462010327, 0.508275109]) ,color='#7a5195',marker='*', label='R=5')
ax2.plot(x,  np.array([0.367612344,0.66276883,0.781989791 ]) ,color='#ef5675',marker='s', label='R=10')
ax2.plot(x,  np.array([0.460590816, 0.89222738,1.18830159]) ,color='#ffa600',marker='X', label='R=50')
ax2.set_xlabel("Attribute noise", fontsize=16)
ax2.set_ylabel("Entropy", fontsize=16)
ax2.legend( fontsize=16)
ax2.grid(linestyle='dotted')
ax2.set_ylim([0,1.55])
plt.show()