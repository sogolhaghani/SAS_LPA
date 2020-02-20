import pandas as pd
import numpy as np
import networkx as nx

def createAttrLFR(base_path , miu ):  
    edges = pd.read_csv((base_path + 'LFRmiu' + miu +'.csv') , header=None).to_numpy()
    nodesAttrs = pd.read_csv((base_path + 'ATTRmiu' + miu +'.csv') , header=None).to_numpy()
    communities = pd.read_csv((base_path + 'groundmiu' + miu +'.csv') , header=None).to_numpy()

    adjustmentMatrix = np.zeros((np.amax(edges),np.amax(edges) ))
    for i in range(0, np.amax(edges)):
        adjustmentMatrix[(edges[i][0] -1 ) ,(edges[i][1] -1) ] = 1

    G = nx.from_numpy_array(adjustmentMatrix)

    a_dic = {i : nodesAttrs[i] for i in range(0, len(nodesAttrs) ) }
    nx.set_node_attributes(G, a_dic, 'attr_vec')

    c_dic = {i : communities[i] for i in range(0, len(communities) ) }
    nx.set_node_attributes(G, c_dic, 'comm_vec')

    return G  

