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