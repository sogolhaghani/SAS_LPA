"""
Label propagation community detection algorithms.
"""
import networkx as nx
import random
from scipy import stats
import numpy as np

def findSelectedNeigh(neighbors):
    x = np.array([neighbors[0][1], 1,neighbors[0][2] ], ndmin=2)
    for node_info in neighbors[1:]:
        if node_info[1] in x[:, 0]:
            index = np.where( x[:, 0] == node_info[1])[0]
            x[index,1] = x[index,1] + 1
            x[index,2] = node_info[2] + x[index,2]
        else:
            t = np.array([node_info[1] , 1 , node_info[2]])
            x =np.vstack([x, t])
    
    index = np.argmax(x[:,2])
    neighbors = np.array(neighbors)
    return np.where( neighbors[:, 1] == x[index][0])[0][0]


def asyn_lpa_communities(G, iter = 5):
    l = [[n, i, G.nodes[n]['weight']] for i, n in enumerate(G)]
    
    labels  = np.asarray(l)
    labels = labels[labels[:,2].argsort()[::-1]]
    for i in range(0, iter):
        for node_info in labels:
            neighbors = [   [n, 
                            labels[ np.where( labels[:, 0] ==n)[0][0]][1],  
                            labels[np.where( labels[:, 0] ==n)[0][0]][2] ] for n in G.neighbors(node_info[0]) 
                        ] 
            if len(neighbors) == 0 :
                continue
            selected_neigh = findSelectedNeigh(neighbors)
            node_info[1] = neighbors[selected_neigh][1]
    print(set(labels[:,1]))
            
           




