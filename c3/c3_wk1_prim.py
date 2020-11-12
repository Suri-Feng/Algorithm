import random

data = []
with open('edges.txt') as f:
    for line in f:
        data.append(line)

num_nodes, num_edges = data[0].split()
num_nodes, num_edges = int(num_nodes), int(num_edges)

#print(num_nodes, num_edges)

gr = [[] for i in range(num_nodes + 1)]
weights = [{} for i in range(num_nodes + 1)]

for i in range(num_edges):
    u, v, edge_cost = data[i + 1].split()
    # note it is undirected graph
    gr[int(u)] += [int(v)]
    gr[int(v)] += [int(u)]
    weights[int(u)][int(v)] = int(edge_cost)
    weights[int(v)][int(u)] = int(edge_cost)

#print(gr, weights)

#####################

T_cost = 0
s = random.randint(1, num_nodes)
X = [s]
not_X = list(range(1, num_nodes + 1))
not_X.remove(s)

while(not_X != []):
    min_cost = 1000000
    for u in X:
        for v in gr[u]:
            if v in not_X:
                cost = weights[u][v]
                if cost < min_cost:
                    min_cost = cost 
                    u_star = u
                    v_star = v
    X += [v_star]
    not_X.remove(v_star)
    T_cost += min_cost

print(T_cost)