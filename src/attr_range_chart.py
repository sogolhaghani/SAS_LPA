import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.1, 0.5, 0.9])


fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Horizontally stacked subplots')

ax1.plot(x,  np.array([0.73116, 0.75758, 0.72258]) ,color='blue', linewidth=2)
ax1.plot(x,  np.array([0.73582,0.74787, 0.72692]) ,color='orange', linewidth=2)
ax1.plot(x,  np.array([0.72412,0.71219,0.71741 ]) ,color='gray', linewidth=2)
ax1.plot(x,  np.array([0.71637, 0.72302, 0.7037]) ,color='green', linewidth=2)



ax2.plot(x,  np.array([0.09533133, 0.132715016, 0.10280015]) ,color='blue', linewidth=2)
ax2.plot(x,  np.array([0.261641959,0.462010327, 0.508275109]) ,color='orange', linewidth=2)
ax2.plot(x,  np.array([0.367612344,0.66276883,0.781989791 ]) ,color='gray', linewidth=2)
ax2.plot(x,  np.array([0.460590816, 0.89222738,1.18830159]) ,color='green', linewidth=2)

plt.show()