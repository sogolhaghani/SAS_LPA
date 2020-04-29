import pandas as pd
import numpy as np
import networkx as nx

def createAttrLFREA(base_path , miu, v ):  
    edges = pd.read_csv((base_path+ miu + v +'/network.dat') , sep="	", header=None).to_numpy()
    nodesAttrs = pd.read_csv((base_path+ miu+v +'/network_attributes.dat' ) , sep="  ", header=None).to_numpy()
    communities = pd.read_csv((base_path+ miu+v +'/community.dat') , sep="	", header=None).to_numpy()
    
    adjustmentMatrix = np.zeros((np.amax(edges),np.amax(edges) ), dtype=np.float16)
    for i in range(0, len(edges)):
        adjustmentMatrix[(edges[i][0] -1 ) ,(edges[i][1] -1) ] = 1

    G = nx.from_numpy_array(adjustmentMatrix)

    a_dic = {i : nodesAttrs[i,1:] for i in range(0, len(nodesAttrs) ) }
    nx.set_node_attributes(G, a_dic, 'attr_vec')

    c_dic = {i : communities[i,1] for i in range(0, len(communities) ) }
    nx.set_node_attributes(G, c_dic, 'club')
    community_dic = {}
    for y in communities[:,1]:
        x= y-1
        community = communities[communities[:,1]== y]
        community = community[:,0]
        community_dic[x] = community -1
    return G , community_dic 




