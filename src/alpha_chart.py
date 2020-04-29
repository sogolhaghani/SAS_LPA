import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, constrained_layout=True)

ax1.plot(x,  np.array([0.6454,0.6471,0.6443,0.647,0.7123,0.7258,0.7441,0.7542,0.7722,0.7643,0.7651]) ,color='#003f5c',  marker='*', label='v=0.1')
ax1.plot(x,  np.array([0.5478,0.6596,0.6768,0.6638,0.6929,0.7154,0.7201,0.7063,0.7222,0.7147,0.7142]) ,color='#bc5090',linestyle='--', marker='o', label='v=0.3')
ax1.set_ylim([0.4,1])
ax1.set_xlabel("α", fontsize=16)
ax1.set_ylabel("NMI", fontsize=16)
ax1.legend( fontsize=16)
ax1.grid(linestyle='dotted')


ax2.plot(x,  np.array([0.411304456,0.444263841,0.470279147, 0.499788038, 0.401121859,0.378091254, 0.361582329,0.357861926,0.338054328, 0.345072515, 0.3439705    ]) ,color='#003f5c',  marker='*', label='v=0.1')
ax2.plot(x,  np.array([0.680894316, 0.571055778, 0.569320717, 0.586058936, 0.558711243, 0.569446457, 0.559318671, 0.57601084, 0.56896132, 0.572065178,0.56407602  ]) ,color='#bc5090',linestyle='--', marker='o', label='v=0.3')
ax2.set_ylim([0.2,0.8])
ax2.set_xlabel("α", fontsize=16)
ax2.set_ylabel("Entropy", fontsize=16)
ax2.legend( fontsize=16)
ax2.grid(linestyle='dotted')



ax3.plot(x,  np.array([0.347862356621481, 0.384358706986444,0.398331595411887, 0.464859228362878, 0.42606882168926, 0.417101147028154, 0.415641293013556, 0.427528675703858,  0.427320125130344, 0.42148070907195, 0.425443169968717  ]) ,color='#003f5c',  marker='*', label='v=0.1')
ax3.plot(x,  np.array([0.551522736754276, 0.366916979557781, 0.424488944513976, 0.430329578639967, 0.413433458489779, 0.432624113475177,  0.427617855652899, 0.437838965373383, 0.43700458906967, 0.435961618690029, 0.424906132665832 ]) ,color='#bc5090',linestyle='--', marker='o', label='v=0.3')
ax3.set_ylim([0.2,0.7])
ax3.set_xlabel("α", fontsize=16)
ax3.set_ylabel("Density", fontsize=16)
ax3.legend( fontsize=16)
ax3.grid(linestyle='dotted')


plt.show()