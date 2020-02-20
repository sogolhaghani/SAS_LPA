# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Example
# %% [markdown]
# # imports

# %%
import build_graph
import laplacian_centrality
import LaplaceDynamic
import SGL_KB_lpa
import networkx as nx
# %%
listOfStr = ['1' , '2' , '3' , '4' , '5' , '6' ,'7' , '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
Gp = nx.Graph()
ed = [('1','2',0.41),
('1','3',0.42),
('3','4',0.42),
('4','5',0.43),
('5','6',0.46),
('6','7',0.49),
('6','8',0.46),
('7','8',0.4),
('7','5',0.5),
('7','9',0.54),
('8','9',0.5),
('5','9',0.63),
('4','9',0.5),
('3','9',0.5),
('1','9',0.59),
('2','8',0.39),
('1','5',0.46),
('6','11',0.46),
('6','10',0.49),
('6','12',0.45),
('13','12',0.39),
('10','12',0.4),
('16','12',0.53),
('16','10',0.54),
('16','11',0.63),
('16','13',0.49),
('16','18',0.53),
('16','15',0.59),
('16','14',0.54),
('11','14',0.49),
('15','14',0.49),
('17','14',0.32),
('17','18',0.32),
('13','18',0.39),
('15','18',0.43),
('15','11',0.5),
('10','11',0.5)
]
Gp.add_weighted_edges_from(ed)
xw = LaplaceDynamic.lap_cent_weighted(Gp, norm=False)
# dic_lc = { listOfStr[i] : xw[i] for i in range(0, len(listOfStr))}
print(xw)
nx.set_node_attributes(Gp, xw, 'weight')
SGL_KB_lpa.asyn_lpa_communities(Gp)
