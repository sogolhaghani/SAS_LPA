# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Run on Real Dataset
# %% [markdown]
# # imports

# %%
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
# from sklearn.preprocessing import scale

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
data = "cora"
data_path = "/home/sogol/py-workspace/SAS_LPA/data/"+data
S, S_ori, X, true_clus, flag, A_ori = build_graph.build_graph(data_path)


# %% [markdown]
# ## Convert to NetworkX Graph
# 
# ### select max connected component
# 

# %%
G = nx.Graph(S_ori)
for e in G.edges:
    if e[0] == e[1]: 
        G.remove_edge(e[0],e[1])


c_dic = {i : n for i , n in enumerate(true_clus )}
orig_lister_dic = {n : [] for  n in set(true_clus )}
for i , n in enumerate(true_clus ):
    orig_lister_dic.setdefault(n, []).append(i) 

nx.set_node_attributes(G, c_dic, 'club')
GMax = max(nx.connected_components(G), key=len)
G = G.subgraph(GMax)

print('number of nodes Max connected Component : ' , len(G.nodes))
print('number of edges Max connected Component : ' , len(G.edges))

A_ori_copy = A_ori[list(G.nodes), :]
col = []
for i in range(0 ,A_ori_copy.shape[1] ):
    if sum(A_ori_copy[:,i]) > 0:
        col.append(i)
A_ori = A_ori[:, col]       
a_dic = {i : A_ori[i] for i in range(0, len(A_ori) ) }
nx.set_node_attributes(G, a_dic, 'attr_vec')


# # %% [markdown]
# # ## Calculate Node Similarity

_score = {}
alpha = 0.6
for e in G.edges:
    n_0_v = G.nodes[e[0]]['attr_vec']
    n_1_v = G.nodes[e[1]]['attr_vec']
    # _score.update( {e : {'weight' : simple_matching_coeffitient.SMC(n_0_v , n_1_v)}})
    # _score.update( {e : {'weight' : cosine_similarity([n_0_v] , [n_1_v])}})
    if G.degree(e[1]) ==1 or G.degree(e[0])==1 :
        weight = -1
    elif simple_matching_coeffitient.SMC_1(n_0_v , n_1_v) == 0:
        weight = 0
    else :
        weight = (alpha) * simple_matching_coeffitient.SMC_1(n_0_v , n_1_v) + (1-alpha) *[p for u, v, p in nx.jaccard_coefficient(G, [e])][0]
    _score.update( {e : {'weight' :weight}})


nx.set_edge_attributes(G, _score)

# %% [markdown]
# ## Calculate Node Laplacian Centrality and applying LPA

# %%
nodes_cent = LaplaceDynamic.lap_cent_weighted(G)
dic_lc = {i : np.ceil(nodes_cent[i]) for i in nodes_cent }
nx.set_node_attributes(G, dic_lc, 'weight')
G, communities =SGL_KB_lpa.asyn_lpa_communities(G)

# %% [markdown]
# ## Evaluation

# %%
v_orig, v_pred = util.convertToResultVec(G, communities, orig_lister_dic)
nmi = normalized_mutual_info_score(v_orig , v_pred)
acc = accuracy_score(v_orig , v_pred)
ari = adjusted_rand_score(v_orig , v_pred)
f_1_macro = f1_score(v_orig , v_pred, average='macro')
f_1_micro = f1_score(v_orig , v_pred, average='micro')
f_1_weighted = f1_score(v_orig , v_pred, average='weighted')
mod = community.modularity(nx.get_node_attributes(G, 'com'),G)
entropy = util.avg_entropy(v_pred, v_orig)
print('Num original Community -> ', len(set(v_orig)))
print('Num Predicted Community -> ', len(set(v_pred)))
print('NMI -> %8.2f %% '%(nmi*100))
print('ACC -> %8.2f %% '%(acc*100))
print('ARI -> %8.2f '%(ari))

print('f1_macro -> %8.2f '%(f_1_macro))
print('f1_micro -> %8.2f '%(f_1_micro))
print('f1 -> %8.2f '%(f_1_weighted))
print('Modularity ->  %8.2f' %mod)
print('Entropy ->  %8.2f' %entropy)

# %% [markdown]
# ## Graph

# %%
# pos = nx.spring_layout(G) #calculate position for each node
# nx.draw(G,pos, with_labels=True , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
# # nx.draw(G,pos, with_labels=True, labels=nx.get_node_attributes(G,'weight') , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
# color_list = list(mcolors.CSS4_COLORS)
# shuffle(color_list)
# i=0
# for x in communities:
#     nx.draw_networkx_nodes(G,pos, nodelist=communities[x], node_color=color_list[i%len(color_list)])
#     i+=1
# for e in G.nodes:
#     x, y = pos[e]  
#     plt.text(x,y+0.005 ,s=np.ceil(G.nodes[e]['weight']), horizontalalignment='center',fontdict={'size': 6})        
# # for e in G.edges:
# #     x1, y1 = po s[e[0]]  
# #     x2, y2 = pos[e[1]]  
# #     plt.text((x1 + x2) /2,(y1 +y2)/2 ,s=np.ceil(G.edges[e]['weight']), horizontalalignment='center')       
# plt.draw()
# plt.show()





# pos = nx.spring_layout(G) #calculate position for each node
# nx.draw(G,pos, with_labels=True , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
# # nx.draw(G,pos, with_labels=True, labels=nx.get_node_attributes(G,'weight') , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
# color_list = list(mcolors.CSS4_COLORS)
# shuffle(color_list)
# i=0
# for x in orig_lister_dic:
#     nx.draw_networkx_nodes(G,pos, nodelist=orig_lister_dic[x], node_color=color_list[i%len(color_list)])
#     i+=1
# plt.draw()
# plt.show()


# %%


