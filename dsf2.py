

# python code
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, parent):
    even_count = 0
    odd_count = 0
    total_weight = weights[node]
    
    for neighbor in graph[node]:
        if neighbor != parent:
            child_even, child_odd, child_weight = dfs(neighbor, node)
            even_count += child_even
            odd_count += child_odd
            total_weight += child_weight
            
            if child_weight % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    if total_weight % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    
    return even_count, odd_count, total_weight

n = int(input())
weights = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
even_count, odd_count, _ = dfs(0, -1)
print(even_count, odd_count)
# This code is a solution to a problem involving trees and weights.
# It calculates the number of even and odd weighted connected components in a tree.