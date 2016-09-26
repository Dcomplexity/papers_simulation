import numpy as np
import random
import math
import networkx as nx
import matplotlib.pyplot as plt

group = {}
group_number = 8
base = 4
base_increase = 0
# for i in range(group_number):
#     if i == 0:
#         group[i] = range(0, base+1)
#         base_increase = base + 1
#     if i == 1:
#         increase_number = int(math.pow(5, 2))
#         group[i] = range(base_increase, base_increase + increase_number)
#         base_increase += increase_number
#     if i in range(2, 4):
#         increase_number = int(math.pow(5, 3))
#         group[i] = range(base_increase, base_increase + increase_number)
#         base_increase += increase_number
#     if i in range(4, 8):
#         increase_number = int(math.pow(5, 4))
#         group[i] = range(base_increase, base_increase + increase_number)
#         base_increase += increase_number
# print (group)

for i in range(group_number):
    if i == 0:
        group[i] = range(0, base+1)
        base_increase = base + 1
    else:
        increase_number = int(math.pow(4, i+1))
        group[i] = range(base_increase, base_increase+increase_number)
        base_increase += increase_number

print (group)


individuals = []
for i in range(base_increase):
    individuals.append(i)

individuals_group = {}
for keys in group.keys():
    for items in group[keys]:
        individuals_group[items] = keys
print (individuals_group)

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

def find_partner(now_individual, now_position, alpha, group, edge_number):
    constant_sum = 0
    for i in range(1, 5):
        constant_sum = constant_sum + math.pow(math.e, (-alpha) * i)
    constant = 1 / constant_sum
    probability = []
    for i in range(1, 5):
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

        selected_group = group[position_new]
        selected_partner_temp = random.sample(selected_group, 1)[0]
        if selected_partner_temp not in selected_partner + [now_individual]:
            edge_number_now += 1
            selected_partner.append(selected_partner_temp)

    return selected_partner

alpha = 0
network = {}

for i in individuals:
    network[i] = []
    partner = find_partner(i, individuals_group[i], alpha, group, 5)
    for j in partner:
        network[i].append(j)

edges_list = []
for keys in network.keys():
    for items in network[keys]:
        edges_list.append((keys, items))
G = nx.DiGraph()
G.add_edges_from(edges_list)


in_degree = G.in_degree()
print (in_degree)
print (in_degree.values())
in_degree_histogram_temp = {}
for values in in_degree.values():
    if values not in in_degree_histogram_temp.keys():
        in_degree_histogram_temp[values] = 0
    else:
        in_degree_histogram_temp[values] += 1

print (in_degree_histogram_temp)

max_in_degree = max(in_degree.values())
print (max_in_degree)
in_degree_histogram = []
for i in range(max_in_degree + 1):
    in_degree_histogram.append(0)
for keys in in_degree_histogram_temp.keys():
    in_degree_histogram[keys] = in_degree_histogram_temp[keys]
print (in_degree_histogram)
x = range(len(in_degree_histogram))                             #生成x轴序列，从1到最大度
y = [z / float(sum(in_degree_histogram)) for z in in_degree_histogram]
#将频次转换为频率，这用到Python的一个小技巧：列表内涵，Python的确很方便：）
plt.loglog(x,y,color="blue",linewidth=2)           #在双对数坐标轴上绘制度分布曲线
plt.show()