# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Example
# %% [markdown]
# # imports

# %%
import build_graph
import laplacian_centrality
import SGL_KB_lpa
import networkx as nx
from sklearn.metrics import jaccard_score

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
nx.set_node_attributes(G, A_ori, 'attr_vec')
# D.nodes[0]['attr_vec'] test

# %% [markdown]
# ## Calculate Node Similarity

# %%
_score = {}
for e in G.edges:
    n_0_v = G.nodes[e[0]]['attr_vec']
    n_1_v = G.nodes[e[1]]['attr_vec']
    _score.update( {e : {'weight' : jaccard_score(n_0_v , n_1_v, average='macro')}})
nx.set_edge_attributes(G, _score)

# %% [markdown]
# ## Calculate Node Laplacian Centrality

# %%
nodes_cent = laplacian_centrality.lap_cent_weighted(G, norm=True)
dic_lc = {i : nodes_cent[i] for i in range(0, len(nodes_cent) ) }
nx.set_node_attributes(G, dic_lc, 'weight')
SGL_KB_lpa.asyn_lpa_communities(G)


# %%


