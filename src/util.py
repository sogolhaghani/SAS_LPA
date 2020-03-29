import scipy.stats as stat
import numpy as np
import networkx as nx
from math import log10 , log2


def avg_entropy(predicted_labels, actual_labels):
    actual_labels_dict = {}
    predicted_labels_dict = {}
    for label in np.unique(actual_labels):
        actual_labels_dict[label] = np.nonzero(actual_labels==label)[0]
    for label in np.unique(predicted_labels):
        predicted_labels_dict[label] = np.nonzero(predicted_labels==label)[0]
    avg_value = 0
    N = len(predicted_labels)
    # store entropy for each community
    for label, items in predicted_labels_dict.items():
        N_i = float(len(items))
        p_i = []
        for label2, items2  in actual_labels_dict.items():
            common = set(items.tolist()).intersection(set(items2.tolist()))
            p_ij = float(len(common))/ N_i
            p_i.append(p_ij)
        entropy_i = stat.entropy(p_i)
        avg_value += entropy_i * (N_i / float(N))
    return avg_value  


def intersection(lst1, lst2): 
    return [item for item in lst1 if item in lst2] 

def get_key(val, my_dict): 
    for key, value in my_dict.items(): 
         if val in value: 
             return key 
  
    return -1

def convertToResultVec(G, communities, _orig_cluster_dic):
    orig_cluster_dic = {**_orig_cluster_dic}
    trans_orig = {}
    trans_pred = {}
    i = 0
    xx = sorted(communities, key=lambda k: len(communities[k]), reverse=True)
    for t in xx:
        d = communities[t]
        _max = 0
        _max_label = ''
        for v in orig_cluster_dic:
            ds = orig_cluster_dic[v]
            if len(intersection(d, ds)) > _max:
                _max = len(intersection(d, ds))
                _max_label = v
        if _max > 0:
            trans_orig[i] = orig_cluster_dic[_max_label]
            orig_cluster_dic.pop(_max_label, None)
        trans_pred[i] = d
        i +=1

    for t in orig_cluster_dic:
        trans_orig[i] = orig_cluster_dic[t]   
        i+=1

    vec_orig_community = []
    vec_pred_community = []
    # save_file('community-original_node_in_cluster.txt',trans_orig)
    # save_file('community-predicted_node_in_cluster.txt',trans_pred)

    for i, n  in enumerate(G):
        vec_orig_community.append(get_key(n, trans_orig))
        vec_pred_community.append(get_key(n, trans_pred))
    return vec_orig_community, vec_pred_community

def save_file(file_name, _list):
    with open(file_name, 'w') as filehandle:
        if type(_list) is dict:
            filehandle.writelines(("%s\n%s\n\n" %( place ,_list[place])) for place in _list)
        else:
            filehandle.writelines("%s\n" % place for place in _list)


def entropy_attr(graph, communities):
    _sum = 0
    _attr_dom = len(graph.nodes[0]['attr_vec'])
    attr = nx.get_node_attributes(graph,'attr_vec')
    attr_list = []
    for x in attr:
        attr_list.append(attr[x])
    attr_list = np.array(attr_list)
    domain =attr_list.max()
    entropy_ck = 0
    for _keyL in communities:
        _sumA = 0
        attr_Key = attr_list[np.array(communities[_keyL], int),:]
        entropy_A_ck = 0
        for i in range(0, _attr_dom):
            ix = attr_Key[:,i]
            entropy_ai_ck = 0
            for _d in range(0, domain):
                pKD  = len([i for i, x in enumerate(ix) if x == _d]) / len(ix)
                if pKD > 0:
                    entropy_ai_ck += pKD * log10(pKD)
            entropy_ai_ck *=(-1)
            entropy_A_ck += entropy_ai_ck
        entropy_ck += entropy_A_ck * (len(communities[_keyL]) / len(graph))
    return entropy_ck

def density(graph, communities):
    edge_ratio = 1 / len(graph.edges)
    _sumC = 0
    for _keyL in communities:
        _edges = graph.edges(communities[_keyL],default=0)
        _exact_edge = []
        for e in _edges:
            if e[0] in communities[_keyL] and e[1] in communities[_keyL]:
                _exact_edge.append(e)
        _sumC += len(_exact_edge)
    return edge_ratio * _sumC

    



