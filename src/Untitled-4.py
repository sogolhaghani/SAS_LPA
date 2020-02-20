# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Example With Synthetic
# %% [markdown]
# # imports

# %%
import build_lfr_attr
import simple_matching_coeffitient
import LaplaceDynamic
import SGL_KB_lpa
import networkx as nx

# %% [markdown]
# ## Create LFR_atrr

# %%
f = '/home/sogol/py-workspace/community_detection_1/data/synthatic/'
G = build_lfr_attr.createAttrLFR(base_path = f , miu='1')

# %% [markdown]
# ## Calculate Node Similarity

# %%
_score = {}
for e in G.edges:
    n_0_v = G.nodes[e[0]]['attr_vec']
    n_1_v = G.nodes[e[1]]['attr_vec']
    # _score.update( {e : {'weight' : jaccard_score(n_0_v , n_1_v)}})
    _score.update( {e : {'weight' : simple_matching_coeffitient.SMC(n_0_v , n_1_v)}})
nx.set_edge_attributes(G, _score)

# %% [markdown]
# ## Calculate Node Laplacian Centrality and applying LPA

# %%
nodes_cent = LaplaceDynamic.lap_cent_weighted(G, norm=True)
dic_lc = {i : nodes_cent[i] for i in range(0, len(nodes_cent) ) }
nx.set_node_attributes(G, dic_lc, 'weight')
SGL_KB_lpa.asyn_lpa_communities(G)


# %%


