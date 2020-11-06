# Used @David Bai's template for parameters setting and reading graph

########################################################
# Data Structures

# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
#num_nodes = 13
num_nodes = 875715

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
#####
# Set two labels vistied and done so that root can be visited first 
# and done after all its head are visited 
#####
visited = [False] * num_nodes
done = [False] * num_nodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

stack = []  # Stack for DFS
order = []  # The finishing orders after the first pass


########################################################
# Importing the graphs
file = open("SCC.txt", "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]

########################################################
# DFS on reverse graph

def iterativeDFS(graph, v):
    stack.append(v)
    while stack:
        #print(stack)
        v = stack[-1]
    
        if done[v]:
            stack.pop()
            continue

        visited[v] = True
        allVisited = True
        for head in r_gr[v]:
            if not visited[head]:
                stack.append(head)
                #print(stack)
                allVisited = False
        if allVisited == True:
            stack.pop()
            done[v] = True
            order.append(v)

for node in range(1, num_nodes):
    if visited[node] == False:
        iterativeDFS(r_gr, node)

#print(order)


########################################################
# DFS on original graph

visited = [False] * len(visited)  # Resetting the visited variable
# no need to use 'done' as I won't care the order of node visited in the same SCC

order.reverse()  # The nodes should be visited in reverse finishing times

def DFS(G, i, s):
    visited[i] = True
    if i!=s:
        scc[i] = s
    scc[s] -= 1    

    for j in G[i]:
        if visited[j] == False:
            stack.append(j)

def iterativeDFS2(graph, s):
    stack.append(s)
    while stack:
        #print(stack)
        v = stack.pop()
        if visited[v]:
            continue 
        visited[v] = True
        if v!=s:
            scc[v] = s
        scc[s] -= 1   
        for head in gr[v]:
            if not visited[head]:
                stack.append(head)


for node in order:
    if visited[node] == False:
        s = node
        if gr[s] == []:
            visited[s] = True
            scc[s] = -1
        else:
            iterativeDFS2(gr, s)

#print(scc)
########################################################
# Getting the five biggest sccs
scc.sort()
print(scc[:5]) 
# the absolute of negative values will be the size,
#  positive values represent the leader in SCC



