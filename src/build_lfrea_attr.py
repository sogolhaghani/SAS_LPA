import pandas as pd
import numpy as np
import networkx as nx

base_path =  '/home/sogol/py-workspace/community_detection_1/data/syn-LFREA/miu'
miu = '01'
def createAttrLFREA(base_path , miu ):  
    edges = pd.read_csv((base_path+ miu +'/network.dat') , sep="	", header=None).to_numpy()
    nodesAttrs = pd.read_csv((base_path+ miu +'/network_attributes.dat' ) , sep="  ", header=None).to_numpy()
    communities = pd.read_csv((base_path+ miu +'/community.dat') , sep="	", header=None).to_numpy()

    adjustmentMatrix = np.zeros((np.amax(edges),np.amax(edges) ))
    for i in range(0, np.amax(edges)):
        adjustmentMatrix[(edges[i][0] -1 ) ,(edges[i][1] -1) ] = 1

    G = nx.from_numpy_array(adjustmentMatrix)

    a_dic = {i : nodesAttrs[i,1:] for i in range(0, len(nodesAttrs) ) }
    nx.set_node_attributes(G, a_dic, 'attr_vec')

    c_dic = {i : communities[i,1] for i in range(0, len(communities) ) }
    nx.set_node_attributes(G, c_dic, 'community')

    return G  




