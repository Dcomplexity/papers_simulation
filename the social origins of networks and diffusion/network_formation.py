import numpy as np
import random
import math

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
        y = int(math.pow(2, distance-1))
        print (y)
        print (int(now_position % y))
        if int(now_position % y) < int(y / 2):
            for k in range(int(y/2), y):
                positions.append(int(now_position / y) * y + k)
        else:
            for k in range(0, int(y/2)):
                positions.append(int(now_position / y) * y + k)
    return positions

def consolidation_formation(dimension0, beta): #beta represents consolidation
    constant_sum = 0
    for i in range(1, 7):
        constant_sum = constant_sum + math.pow(2, (-beta) * i)
    constant = 1 / constant_sum
    probability = []
    for i in range(1, 7):
        probability.append(constant * math.pow(2, (-beta) * i))
    individuals_con = {}
    for keys in dimension0.keys():
        for items in dimension0[keys]:
            individuals_con[items] = keys
    probability_sum = []
    temp_sum = 0
    for i in range(len(probability)):
        temp_sum = temp_sum + probability[i]
        probability_sum.append(temp_sum)
    p = random.uniform(0, 1)
    for i in range(len())

    return probability, probability_sum, individuals_con

probability, probability_sum, individuals_con = consolidation_formation(dimension[0], -1)

