import numpy as np
import random
import networkx as nx
from networkx.algorithms import community

from IPython.display import Image
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def _main():
    G_karate = nx.karate_club_graph()
    n = G_karate.number_of_nodes()
    m = G_karate.number_of_edges()
    print("Number of nodes :", str(n))
    print("Number of edges :", str(m))
    print("Number of connected components :" ,str(nx.number_connected_components(G_karate)))
    plt.figure(figsize=(12,8))
    nx.draw(G_karate)

    # Yields = community.label_propagation_communities(G_karate)
    Yields = community.asyn_lpa_communities(G_karate)
    for x in Yields:
        print(x)

if __name__ == "__main__":
    _main()
