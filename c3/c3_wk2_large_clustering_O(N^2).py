### implemented in O(num_nodes^2)

from uf import Unionfind

def Hamming_distance(num_bits, node1_bits, node2_bits):
    dis = 0
    for i in range(num_bits):
        if node1_bits[i] != node2_bits[i]:
            dis += 1
    return dis

############# Loading ################

data = []
with open('clustering_big.txt') as f:
    for line in f:
        data.append(line)

num_nodes, num_bits = data[0].split()
num_nodes, num_bits = int(num_nodes), int(num_bits)

distance_bits = [[] for i in range(num_nodes + 1)]

for i in range(1, num_nodes + 1):
    distance_bits[i] = data[i].split()

#print(distance_bits)

#############################

edges = []# storing nodes where have distance 0, 1, 2

for i in range(1, num_nodes + 1):
    for j in range(i + 1, num_nodes + 1):
        dis = Hamming_distance(num_bits, distance_bits[i], distance_bits[j])
        if dis <= 2:
            edges.append((i, j))


print(len(edges))

uf = Unionfind(num_nodes + 1)

clusters = num_nodes
flag = False
for i in range(len(edges)):
    u, v = edges[i]
    if uf.connected(u, v) == False:
        clusters -= 1
    uf.union(u,v)


print(clusters)
