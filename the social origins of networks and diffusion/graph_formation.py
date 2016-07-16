import networkx as nx

G = nx.Graph()

G.add_edges_from([(1, 2), (1, 3), (2, 1)])
print (nx.is_connected(G))

