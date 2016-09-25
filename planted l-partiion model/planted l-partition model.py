import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

individuals = []
group= {}
group_number = 4
group_index = []
for i in range(group_number):
    group_index.append(i)

member_number = 32
individual_number = group_number * member_number

network = {}

for i in range(individual_number):
    individuals.append(i)

for i in individuals:
    network[i] = []

for i in range(group_number):
    group_member = random.sample(individuals, member_number)
    group[i] = group_member
    individuals = list(set(individuals) - set(group_member))

average_degree = 16
z_in = 15
p_in = z_in / (member_number - 1)
p_out = (average_degree - p_in * (member_number - 1)) / ((member_number) * (group_number - 1))

p_in_use = p_in / (p_in + p_out)
p_out_use = p_out / (p_in + p_out)

total_edges = individual_number * average_degree / 2
for i in range(int(total_edges)):
    p = random.uniform(0, 1)
    if p < p_in_use:
        L = random.sample(group_index, 1)
        L = L[0]
        while True:
            l_i = random.sample(group[L], 1)
            l_j = random.sample(set(group[L]) - set(l_i), 1)
            l_i = l_i[0]
            l_j = l_j[0]
            if (l_j not in network[l_i]):
                network[l_i].append(l_j)
                network[l_j].append(l_i)
                break
    else:
        L1 = random.sample(group_index, 1)
        L2 = random.sample(set(group_index) - set(L1), 1)
        L1 = L1[0]
        L2 = L2[0]
        while True:
            l_i = random.sample(group[L1], 1)
            l_j = random.sample(group[L2], 1)
            l_i = l_i[0]
            l_j = l_j[0]
            if (l_j not in network[l_i]):
                network[l_i].append(l_j)
                network[l_j].append(l_i)
                break

edges_list = []
for keys in network.keys():
    for item in network[keys]:
        edges_list.append((keys, item))

G = nx.Graph()
G.add_edges_from(edges_list)

print (nx.is_connected(G))
print (nx.average_clustering(G))
print (G.degree())
nx.draw(G)
plt.show()

RG = nx.random_graphs.random_regular_graph(50, 3200)
print (nx.average_clustering(RG))

dd = nx.average_clustering(G)
ddd = nx.average_clustering(RG)
print (dd / ddd)

