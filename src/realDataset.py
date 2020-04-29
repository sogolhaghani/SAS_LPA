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
from datetime import datetime

def preprocess_graph(data):
    data_path = "/home/sogol/py-workspace/SAS_LPA/data/"+data
    S, S_ori, X, true_clus, flag, A_ori = build_graph.build_graph(data_path)
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
    return G ,orig_lister_dic


def calculate_edge_weight(G):
    _score = {}
    alpha =1

    for e in G.edges:
        n_0_v = G.nodes[e[0]]['attr_vec']
        n_1_v = G.nodes[e[1]]['attr_vec']
        # if G.degree(e[1]) ==1 or G.degree(e[0])==1 or simple_matching_coeffitient.SMC_1(n_0_v , n_1_v)== 0:
        #     weight = -0.5
        # else :
        # weight = (alpha) * simple_matching_coeffitient.SMC(n_0_v , n_1_v) + (1-alpha) *[p for u, v, p in nx.adamic_adar_index(G, [e])][0]
        # weight = (alpha) * simple_matching_coeffitient.SMC(n_0_v , n_1_v) + (1-alpha) *[p for u, v, p in nx.jaccard_coefficient(G, [e])][0]
        weight = (alpha) * simple_matching_coeffitient.SMC(n_0_v , n_1_v) 
        _score.update( {e : {'weight' :weight}})
    nx.set_edge_attributes(G, _score)

def calculate_node_weight(G):
    nodes_cent = LaplaceDynamic.lap_cent_weighted(G)
    dic_lc = {i : nodes_cent[i] for i in nodes_cent }
    nx.set_node_attributes(G, dic_lc, 'weight')

def evaulate(v_orig, v_pred,time):
    nmi = normalized_mutual_info_score(v_orig , v_pred)
    acc = accuracy_score(v_orig , v_pred)
    # ari = adjusted_rand_score(v_orig , v_pred)
    # f_1_macro = f1_score(v_orig , v_pred, average='macro')
    # f_1_micro = f1_score(v_orig , v_pred, average='micro')
    f_1_weighted = f1_score(v_orig , v_pred, average='weighted')
    # mod = community.modularity(nx.get_node_attributes(G, 'com'),G)
    # entropy = util.avg_entropy(v_pred, v_orig)
    # attr_entropy  = util.entropy_attr_real(G,communities)
    # _density  = util.density(G,communities)
    _result =[]
    _result.append('Num original Community\t\t%s'%(len(set(v_orig))))
    _result.append('Num Predicted Community\t\t%s' %(len(set(v_pred))))
    _result.append('NMI\t\t\t\t%1.4f '%(nmi))
    _result.append('ACC\t\t\t\t%1.4f '%(acc))
    # _result.append('ARI\t\t\t\t%1.4f'%(ari))
    # _result.append('f1_macro\t\t\t%1.4f '%(f_1_macro))
    # _result.append('f1_micro\t\t\t%1.4f '%(f_1_micro))
    _result.append('f1\t\t\t\t%1.4f '%(f_1_weighted))
    # _result.append('Modularity\t\t\t%1.4f' %mod)
    # _result.append('Entropy\t\t\t\t%1.4f' %entropy)
    # _result.append('Attribute Entropy\t\t%s' %attr_entropy)
    # _result.append('Density\t\t\t\t%s' %_density)
    _result.append('Time\t\t\t\t%s' %time)
    
    for x in _result:
        print(x)


def drawGraph(G,communities,orig_lister_dic):
    pos = nx.spring_layout(G, weight=None) #calculate position for each node
    nx.draw(G,pos, with_labels=True , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
    # nx.draw(G,pos, with_labels=True, labels=nx.get_node_attributes(G,'weight') , font_weight='light', node_size= 280, width= 0.5, font_size= 'xx-small')
    color_list = list(mcolors.CSS4_COLORS)
    shuffle(color_list)
    i=0
    # for x in communities:
    #     nx.draw_networkx_nodes(G,pos, nodelist=communities[x], node_color=color_list[i%len(color_list)])
    #     i+=1
    for x in orig_lister_dic:
        nx.draw_networkx_nodes(G,pos, nodelist=util.getKeysByValue(nx.get_node_attributes(G,'club'), x), node_color=color_list[i%len(color_list)])
        i+=1
    # for e in G.nodes:
    #     x, y = pos[e]  
    #     plt.text(x,y+0.005 ,s=G.nodes[e]['club'], horizontalalignment='center',fontdict={'size': 8})              
    plt.draw()
    plt.show()



# data="WebKB_univ"
# data="citeseer"
# data = "polblog"
# data = "cora"
# data ="cornell"
# data ="texas"
# data = "washington"
data = "wisconsin"
G,orig_lister_dic = preprocess_graph(data)
now = datetime.now()
calculate_edge_weight(G)
# edgeT = datetime.now()
# print('Time calculate edge weight %s' %(edgeT - now) )
calculate_node_weight(G)
# nodeT = datetime.now()
# print('Time calculate node weight %s' %(nodeT - edgeT) )
G, communities =SGL_KB_lpa.asyn_lpa_communities(G)
# lpaT = datetime.now()
# print('Time LPA %s' %(lpaT - nodeT) )
v_orig, v_pred = util.convertToResultVec(G, communities, orig_lister_dic)
diff = datetime.now() - now
evaulate(v_orig, v_pred,diff)
# drawGraph(G, communities, orig_lister_dic)
