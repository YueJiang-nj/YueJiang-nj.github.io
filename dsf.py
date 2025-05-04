import sys

sys.setrecursionlimit(1 << 25)

n = 4
input = [[1, 2, 3, 4], [1, 2], [1, 3], [2, 4]]

weights = input[0]

tree = dict()
for i in range(1, len(weights) + 1):
    tree[i] = []

for i in range(1, n):
    edge = input[i]
    tree[edge[0]].append(edge[1])

global all_trees
all_trees = []
def dfs(node, visited, all_trees):
    if node in visited:
        return
    visited.add(node)
    if visited not in all_trees:
        all_trees.append(visited.copy())
    for neighbor in tree[node]:
        dfs(neighbor, visited, all_trees)

def dfs_reverse(node, visited, all_trees):
    if node in visited:
        return
    visited.add(node)
    if visited not in all_trees:
        all_trees.append(visited.copy())
    for n in range(len(tree[node])):
        neighbor = tree[node][len(tree[node]) - n - 1]
        dfs_reverse(neighbor, visited, all_trees)


def get_even_odd_num(tree, weights):
    weight_map = dict()
    for i in range(1, n + 1):
        weight_map[i] = weights[i - 1]

    num_even_trees = 0
    num_odd_trees = 0
    for subtree in all_trees:
        total_weight = 0
        for node in subtree:
            total_weight += weight_map[node]
        if total_weight % 2 == 0:
            num_even_trees += 1
        else:
            num_odd_trees += 1
    return num_even_trees, num_odd_trees

for i in range(1, n + 1):
    all_trees = []
    visited = set()
    dfs(i, visited, all_trees)
    visited = set()
    dfs_reverse(i, visited, all_trees)
    num_even_trees, num_odd_trees = get_even_odd_num(tree, weights)
    print(num_even_trees, num_odd_trees)

