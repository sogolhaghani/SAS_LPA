# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Example With Synthetic
# %% [markdown]
# # imports

# %%
# import build_lfr_attr
import build_lfrea_attr
import simple_matching_coeffitient
import LaplaceDynamic
import SGL_KB_lpa
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from random import shuffle
import numpy as np
from sklearn.metrics import jaccard_score
import laplacian_centrality

# %% [markdown]
# ## Create LFR_atrr

# %%
f = '/home/sogol/py-workspace/SAS_LPA/data/syn-LFREA/miu'
G = build_lfrea_attr.createAttrLFREA(base_path = f , miu='01')
GMax = max(nx.connected_components(G), key=len)
G = G.subgraph(GMax)
# %% [markdown]
# ## Calculate Node Similarity

# %%
_score = {}
for e in G.edges:
    n_0_v = G.nodes[e[0]]['attr_vec']
    n_1_v = G.nodes[e[1]]['attr_vec']
    # _score.update( {e : {'weight' : jaccard_score(n_0_v , n_1_v, average='macro')}})
    _score.update( {e : {'weight' : 1}})
    # _score.update( {e : {'weight' : simple_matching_coeffitient.SMC(n_0_v , n_1_v)}})
nx.set_edge_attributes(G, _score)

# %% [markdown]
# ## Calculate Node Laplacian Centrality and applying LPA

# %%
# nodes_cent = laplacian_centrality.lap_cent_weighted(G, norm=True)
nodes_cent = LaplaceDynamic.lap_cent_weighted(G, norm=True)
dic_lc = {i : np.ceil(nodes_cent[i]) for i in nodes_cent }
nx.set_node_attributes(G, dic_lc, 'weight')
G, communities =SGL_KB_lpa.asyn_lpa_communities(G)
pos = nx.spring_layout(G) #calculate position for each node

nx.draw(G,pos, with_labels=True , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
# nx.draw(G,pos, with_labels=True, labels=nx.get_node_attributes(G,'weight') , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')

color_list = list(mcolors.CSS4_COLORS)
shuffle(color_list)

i=0
for x in communities:
    nx.draw_networkx_nodes(G,pos, nodelist=communities[x], node_color=color_list[i])
    i+=1


plt.draw()
plt.show()

# %%


