import numpy as np
import random
import math
import networkx as nx
import matplotlib.pyplot as plt

group = {}
piles_number = 4
for i in range(piles_number):
    for j in range(0, int(math.pow(2, i))):
        group[(i, j)] = []

base = 5
base_increase = 0
for i in range(piles_number):
    for j in range(0, int(math.pow(2, i))):
        if i == 0:
            group[(i, j)] = range(0, base + 1)
            base_increase = base + 1
        else:
            group[(i, j)] = range(base_increase, base_increase + increase_number)
            base_increase += increase_number
    increase_number = int (math.pow(5, i+2))
print (group)
print (base_increase)
individuals = []
for i in range(base_increase):
    individuals.append(i)

individuals_group = {}
for keys in group.keys():
    for items in group[keys]:
        individuals_group[items] = keys
print (individuals_group)

def find_partner(now_individual, now_position, alpha, group, edge_number):
    constant_sum = 0
    pile_index = now_position[0]
    for i in range(1, pile_index + 2):
        constant_sum = constant_sum + math.pow(math.e, (-alpha) * i)
    constant = 1 / constant_sum
    probability = []
    for i in range(1, pile_index + 2):
        probability.append(constant * math.pow(math.e, (-alpha) * i))
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

    edge_number_now = 0
    selected_partner = []
    while edge_number_now < edge_number:
        position = []
        if distance == 1:
            pile_index_i = now_position[0]
            pile_index_j = now_position[1]
            for i in range(0, pile_index + 1):
                for j in range(0, i + 1)

