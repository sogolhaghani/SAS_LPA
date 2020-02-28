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
# from networkx.algorithms.community import LFR_benchmark_graph


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



# n = 250
# tau1 = 3
# tau2 = 1.5
# mu = 0.1
# G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=5, min_community=20, seed=10)
for e in G.edges:
    _score.update( {e : {'weight' : 1}})
nx.set_edge_attributes(G, _score)

# nx.set_node_attributes(G, listOfStr)
nodes_cent = LaplaceDynamic.lap_cent_weighted(G)
dic_lc = {i : np.ceil(nodes_cent[i]) for i in nodes_cent }
nx.set_node_attributes(G, dic_lc, 'weight')
G, communities =SGL_KB_lpa.asyn_lpa_communities(G)
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


