"""
Label propagation community detection algorithms.
"""
import networkx as nx
import random
from scipy import stats
import numpy as np


#[docs]@py_random_state(2)
def asyn_lpa_communities(G):
    labels = {n: [i, G.node[n]['weight']] for i, n in enumerate(G)}
    for i in range(0, 50):
        print(i)
        keys =  list(labels.keys())
        random.shuffle(keys)
        for node_name in keys:
            nei_label_list =  [ labels[n][0] for n in G.neighbors(node_name) ]  
            if len(nei_label_list) == 0:
                continue  
            if len(nei_label_list) == len(set(nei_label_list)):
                max_cent = max([labels[x][1] for x in G.neighbors(node_name)])
                for x in G.neighbors(node_name):
                    if labels[x][1] == max_cent:
                        labels[node_name][0] = labels[x][0]
                        break
            else:
                temp = np.array([labels[x][0] for x in G.neighbors(node_name)])
                m = stats.mode(temp).mode
                mode_neigh_lc = []
                for z in m:
                    mode_neigh = list(filter(lambda x: z == labels[x][0], G.neighbors(node_name)))
                    mode_neigh_lc.append ((z ,  np.average([labels[x][1] for x in mode_neigh], axis=0)) ) 

                max_cent = max([x[1] for x in mode_neigh_lc])
                for ix in range(0, len(mode_neigh_lc)) :
                    if mode_neigh_lc[ix][1] == max_cent:
                        labels[node_name][0] = mode_neigh_lc[ix][0]
                        break
    print(set([ labels[key][0] for key in labels ]))
    print(len(set([ labels[key][0] for key in labels ])))




