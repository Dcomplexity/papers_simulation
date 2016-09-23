import numpy as np
import random
import math
import networkx as nx

dimension = []
dimension.append({})
# for i in range(32):
#     dimension[0][i] = []
individuals = []
for i in range(3200):
    individuals.append(i)
for i in range(32):
    group_member = random.sample(individuals, 100)
    dimension[0][i] = group_member
    individuals = list(set(individuals) - set(group_member))


def find_position(now_position, distance):
    positions = []
    if distance == 1:
        positions.append(now_position)
    else:
        y = int(math.pow(2, distance - 1))
        if int(now_position % y) < int(y / 2):
            for k in range(int(y / 2), y):
                positions.append(int(now_position / y) * y + k)
        else:
            for k in range(0, int(y / 2)):
                positions.append(int(now_position / y) * y + k)
    position_new = random.sample(positions, 1)
    return position_new[0]


def consolidation_formation(dimension0, beta):  # beta represents consolidation
    constant_sum = 0
    for i in range(1, 7):
        constant_sum = constant_sum + math.pow(2, (-beta) * i)
    constant = 1 / constant_sum
    probability = []
    for i in range(1, 7):
        probability.append(constant * math.pow(2, (-beta) * i))
    probability_sum = []
    temp_sum = 0
    for i in range(len(probability)):
        temp_sum = temp_sum + probability[i]  """account the probability, in order to find the max probability"""
        probability_sum.append(temp_sum)

    individuals_0 = {}
    for keys in dimension0.keys():
        for items in dimension0[keys]:
            individuals_0[items] = keys  """record the position(keys) of individuals(items) of dimension0"""

    individuals_con = {}     """individuals_con for individuals consolidation"""
    for keys in individuals_0.keys():
        position_0 = individuals_0[keys]   """position_0 means the position of individual in dimension0"""
        p = random.uniform(0, 1)
        distance = 0
        for i in range(len(probability_sum)):   """calculate the distances between different dimensions"""
            if p < probability_sum[i]:
                distance = i + 1
                break
        position_new = find_position(position_0, distance)
        individuals_con[keys] = position_new

    positions_con = {}
    for i in range(32):
        positions_con[i] = []
    for keys in individuals_con.keys():
        positions_con[individuals_con[keys]].append(keys)

    return positions_con, individuals_con


beta = 2
alpha = 2
for i in range(1, 10):
    positions_con = consolidation_formation(dimension[0], beta)[0]
    dimension.append(positions_con)
print(len(dimension))
individual_pos = []
for i in range(len(dimension)):
    individual_temp = {}
    for keys in dimension[i]:
        for items in dimension[i][keys]:
            individual_temp[items] = keys
    individual_pos.append(individual_temp)
print(individual_pos)

network = {}
for i in range(3200):
    network[i] = []
individual_group = range(3200)
dimension_group = range(10)


def find_partner(now_individual, now_position, alpha, now_neighbor, dimension, selected_dimension, edge_number):
    constant_sum = 0
    for i in range(1, 7):
        constant_sum = constant_sum + math.pow(2, (-alpha) * i)
    constant = 1 / constant_sum
    probability = []
    for i in range(1, 7):
        probability.append(constant * math.pow(2, (-alpha) * i))
    probability_sum = []
    temp_sum = 0
    for i in range(len(probability)):
        temp_sum = temp_sum + probability[i]
        probability_sum.append(temp_sum)
    p = random.uniform(0, 1)
    distance = 0
    for i in range(len(probability_sum)):
        if p < probability_sum[i]:
            distance = i + 1
            break

    while True:
        positions = []
        if distance == 1:
            positions.append(now_position)
        else:
            y = int(math.pow(2, distance - 1))
            if int(now_position % y) < int(y / 2):
                for k in range(int(y / 2), y):
                    positions.append(int(now_position / y) * y + k)
            else:
                for k in range(0, int(y / 2)):
                    positions.append(int(now_position / y) * y + k)

        position_new = random.sample(positions, 1)[0]

        selected_group = dimension[selected_dimension][position_new]
        selected_partner = random.sample(selected_group, 1)[0]
        if selected_partner not in now_neighbor + [now_individual]:
            edge_number += 1
            break

    return selected_partner, edge_number


total_edges = 16000
now_edges = 0
while now_edges < total_edges:
    selected_individual = random.sample(individual_group, 1)[0]
    selected_dimension = random.sample(dimension_group, 1)[0]
    selected_indiv_pos = individual_pos[selected_dimension][selected_individual]
    selected_partner, now_edges = find_partner(selected_individual, selected_indiv_pos, alpha, network[selected_individual], dimension, selected_dimension, now_edges)
    network[selected_individual].append(selected_partner)
    network[selected_partner].append(selected_individual)

edges_list= []
for keys in network.keys():
    for item in network[keys]:
        edges_list.append((keys, item))
G = nx.Graph()
G.add_edges_from(edges_list)

print (nx.is_connected(G))
print (nx.average_clustering(G))
print (nx.degree_histogram(G))

nx.write_edgelist(G, "test.txt", data=False)
