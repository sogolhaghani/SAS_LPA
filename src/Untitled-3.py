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
from networkx.algorithms.community import greedy_modularity_communities
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

# %%
# data="WebKB_univ"
# data="citeseer"
data = "polblog"
# data = "cora"
data_path = "/home/sogol/py-workspace/community_detection_1/data/"+data
S, S_ori, X, true_clus, flag, A_ori = build_graph.build_graph(data_path)

# %% [markdown]
# ## Convert to NetworkX Graph

# %%
G = nx.Graph(S_ori)
a_dic = {i : A_ori[i] for i in range(0, len(A_ori) ) }
nx.set_node_attributes(G, a_dic, 'attr_vec')

# %% [markdown]
# ## Calculate Node Similarity

# %%
_score = {}
for e in G.edges:
    n_0_v = G.nodes[e[0]]['attr_vec']
    n_1_v = G.nodes[e[1]]['attr_vec']
    _score.update( {e : {'weight' : simple_matching_coeffitient.SMC(n_0_v , n_1_v)}})
    # _score.update( {e : {'weight' : jaccard_score(n_0_v , n_1_v)}})

nx.set_edge_attributes(G, _score)
# color=nx.get_edge_attributes(G,'weight')
# for e in G.edges:
#     print(color[e])

# %% [markdown]
# ## Calculate Node Laplacian Centrality and applying LPA

# %%
nodes_cent = LaplaceDynamic.lap_cent_weighted(G)
dic_lc = {i : nodes_cent[i] for i in range(0, len(nodes_cent) ) }
nx.set_node_attributes(G, dic_lc, 'weight')
SGL_KB_lpa.asyn_lpa_communities(G)
# nx.draw(G)
# plt.draw()
# plt.show()
c = list(greedy_modularity_communities(G))
print(c[0])
# %%


