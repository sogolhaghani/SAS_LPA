from networkx.algorithms.community import LFR_benchmark_graph

n = 15000
tau1 = 3
tau2 = 1.5
mu = 0.1
G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=5, min_community=20, seed=10)
# communities = {frozenset(G.nodes[v]['community']) for v in G}
print(G.nodes[1]['community'])