f = open('g3.txt', 'r')

num_vertices, num_edges = f.readline().split()
num_vertices, num_edges = int(num_vertices), int(num_edges)
gr = [[] for i in range(num_vertices + 1)]
gr_h2t = [[] for i in range(num_vertices + 1)]
weights = [{} for i in range(num_vertices + 1)]
weights_h2t = [{} for i in range(num_vertices + 1)]

data = f.readline()
while data:
    u, v, weight = data.split()
    gr[int(u)] += [int(v)]
    gr_h2t[int(v)] += [int(u)]
    weights[int(u)][int(v)] = int(weight)
    weights_h2t[int(v)][int(u)] = int(weight)
    data = f.readline()

f.close()

#############################

infinity = 100000000000

# O(nm)
def SSSP_Bellman_Ford(s):
    A = [[infinity]* (num_vertices + 1) for i in range(num_vertices + 1)]
    A[0][s] = 0

    for i in range(1, num_vertices + 1):
        for v in range(1, num_vertices + 1):
            case2 = infinity
            for w in gr_h2t[v]:
                if A[i-1][w] + weights_h2t[v][w] < case2:
                    case2 = A[i-1][w] + weights_h2t[v][w]
            A[i][v] = min(A[i - 1][v], case2)
        if i < num_vertices and A[i] == A[i - 1]:
            break
        if i == num_vertices and A[i-1] != A[i]:
            raise Exception('Has negative cycle')

    shortest_path = min(A[i])
    return shortest_path

shortest_paths = []
# O(n)
for s in range(1, len(gr)):
    sp = SSSP_Bellman_Ford(s)
    shortest_paths.append(sp)
    if s%100 == 0:
        print(s)

shortest_shortest_path = min(shortest_paths)
print(shortest_shortest_path)