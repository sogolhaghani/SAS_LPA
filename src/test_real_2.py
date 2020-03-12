# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Run on Real Dataset
# %% [markdown]
# # imports

# %%
import data_loader
import util
import simple_matching_coeffitient
import LaplaceDynamic
import laplacian_centrality
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

# %% [markdown]
# ## Choose data you would like to use
# ### Data statics are displayed
# #### S : adjacency matrix with prepoces
# #### S_ori : original adjacency matrix
# #### A : attribute matrix with preprocess
# #### clus : true cluster of nodes
# #### flag : with ground truth or without
# #### A_ori : original attribute matrix

# %%
# data="WebKB_univ"
# data="citeseer"
# data = "polblog"
# data = "cora"
# data_path = "/home/sogol/py-workspace/SAS_LPA/data/"+data
features, labels, adj, graph = data_loader.load_data()


# %% [markdown]
# ## Convert to NetworkX Graph
# 
# ### select max connected component
# 
a_dic ={}
for i , n in enumerate(graph):
    x = features[0][np.where( features[0][:, 0] == n)][:,1]
    y = np.zeros(features[2][1])
    np.put(y, x, 1, mode='clip')
    a_dic[n] = y
c_dic = {i : np.where( labels[i] == 1)[0] for i in range(0, len(labels) )}

orig_lister_dic = {n : [] for  n in range(0,labels.shape[1] )}
for i in range(0, len(labels) ):
    n= np.where( labels[i] == 1)
    if len(n[0]) > 0:
        orig_lister_dic.setdefault(n[0][0], []).append(i) 


# %%
G = graph
# a_dic = {i : A_ori[i] for i in range(0, len(A_ori) ) }
# c_dic = {i : n for i , n in enumerate(true_clus )}
# orig_lister_dic = {n : [] for  n in set(true_clus )}
# for i , n in enumerate(true_clus ):
#     orig_lister_dic.setdefault(n, []).append(i) 

nx.set_node_attributes(G, a_dic, 'attr_vec')
nx.set_node_attributes(G, c_dic, 'club')
GMax = max(nx.connected_components(G), key=len)
G = G.subgraph(GMax)
print('number of nodes Max connected Component : ' , len(G.nodes))
print('number of edges Max connected Component : ' , len(G.edges))

# %% [markdown]
# ## Calculate Node Similarity

# %%
_score = {}
alpha = 0.5
for e in G.edges:
    n_0_v = G.nodes[e[0]]['attr_vec']
    n_1_v = G.nodes[e[1]]['attr_vec']
    # _score.update( {e : {'weight' : simple_matching_coeffitient.SMC(n_0_v , n_1_v)}})
    # _score.update( {e : {'weight' : cosine_similarity([n_0_v] , [n_1_v])}})
    weight = (alpha) * simple_matching_coeffitient.SMC_2(n_0_v , n_1_v) + (1-alpha) *jaccard_score(n_0_v , n_1_v, average='weighted')
    _score.update( {e : {'weight' : weight}})
nx.set_edge_attributes(G, _score)

# %% [markdown]
# ## Calculate Node Laplacian Centrality and applying LPA

# %%
# nodes_cent = laplacian_centrality.lap_cent_weighted(G)
nodes_cent = LaplaceDynamic.lap_cent_weighted(G, norm=True)
dic_lc = {i : np.ceil(nodes_cent[i]) for i in nodes_cent }
nx.set_node_attributes(G, dic_lc, 'weight')
G, communities =SGL_KB_lpa.asyn_lpa_communities(G)

# # %% [markdown]
# # ## Evaluation

# # %%
v_orig, v_pred = util.convertToResultVec(G, communities, orig_lister_dic)
nmi = normalized_mutual_info_score(v_orig , v_pred)
acc = accuracy_score(v_orig , v_pred)
ari = adjusted_rand_score(v_orig , v_pred)
f_1_macro = f1_score(v_orig , v_pred, average='macro')
f_1_micro = f1_score(v_orig , v_pred, average='micro')
f_1_weighted = f1_score(v_orig , v_pred, average='weighted')
print('Num original Community -> ', len(set(v_orig)))
print('Num Predicted Community -> ', len(set(v_pred)))
print('NMI -> %8.2f %% '%(nmi*100))
print('ACC -> %8.2f %% '%(acc*100))
print('ARI -> %8.2f '%(ari))

print('f1_macro -> %8.2f '%(f_1_macro))
print('f1_micro -> %8.2f '%(f_1_micro))
print('f1 -> %8.2f '%(f_1_weighted))

# partition = community.best_partition(G)



# %% [markdown]
# ## Graph

pos = nx.spring_layout(G) #calculate position for each node
# nx.draw(G,pos, with_labels=True , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
nx.draw(G,pos, with_labels=True, labels=nx.get_node_attributes(G,'weight') , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
color_list = list(mcolors.CSS4_COLORS)
shuffle(color_list)
i=0
for x in communities:
    nx.draw_networkx_nodes(G,pos, nodelist=communities[x], node_color=color_list[i%len(color_list)])
    i+=1
plt.draw()
plt.show()


# %%


