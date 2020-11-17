from uf import Unionfind

data = []
with open('clustering1.txt') as f:
    for line in f:
        data.append(line)

num_nodes = int(data[0])

#print(num_nodes)

maxDis = 0
for i in range(1, len(data)):
    _, _, edge_cost = data[i].split()
    if int(edge_cost) > maxDis:
        maxDis = int(edge_cost)

##### directly import the sorted edge costs ######
distances = [[] for i in range(maxDis + 1)]

for i in range(1, len(data)):
    u, v, edge_cost = data[i].split()
    distances[int(edge_cost)] += [(int(u), int(v))]


#print(distances)

sorted_distances = []
sorted_edges = []
for i in range(len(distances)):
    for edge in distances[i]:
        sorted_distances.append(i)
        sorted_edges.append(edge)

######## Run early stop Kruskal's MST #########
uf = Unionfind(num_nodes + 1)

T = []
clusters = num_nodes
flag = False
for i in range(len(sorted_edges)):
    u, v = sorted_edges[i]
    if uf.connected(u, v) == False:
        T.append((u,v))
        uf.union(u,v)
        clusters -= 1

        if clusters < 4:
            maxSpacing = sorted_distances[i]
            flag = True
    
    if flag == True:
        break


print(maxSpacing)


