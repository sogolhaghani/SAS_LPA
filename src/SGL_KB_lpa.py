"""
Label propagation community detection algorithms.
"""
import networkx as nx
import random
from scipy import stats
import numpy as np
import simple_matching_coeffitient

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
    
    if np.max(x[:,1]) == 1:
        index = np.argmax(x[:,2])
        # index = random.choice(list(enumerate(x)))[0]

    else:
        index = np.argmax(x[:,1]) 
    # index = np.argmax(x[:,2])      
    neighbors = np.array(neighbors)
    return np.where( neighbors[:, 1] == x[index][0])[0][0]


def asyn_lpa_communities(G, iter = 1, loggable = False):
    l = [[n, i, G.nodes[n]['weight']] for i, n in enumerate(G)]
    labels  = np.asarray(l)
    # labels = labels[labels[:,2].argsort()[::1]]
    for i in range(0, iter):
        np.random.shuffle(labels)     
        if loggable:
            print('\n Iteration %s \n ' %(i + 1))

        x = 0
        for node_info in labels:
            x+=1
            neighbors = [   [n, 
                            labels[ np.where( labels[:, 0] ==n)[0][0]][1],  
                            labels[np.where( labels[:, 0] ==n)[0][0]][2] ] for n in G.neighbors(node_info[0]) 
                        ] 
            if len(neighbors) == 0 :
                continue
            selected_neigh = findSelectedNeigh(neighbors)
            node_info[1] = neighbors[selected_neigh][1]
            if loggable:
                print('%s\t%s\t%s\t%8.2f' %(x,node_info[0] +1  ,  node_info[1]+ 1, node_info[2]))
        if loggable:    
            for node_info in labels:
                print('node %s, label %s, centrality : %s' %(node_info[0] + 1 ,node_info[1] + 1,node_info[2]))        

    community_node_dic = {}
    for node in list(G.nodes):
        row = labels[labels[:,0]== node]
        community = labels[labels[:,1]== row[0][1]]
        community = community[:,0]
        community_node_dic[node] = {'community' :community}
        community_node_dic[node] = {'com' :row[0][1]}
    nx.set_node_attributes(G, community_node_dic)
    community_dic = {}
    for x in labels[:,1]:
        community = labels[labels[:,1]== x]
        community = community[:,0]
        community_dic[x] = community
    return G, community_dic