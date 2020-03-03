# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Example
# %% [markdown]
# # imports

# %%
import build_graph
import simple_matching_coeffitient
import LaplaceDynamic
import SGL_KB_lpa
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from random import shuffle
import numpy as np
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import jaccard_score


# from sklearn.metrics import jaccard_score
# from sklearn.metrics.pairwise import cosine_similarity

# %% [markdown]
# ## Choose data you would like to use
# ### Data statics are displayed
# #### S : adjacency matrix with prepoces
# #### S_ori : original adjacency matrix
# #### A : attribute matrix with preprocess
# #### clus : true cluster of nodes
# #### flag : with ground truth or without
# #### A_ori : original attribute matrix
# Cora O
# %%
# data="WebKB_univ"
data="citeseer"
# data = "polblog"
# data = "cora"
data_path = "/home/sogol/py-workspace/community_detection_1/data/"+data
S, S_ori, X, true_clus, flag, A_ori = build_graph.build_graph(data_path)

# %% [markdown]
# ## Convert to NetworkX Graph

# %%
G = nx.Graph(S_ori)
a_dic = {i : A_ori[i] for i in range(0, len(A_ori) ) }
c_dic = {i : n for i , n in enumerate(true_clus )}
cc_dic = {n : [] for  n in set(true_clus )}
for i , n in enumerate(true_clus ):
    cc_dic.setdefault(n, []).append(i) 

nx.set_node_attributes(G, a_dic, 'attr_vec')
nx.set_node_attributes(G, c_dic, 'club')

# %% [markdown]
# ## Calculate Node Similarity

# %%
_score = {}
for e in G.edges:
    n_0_v = G.nodes[e[0]]['attr_vec']
    n_1_v = G.nodes[e[1]]['attr_vec']
    # _score.update( {e : {'weight' : simple_matching_coeffitient.SMC(n_0_v , n_1_v)}})
    _score.update( {e : {'weight' : jaccard_score(n_0_v , n_1_v)}})

nx.set_edge_attributes(G, _score)

GMax = max(nx.connected_components(G), key=len)
G = G.subgraph(GMax)



# color=nx.get_edge_attributes(G,'weight')
# for e in G.edges:
#     print(color[e])

# %% [markdown]
# ## Calculate Node Laplacian Centrality and applying LPA

# %%
nodes_cent = LaplaceDynamic.lap_cent_weighted(G)
dic_lc = {i : np.ceil(nodes_cent[i]) for i in nodes_cent }
nx.set_node_attributes(G, dic_lc, 'weight')
G, communities =SGL_KB_lpa.asyn_lpa_communities(G)

def intersection(lst1, lst2): 
    return [item for item in lst1 if item in lst2] 

trans_orig = {}
trans_pred = {}
i = 0
xx = sorted(communities, key=lambda k: len(communities[k]), reverse=True)
for t in xx:
    d = communities[t]
    _max = 0
    _max_label = ''
    for v in cc_dic:
        ds = cc_dic[v]
        if len(intersection(d, ds)) > _max:
            _max = len(intersection(d, ds))
            _max_label = v
    if _max > 0:
        trans_orig[i] = cc_dic[_max_label]
        cc_dic.pop(_max_label, None)
    trans_pred[i] = d
    i +=1

for t in cc_dic:
    trans_orig[i] = cc_dic[t]   
    i+=1

vec_orig_community = []
vec_pred_community = []

def get_key(val, my_dict): 
    for key, value in my_dict.items(): 
         if val in value: 
             return key 
  
    return "key doesn't exist"

for i, n  in enumerate(G):
    vec_orig_community.append(get_key(n, trans_orig))
    vec_pred_community.append(get_key(n, trans_pred))

nmi = normalized_mutual_info_score(vec_orig_community , vec_pred_community)
acc = accuracy_score(vec_orig_community , vec_pred_community)
print(nmi, acc)


# pos = nx.spring_layout(G) #calculate position for each node

# nx.draw(G,pos, with_labels=True, labels=nx.get_node_attributes(G,'weight') , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')

# color_list = list(mcolors.CSS4_COLORS)
# shuffle(color_list)

# i=0
# for x in communities:
#     nx.draw_networkx_nodes(G,pos, nodelist=communities[x], node_color=color_list[i])
#     i+=1


# plt.draw()
# plt.show()
# c = list(greedy_modularity_communities(G))
# print(c[0])
# %%


