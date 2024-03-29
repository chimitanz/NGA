import math
import random

"""
This file evaluates fitness according to some benchmark functions in GA
Modified by Yizhou Xiao
"""


"""
#range is [-32, 32]
"""
def f1(vector):
    D = len(vector)
    result = 0
    num1 = 0
    num2 = 0
    for value in vector:
        num1 += value ** 2
        num2 += math.cos(2 * math.pi * value)
    minuend = -20 * math.exp(-0.2 * math.sqrt(num1 / D))
    subtrahend = math.exp(num2 / D)
    result = minuend - subtrahend + 20 + math.e
    if result == 0:
        return 0
    else:
        return 1/ abs(result)


"""
#range is [-100, 100]
"""
def f2(vector):
    result = 0
    for value in vector:
        result += value ** 2
    if result == 0:
        return 0
    else:
        return 1 / abs(result)


"""
#range is [-10, 10]
"""
def f3(vector):
    num1 = 0
    num2 = 0
    for value in vector:
        num1 = abs(num1 + value)
        num2 = abs(num2 * value)
    result = num1 + num2
    if result == 0:
        return 0
    else:
        return 1 / abs(result)


"""
#range is [-1.28, 1.28]
"""
def f4(vector):
    result = 0
    for i in range(len(vector)):
        result += (i+1) * vector[i] ** 4 + random.random()
    if result == 0:
        return 0
    else:
        return 1 / abs(result)


"""
#range is [-5.12, 5.12]
"""
def f5(vector):
    result = 0
    for value in vector:
        result += value ** 2 - 10 * math.cos(2 * math.pi * value) + 10
    if result == 0:
        return 0
    else:
        return 1 / abs(result)


"""
#range is [-600, 600]
"""
def f6(vector):
    num1 = 0
    num2 = 1
    for i in range(len(vector)):
        num1 += vector[i] ** 2
        num2 *= math.cos(vector[i] / (math.sqrt(i+1)))+1
    result = num1 / 4000 + num2
    if result == 0:
        return 0
    else:
        return 1 / abs(result)


"""
#range is [-32, 32]
"""
def f7(vector):
    result = 0
    for i in range(len(vector) - 1):
        result += 100 * (vector[i + 1] - vector[i] ** 2) ** 2 + (vector[i] - 1) ** 2
    if result == 0:
        return 0
    else:
        return 1 / abs(result)


'''
The following function evaluates the fitness for a single vector
'''


def evaluate(vector):
    return f2(vector)


'''
The following function evaluates the fitness for a list of vectors
'''


def evaluate_lst(population):
    fitness = []
    for vector in population:
        fitness.append(f2(vector))
    return fitness


