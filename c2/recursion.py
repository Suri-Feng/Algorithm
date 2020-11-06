
# passed all test cases but will exceed max recursion limit
# Used @David Bai's template for parameters setting and reading graph

########################################################
# Data Structures

# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
#num_nodes = 875715
num_nodes = 10

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * num_nodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

stack = []  # Stack for DFS
order = []  # The finishing orders after the first pass


########################################################
# Importing the graphs
file = open("SCCtest1.txt", "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]

########################################################
# DFS on reverse graph

def DFS_rev(G, i):
    visited[i] = True
    for j in G[i]:
        if visited[j] == False:
            DFS_rev(G, j)
    #print(i)
    order.append(i)

for node in range(1, num_nodes):
    if visited[node] == False:
        stack.append(node)
    while stack:
        stack_node = stack.pop()
        DFS_rev(r_gr, stack_node)


print(order)


########################################################
# DFS on original graph

visited = [False] * len(visited)  # Resetting the visited variable
order.reverse()  # The nodes should be visited in reverse finishing times

def DFS(G, i, s):
    visited[i] = True
    if i!=s:
        scc[i] = s
    scc[s] -= 1    

    for j in G[i]:
        if visited[j] == False:
            DFS(G, j, s)

for node in order:
    if visited[node] == False:
        stack.append(node)
        s = node
    while stack:
        stack_node = stack.pop()
        DFS(gr, stack_node, s)

print(scc)
########################################################
# Getting the five biggest sccs
scc.sort()
print(scc[:5])
