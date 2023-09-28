from os import *
from sys import *
from collections import *
from math import *

from typing import List

def delete_repeating_adjacent(s, cost):
    stack = []
    total_cost = 0

    for i, char in enumerate(s):
        if stack and stack[-1][0] == char:
            total_cost += min(cost[i], stack[-1][1])
            if cost[i] > stack[-1][1]:
                stack.pop()
                stack.append((char, cost[i]))
        else:
            stack.append((char, cost[i]))

    result = ''.join(char for char, _ in stack)
    return total_cost

def minimumCost(n: int, s: str, cost: List[int]) -> int:
    return delete_repeating_adjacent(s ,cost)
