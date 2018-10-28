from itertools import permutations
from math import factorial

# FronzenSet is used instead of Set
# because it can be used as key to dictionary
# Below defines certain results of v(S)
vDict = {
    frozenset(): 0,
    frozenset({1}): 125,
    frozenset({2}): 130,
    frozenset({3}): 200,
    frozenset({1, 2}): 255,
    frozenset({2, 3}): 330,
    frozenset({1, 3}): 325,
    frozenset({1, 2, 3}): 350
}

# Define the grand set G
G = {1, 2, 3}
n = len(G)


# Define v(S) for that all S is a subset of G
def v(S):
    if S <= G:
        return vDict[S]
    else:
        raise ValueError('S is not subset of G')


# Define function N that for permutation p,
# return a frozenset that contains all elements in p before i
def N(p, i):
    return frozenset(p[:p.index(i)])


# Define function S to return the Shapley value of player i
def S(i):
    sum = 0
    for p in permutations(G):
        sum += v(N(p, i) | frozenset({i})) - v(N(p, i))
    return 1/factorial(n) * sum


# print the calculation result
print(S(1), S(2), S(3))
# 90.0 95.0 165.0
