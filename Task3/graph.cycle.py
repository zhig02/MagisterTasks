from collections import deque
# v = int(input())
# n = int(input())
n = 6
v = 6
rebra = [[0, 1], [0, 2], [2, 3], [2, 4], [3, 5], [4, 5]]

# for i in range(n):
#     rebra.append(list(map(int, input().split())))
# print(rebra)

def make_graph(rbra: list):
    grph = {}
    for i in range(n):
        keys = [rbra[i][0], rbra[i][1]]
        values = [rbra[i][1], rbra[i][0]]
        for j in range(2):
            key = keys[j]
            value = values[j]
            if key in grph:
                grph[key].append(value)
            else:
                grph[key] = [value]
    return grph


def bfs(graph, root):

    visited = set()
    parent = {root: -1}
    distance = {root: 0}

    queue = deque([root])

    while queue:

        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = node
                distance[neighbor] = distance[node] + 1
            
            elif parent[node] != neighbor:
                return distance[node] + distance[neighbor] + 1


    return float("inf")

G = make_graph(rebra)
min_cycle_l  = float("inf")
for node in G:
    min_cycle_l = min(bfs(G, node), min_cycle_l)
print(min_cycle_l)
    