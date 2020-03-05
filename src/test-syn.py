import build_graph
import util
import simple_matching_coeffitient
import LaplaceDynamic
import SGL_KB_lpa
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from random import shuffle
import numpy as np
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import f1_score
import community
import build_lfrea_attr


f = '/home/sogol/py-workspace/SAS_LPA/data/syn-LFREA/x'
G, orig_lister_dic = build_lfrea_attr.createAttrLFREA(base_path = f , miu='01')
GMax = max(nx.connected_components(G), key=len)
G = G.subgraph(GMax)
print('number of nodes Max connected Component : ' , len(G.nodes))
print('number of edges Max connected Component : ' , len(G.edges))
alpha = 0.5

_score = {}
for e in G.edges:
    n_0_v = G.nodes[e[0]]['attr_vec']
    n_1_v = G.nodes[e[1]]['attr_vec']
    # _score.update( {e : {'weight' : simple_matching_coeffitient.SMC(n_0_v , n_1_v)}})
    # _score.update( {e : {'weight' : cosine_similarity([n_0_v] , [n_1_v])}})
    weight = (alpha) * simple_matching_coeffitient.SMC(n_0_v , n_1_v) + (1-alpha) *jaccard_score(n_0_v , n_1_v, average='weighted')
    _score.update( {e : {'weight' : weight}})
nx.set_edge_attributes(G, _score)

nodes_cent = LaplaceDynamic.lap_cent_weighted(G)
dic_lc = {i : np.ceil(nodes_cent[i]) for i in nodes_cent }
nx.set_node_attributes(G, dic_lc, 'weight')
G, communities =SGL_KB_lpa.asyn_lpa_communities(G)

v_orig, v_pred = util.convertToResultVec(G, communities, orig_lister_dic)
nmi = normalized_mutual_info_score(v_orig , v_pred)
acc = accuracy_score(v_orig , v_pred)
ari = adjusted_rand_score(v_orig , v_pred)
f_1_macro = f1_score(v_orig , v_pred, average='macro')
f_1_micro = f1_score(v_orig , v_pred, average='micro')
f_1_weighted = f1_score(v_orig , v_pred, average='weighted')

print('\n RESULT')

print('Num original Community -> ', len(set(v_orig)))
print('Num Predicted Community -> ', len(set(v_pred)))
print('NMI -> %8.2f %% '%(nmi*100))
print('ACC -> %8.2f %% '%(acc*100))
print('ARI -> %8.2f '%(ari))

print('f1_macro -> %8.2f '%(f_1_macro))
print('f1_micro -> %8.2f '%(f_1_micro))
print('f1 -> %8.2f '%(f_1_weighted))

# partition = community.best_partition(G)


pos = nx.spring_layout(G) #calculate position for each node
nx.draw(G,pos, with_labels=True , font_weight='light', node_size= 280, width= 0.8, font_size= 'x-small', edgecolors=None)
# nx.draw(G,pos, with_labels=True, labels=nx.get_node_attributes(G,'attr_vec') , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
color_list = list(mcolors.CSS4_COLORS)
shuffle(color_list)
i=0
for x in communities:
    nx.draw_networkx_nodes(G,pos, nodelist=communities[x], node_color=color_list[i%len(color_list)])
    i+=1
for i, n in enumerate(G): 
    x, y = pos[n]   
    plt.text(x,y+0.03,s=G.nodes[n]['attr_vec'], horizontalalignment='center')    
plt.draw()
plt.show()
