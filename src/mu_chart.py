import matplotlib.pyplot as plt
import numpy as np


data_LFREA = np.array([[0.9936,1,    1,      1,      1,      0.991,  1,      0.9922, 0.9931,0.9974],
                [0.9805,0.9844,0.9866, 0.9765, 0.9679, 0.9719, 0.9836, 0.9923, 0.9925, 0.9702],
                [0.7596,0.7274,0.7507, 0.7539, 0.7148, 0.6463, 0.6975, 0.7986, 0.7243, 0.6681],
                [0.3928,0.3958,0.3281, 0.4117, 0.3921, 0.1155, 0.3979, 0.4142, 0.4113, 0.3824],
                [0.2929,0.337 ,0.3028, 0.2582, 0.2044, 0.2786, 0.3162, 0.2691, 0.3029, 0.27] ], dtype=np.float32)

data_LFR = np.array([[0.9966,1,  0.9979, 1,      1,      0.9922, 1,      1,      0.993,  1 ],
                [0.9865, 0.9974, 0.9886, 0.9767, 0.9851, 0.9851, 0.9762, 0.9721, 0.9813, 0.9767],
                [0.7727, 0.6912, 0.7114, 0.7088, 0.7226, 0.6925, 0.5662, 0.7793, 0.7627, 0.6768],
                [0.2992, 0.3175, 0.2953, 0.3272, 0.1301, 0.2192, 0.0245, 0.307,  0.3133, 0.3118],
                [0.1622, 0.227,  0.2273, 0.2431, 0.2096, 0.2339, 0.0133, 0.2483, 0.2214, 0.2259] ], dtype=np.float32)


x=np.array([0.1,0.3,0.5,0.7,0.9])

data_LFREA = np.transpose(data_LFREA)
y_LFREA = data_LFREA.mean(axis=0)

data_LFR = np.transpose(data_LFR)
y_LFR = data_LFR.mean(axis=0)

# Plot a line between the means of each dataset
plt.plot(x, y_LFREA,color='#003f5c', linewidth=3 ,label="SAS_LPA")
plt.plot(x, y_LFR,color='#ffa600', linewidth=3,label="LPA")

# locs, labels = plt.xticks() 

plt.boxplot(data_LFREA, positions=x,widths = 0.06,showfliers=True, manage_ticks=False)
plt.boxplot(data_LFR, positions=x, widths = 0.06, patch_artist = True,showfliers=True, manage_ticks=False)

plt.xlabel('μ',fontsize=25)
plt.ylabel('NMI',fontsize=25)
plt.legend(fontsize=22)
plt.grid(linestyle='dotted')
plt.show()