import scipy.stats as stat
import numpy as np


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

    for i, n  in enumerate(G):
        vec_orig_community.append(get_key(n, trans_orig))
        vec_pred_community.append(get_key(n, trans_pred))
    return vec_orig_community, vec_pred_community