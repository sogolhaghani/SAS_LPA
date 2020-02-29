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

vec_orig_community = []
vec_pred_community = []
clubDict = nx.get_node_attributes(G,'club')
clubKeys = set(clubDict.values())
clubKeys = list(clubKeys)
clubKeys.sort()
comKeys = set(communities.keys() )
comKeys = list(comKeys)
comKeys.sort()
trans_orig = {n : i for i, n in enumerate(clubKeys) }
trans_pred = {n : i for i, n in enumerate(comKeys) }


for  i, n  in enumerate(G):
    orig = G.nodes[n]['club']    
    prec = G.nodes[n]['com']
    vec_orig_community.append(trans_orig[orig])
    vec_pred_community.append(trans_pred[prec])

nmi = normalized_mutual_info_score(vec_orig_community , vec_pred_community)
print(nmi)


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


