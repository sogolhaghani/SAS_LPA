import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])


fig, axs = plt.subplots(ncols=3,nrows= 2, constrained_layout=True)
#Citeseer
axs[0,0].plot(x,  np.array([ 0.3425, 0.3472, 0.3474,0.3454, 0.3453, 0.3456,0.3455, 0.3452, 0.3438, 0.3447, 0.3447]), color='#bc5090',linestyle='--', marker='o', label="NMI")
axs[0,0].plot(x,  np.array([ 0.0687, 0.1403, 0.1336, 0.1104, 0.1095, 0.1199, 0.1109, 0.1114, 0.0972, 0.1114, 0.1114]), color='#ffa600',linestyle='-', marker='*', label="ACC")   
axs[0,0].plot(x,  np.array([ 0.1174, 0.2093, 0.1995, 0.1701, 0.1688, 0.1882, 0.1712, 0.1721, 0.1567,0.1721, 0.1721 ]), color='#003f5c',linestyle='dotted', marker='+', label="F1")
axs[0,0].plot(x,  np.array([ 0.003224682994814,0.003281143041465,0.003279498551121,0.003271521224163,0.003261375018906,0.003259367741673,0.003255223300968,0.003255050230997,0.003256150324736,0.003255165908571,0.003255165908571]), color='orchid',linestyle='-.', marker='v', label="Entropy")  
axs[0,0].plot(x,  np.array([0.716739367502726,0.780534351145038,0.781897491821156,0.767720828789531,0.764449291166848,0.755452562704471,0.760087241003272,0.759814612868048,0.751363140676118,0.760087241003272,0.760087241003272]), color='royalblue',linewidth=2, marker='s', label="Density")                                            
axs[0,0].set_xlabel("", fontsize=16)
axs[0,0].set_ylabel("", fontsize=16)
axs[0,0].legend( fontsize=6)
axs[0,0].grid(linestyle='dotted')
axs[0,0].set_ylim([0,1])
axs[0,0].set_title("a",)


#cora
axs[0,1].plot(x,  np.array([ 0.427,  0.4269, 0.4229,0.4253, 0.4272, 0.428,0.4292, 0.4299, 0.4281,0.4298, 0.428 ]), color='#bc5090',linestyle='--', marker='o', label="NMI")
axs[0,1].plot(x,  np.array([ 0.2141, 0.2209, 0.2085, 0.2209, 0.2205, 0.2241,0.2294, 0.2278, 0.2237,0.2298, 0.229]), color='#ffa600',linestyle='-', marker='*', label="ACC")   
axs[0,1].plot(x,  np.array([ 0.2904, 0.3024, 0.2816,0.3037, 0.2952, 0.2957,0.2955, 0.2986, 0.2942,0.2984, 0.2976]), color='#003f5c',linestyle='dotted', marker='+', label="F1") 
axs[0,1].plot(x,  np.array([0.004730065058748,0.004760517290755,0.004761128285493,0.004770831065316,0.00478819345901,0.004804117412629,0.004812919811993,0.004801169875076,0.004806039223201,0.004808107521119,0.004806480307393]), color='orchid',linestyle='-.', marker='v', label="Entropy")  
axs[0,1].plot(x,  np.array([0.700335371868219,0.707240086802131,0.705267311106727,0.708226474649832,0.715131189583744,0.719274018544092,0.721444071809035,0.718682185835471,0.715131189583744,0.717695797987769,0.715723022292365]), color='royalblue',linewidth=2, marker='s', label="Density") 
axs[0,1].set_xlabel("", fontsize=16)
axs[0,1].set_ylabel("", fontsize=16)
axs[0,1].legend( fontsize=6)
axs[0,1].grid(linestyle='dotted')
axs[0,1].set_ylim([0,1])
axs[0,1].set_title("b")


#cornel
axs[0,2].plot(x,  np.array([0.1355,0.1269, 0.1292,0.1456,0.1456,0.1413,0.1497,0.1497,0.1497,0.1516,0.1497 ]), color='#bc5090',linestyle='--', marker='o', label="NMI")
axs[0,2].plot(x,  np.array([0.2678,0.4208,0.388,0.3716,0.3716,0.377,0.3825,0.3716,0.3825,0.3607,0.3661]), color='#ffa600',linestyle='-', marker='*', label="ACC")   
axs[0,2].plot(x,  np.array([0.292,0.3619,0.3404,0.3362,0.3362,0.3368,0.3522,0.3368,0.3522,0.3476,0.3496]), color='#003f5c',linestyle='dotted', marker='+', label="F1") 
axs[0,2].plot(x,  np.array([0.019315139804046,0.020299622352613,0.020166155676298,0.019999181811748,0.019999181811748,0.020100103323453,0.020050608126929,0.020050608126929,0.020050608126929,0.019714388306928,0.019718967885451]), color='orchid',linestyle='-.', marker='v', label="Entropy")  
axs[0,2].plot(x,  np.array([0.729241877256318,0.866425992779783,0.830324909747292,0.815884476534296,0.815884476534296,0.826714801444043,0.826714801444043,0.826714801444043,0.826714801444043,0.8014440433213,0.8014440433213]), color='royalblue',linewidth=2, marker='s', label="Density") 
axs[0,2].set_xlabel("", fontsize=16)
axs[0,2].set_ylabel("", fontsize=16)
axs[0,2].legend( fontsize=6)
axs[0,2].grid(linestyle='dotted')
axs[0,2].set_ylim([0,1])
axs[0,2].set_title("c")

#Texas
axs[1,0].plot(x,  np.array([0.141,0.0863,0.0823,0.1047,0.1047,0.1047,0.1047,0.1047,0.1047,0.1047,0.1047]), color='#bc5090',linestyle='--', marker='o', label="NMI")
axs[1,0].plot(x,  np.array([0.5246,0.5082,0.4918,0.4863,0.4863,0.4863,0.4863,0.4863,0.4863,0.4863,0.4863]), color='#ffa600',linestyle='-', marker='*', label="ACC")   
axs[1,0].plot(x,  np.array([0.4576,0.4197,0.4149,0.4179,0.4179,0.4179,0.4179,0.4179,0.4179,0.4179,0.4179]), color='#003f5c',linestyle='dotted', marker='+', label="F1") 
axs[1,0].plot(x,  np.array([0.018021060857805,0.017807073363184,0.017693409373896,0.017541711101573,0.017541711101573,0.017541711101573,0.017541711101573,0.017541711101573,0.017541711101573,0.017541711101573,0.017541711101573]), color='orchid',linestyle='-.', marker='v', label="Entropy")  
axs[1,0].plot(x,  np.array([0.881720430107527,0.946236559139785,0.931899641577061,0.917562724014337,0.917562724014337,0.917562724014337,0.917562724014337,0.917562724014337,0.917562724014337,0.917562724014337,0.917562724014337]), color='royalblue',linewidth=2, marker='s', label="Density") 

axs[1,0].set_xlabel("", fontsize=16)
axs[1,0].set_ylabel("", fontsize=16)
axs[1,0].legend( fontsize=6)
axs[1,0].grid(linestyle='dotted')
axs[1,0].set_ylim([0,1])
axs[1,0].set_title("d")

#Washington
axs[1,1].plot(x,  np.array([0.1227,0.1436,0.1436,0.1436,0.1436,0.1436,0.1436,0.1436,0.1436,0.1436,0.1436]), color='#bc5090',linestyle='--', marker='o', label="NMI")
axs[1,1].plot(x,  np.array([0.5023,0.493,0.493,0.493,0.493,0.493,0.493,0.493,0.493,0.493,0.493]), color='#ffa600',linestyle='-', marker='*', label="ACC")   
axs[1,1].plot(x,  np.array([0.3746,0.3804,0.3804,0.3804,0.3804,0.3804,0.3804,0.3804,0.3804,0.3804,0.3804]), color='#003f5c',linestyle='dotted', marker='+', label="F1") 
axs[1,1].plot(x,  np.array([0.019347759430481,0.019128492206559,0.019128492206559,0.019128492206559,0.019128492206559,0.019128492206559,0.019128492206559,0.019128492206559,0.019128492206559,0.019128492206559,0.019128492206559]), color='orchid',linestyle='-.', marker='v', label="Entropy")  
axs[1,1].plot(x,  np.array([0.975342465753425,0.961643835616438,0.961643835616438,0.961643835616438,0.961643835616438,0.961643835616438,0.961643835616438,0.961643835616438,0.961643835616438,0.961643835616438,0.961643835616438]), color='royalblue',linewidth=2, marker='s', label="Density")
axs[1,1].set_xlabel("", fontsize=16)
axs[1,1].set_ylabel("", fontsize=16)
axs[1,1].legend( fontsize=6)
axs[1,1].grid(linestyle='dotted')
axs[1,1].set_ylim([0,1])
axs[1,1].set_title("e")

#Wisconsin
axs[1,2].plot(x,  np.array([0.0791,0.0929,0.0929,0.1076,0.1108,0.1063,0.1063,0.1063,0.1094,0.1145,0.1145]), color='#bc5090',linestyle='--', marker='o', label="NMI")
axs[1,2].plot(x,  np.array([0.4542,0.4502,0.4502,0.4422,0.4462,0.4542,0.4542,0.4542,0.4223,0.4542,0.4542]), color='#ffa600',linestyle='-', marker='*', label="ACC")   
axs[1,2].plot(x,  np.array([0.3766,0.4049,0.4049,0.3992,0.4013,0.4078,0.4078,0.4078,0.3933,0.4058,0.4058]), color='#003f5c',linestyle='dotted', marker='+', label="F1") 
axs[1,2].plot(x,  np.array([0.020181686045521,0.020114705280071,0.020114705280071,0.020123566790496,0.020119584095699,0.020093968623024,0.020093968623024,0.020093968623024,0.020026543824629,0.020131274889189,0.020131274889189]), color='orchid',linestyle='-.', marker='v', label="Entropy")  
axs[1,2].plot(x,  np.array([0.9,0.88,0.88,0.866666666666667,0.866666666666667,0.873333333333333,0.873333333333333,0.873333333333333,0.853333333333333,0.873333333333333,0.873333333333333]), color='royalblue',linewidth=2, marker='s', label="Density")
axs[1,2].set_xlabel("", fontsize=16)
axs[1,2].set_ylabel("", fontsize=16)
axs[1,2].legend( fontsize=6)
axs[1,2].grid(linestyle='dotted')
axs[1,2].set_ylim([0,1])
axs[1,2].set_title("f")


#polblog
# axs[2,1].plot(x,  np.array([0.7124,0.708,0.708,0.708,0.7122,0.7122,0.7122,0.7122,0.7122,0.7122,0.7122]), color='#bc5090',linestyle='--', marker='o', label="NMI")
# axs[2,1].plot(x,  np.array([0.9476,0.9459,0.9459,0.9459,0.9468,0.9468,0.9468,0.9468,0.9468,0.9468,0.9468]), color='#ffa600',linestyle='-', marker='*', label="ACC")   
# axs[2,1].plot(x,  np.array([0.9483,0.9475,0.9475,0.9475,0.9483,0.9483,0.9483,0.9483,0.9483,0.9483,0.9483]), color='#003f5c',linestyle='dotted', marker='+', label="F1") 
# axs[2,1].plot(x,  np.array([0.062999708734823,0.062905891982509,0.062905891982509,0.062905891982509,0.062903539797244,0.062903539797244,0.062903539797244,0.062903539797244,0.062903539797244,0.062903539797244,0.062903539797244]), color='orchid',linestyle='-.', marker='v', label="Entropy")  
# axs[2,1].plot(x,  np.array([0.926981835679057,0.926981835679057,0.926981835679057,0.926981835679057,0.926981835679057,0.926981835679057,0.926981835679057,0.926981835679057,0.926981835679057,0.926981835679057,0.926981835679057]), color='royalblue',linewidth=2, marker='s', label="Density")
# axs[2,1].set_xlabel("", fontsize=16)
# axs[2,1].set_ylabel("", fontsize=16)
# axs[2,1].legend( fontsize=6)
# axs[2,1].grid(linestyle='dotted')
# axs[2,1].set_ylim([0,1])
# axs[2,1].set_title("g")

# axs[2, 0].axis('off')
# axs[2, 2].axis('off')
plt.show()