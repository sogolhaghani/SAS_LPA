from networkx import *
import time
import sys, getopt
import pickle
import os

def lap_energy(graph, degrees=None, weight='weight'):    
    if degrees is None:
        degrees = dict(graph.degree(weight=weight))
    d1 = sum(v**2 for i,v in degrees.items())
    wl = 0
    for i in graph.edges(data=True):
        wl += ((i[2].get(weight))**2)
    return [d1,2*wl]

def cw(graph, node, degrees=None, weight='weight'):
    neis = graph.neighbors(node)
    ne = graph [node]
    cw,sub = 0,0
    for i in neis:
        we = ne[i].get(weight)
        od = degrees [i]
        sub += -od**2 + (od - we)**2
        cw += we**2
    return [cw, sub]

def lap_cent_weighted(graph, nbunch=None, degrees=None, norm=False, weight='weight'):
    if nbunch is None:
        vs = graph.nodes()
    else:
        vs = nbunch
    if degrees is None:
         degrees = dict(graph.degree(weight=weight))
    if norm == True:
        fe = lap_energy(graph, degrees=degrees, weight=weight)
        den = float(fe[0]+fe[1])
    else:
        den = 1

    result = {}

    for v in vs:
        d2 = degrees [v]
        w2 = cw(graph, v, degrees=degrees, weight=weight)
        fin = d2**2 - w2[1] + 2*w2[0]
        result [v] = (fin/den)
    return result

def lap_cent_weighted_add_remove_edge(graph, add_list, remove_list, laplacian, degrees=None, norm=False, weight='weight'):

    vs = []
    for edge in add_list:
        source = edge [0]
        vs.append(source)
        destination = edge [1]
        vs.append(destination) 
        w = edge [2]
        graph.add_edge(source, destination, weight=w)

        if source in degrees:
            degrees[source] = degrees[source] + 1
        else:
            degrees[source] = 1
        if destination in degrees:
            degrees[destination] = degrees[destination] + 1
        else:
            degrees[destination] = 1

    for edge in remove_list:
        source = edge [0]
        vs.append(source)
        destination = edge [1]
        vs.append(destination)

        if source in degrees:
            degrees[source] = degrees[source] - 1
        else:
            degrees[source] = 0
        if destination in degrees:
            degrees[destination] = degrees[destination] - 1
        else:
            degrees[destination] = 0

    vs2 = set(vs)
    for node in set(vs):
        try:
            vs2 |= set(graph.neighbors(node))
        except (networkx.exception.NetworkXError, KeyError) as e:
            continue

    for edge in remove_list:
        source = edge [0]
        destination = edge [1]
        try:
            graph.remove_edge(source, destination)
        except (networkx.exception.NetworkXError, KeyError) as e:
            continue

    if degrees is None:
         degrees = dict(graph.degree(weight=weight))

    if norm == True:
        fe = lap_energy(graph, degrees=degrees, weight=weight)
        den = float(fe[0]+fe[1])
    else:
        den = 1

    result = laplacian

    for v in vs2:    		
        try:
	        d2 = degrees [v]
	        w2 = cw(graph, v, degrees=degrees, weight=weight)
	        fin = d2**2 - w2[1] + 2*w2[0]
	        result [v] = (fin/den)
        except (networkx.exception.NetworkXError, KeyError) as e:
            continue
    return result, len(vs2)

def lap_cent(graph, nbunch=None, degrees=None, norm=False):
    if nbunch is None:
        vs = graph.nodes()
    else:
        vs = nbunch
    if degrees is None:
         degrees = dict(graph.degree(weight=None))
    if norm is True:
        den = sum(v**2 + v for i,v in degrees.items())
        den = float(den)
    else:
        den = 1

    result = {}

    for v in vs:
        neis = graph.neighbors(v)
        loc = degrees[v]
        nei = 2*sum(degrees[i] for i in neis)
        val = (loc**2 + loc + nei)/den
        result[v] = val
    return result

def lap_cent_add_remove_edge(graph, add_list, remove_list, laplacian, degrees=None, norm=False):

    vs = []
    for edge in add_list:
        source = edge [0]
        vs.append(source)
        destination = edge [1]
        vs.append(destination)  
        graph.add_edge(source, destination)

        if source in degrees:
            degrees[source] = degrees[source] + 1
        else:
            degrees[source] = 1
        if destination in degrees:
            degrees[destination] = degrees[destination] + 1
        else:
            degrees[destination] = 1

    for edge in remove_list:
        source = edge [0]
        vs.append(source)
        destination = edge [1]
        vs.append(destination)

        if source in degrees:
            degrees[source] = degrees[source] - 1
        else:
            degrees[source] = 0
        if destination in degrees:
            degrees[destination] = degrees[destination] - 1
        else:
            degrees[destination] = 0

    vs2 = set(vs)
    for node in set(vs):
        try:
            vs2 |= set(graph.neighbors(node))
        except (networkx.exception.NetworkXError, KeyError) as e:
            continue

    for edge in remove_list:
        source = edge [0]
        destination = edge [1]
        try:
            graph.remove_edge(source, destination)
        except (networkx.exception.NetworkXError, KeyError) as e:
            continue

    if degrees is None:
         degrees = graph.degree(weight=None)
    
    if norm is True:
        den = sum(v**2 + v for i,v in degrees.items())
        den = float(den)
    else:
        den = 1       

    result = laplacian

    for v in vs2:
        try:
            neis = graph.neighbors(v)
            loc = degrees[v]
            nei = 2*sum(degrees[i] for i in neis)
            val = (loc**2 + loc + nei)/den
            result[v] = val        
        except (networkx.exception.NetworkXError, KeyError) as e:
            continue
    return result, len(vs2)

