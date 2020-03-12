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
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import f1_score
import util


# listOfStr = {1: {'weight' : 84} , 
# 2: {'weight' : 26} , 
# 3: {'weight' : 25} , 
# 4 : {'weight' : 10}, 
# 5: {'weight' : 36} , 
# 6 : {'weight' : 18},
# 7: {'weight' : 20} , 
# 8: {'weight' : 58},
# 9: {'weight' : 43},
# 10: {'weight' : 10},
# 11: {'weight' : 22}, 
# 12: {'weight' : 45}, 
# 13: {'weight' : 16}, 
# 14: {'weight' : 6}}
# G = nx.Graph()
# ed = [
# (1,2), (2,5), (3,5), (4,5), (6,5), (6,7), (7,8), 
# (8,9), (9,10), (9,11), (9,12), (8,12), (12,11), (12,13), (14,13)
# ]
# G.add_edges_from(ed)


_score = {}
G = nx.karate_club_graph()
for e in G.edges:
    _score.update( {e : {'weight' : 1}})
nx.set_edge_attributes(G, _score)
nodes_cent = LaplaceDynamic.lap_cent_weighted(G)
dic_lc = {i : np.ceil(nodes_cent[i]) for i in nodes_cent }
nx.set_node_attributes(G, dic_lc, 'weight')
G, communities =SGL_KB_lpa.asyn_lpa_communities(G)
orig_lister_dic = {n : [] for  n in set(nx.get_node_attributes(G, 'club') )}
for i , n in enumerate(nx.get_node_attributes(G, 'club') ):
    orig_lister_dic.setdefault(n, []).append(i) 


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



pos = nx.spring_layout(G) #calculate position for each node

nx.draw(G,pos, with_labels=True, font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
# nx.draw(G,pos, with_labels=True, labels=nx.get_node_attributes(G,'weight') , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')

color_list = list(mcolors.CSS4_COLORS)
shuffle(color_list)

i=0
for x in communities:
    nx.draw_networkx_nodes(G,pos, nodelist=communities[x], node_color=color_list[i])
    i+=1


plt.draw()
plt.show()
# c = list(greedy_modularity_communities(G))
# print(c[0])
# %%


