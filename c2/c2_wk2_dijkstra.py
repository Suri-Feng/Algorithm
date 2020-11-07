
num_nodes = 201

gr = [[] for i in range(num_nodes)]
weights = [{} for i in range(num_nodes)]

visited = [False] * num_nodes


########################################################
# Importing the graphs
file = open("dijkstraData.txt", "r")
data = file.readlines()

for line in data:
    items = line.split()
    for i in range(1, len(items)):
        node, weight = items[i].split(',')
        gr[int(items[0])] += [int(node)]
        weights[int(items[0])][int(node)] = int(weight)

print(gr)
#print(weights)

A = [1000000]*num_nodes
A[1] = 0
not_X = list(range(1, num_nodes))
not_X.remove(1)
X = [1]

while(not_X != []):
    min_len = 1000000
    for v in X:
        A_v = A[v]
        for w in gr[v]:
            if w in not_X:
                curr_len = A_v + weights[v][w]
                if curr_len < min_len:
                    min_len = curr_len
                    v_star = v
                    w_star = w
    X += [w_star]
    not_X.remove(w_star)
    A[w_star] = A[v_star] + weights[v_star][w_star]

destinations = [7,37,59,82,99,115,133,165,188,197]
ans = [A[i] for i in destinations]
print(ans)