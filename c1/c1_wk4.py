from random import choice 


def performCut(graph):

    # pick a remanining edge(u,v) uniformly at random
    u_choice = choice(range(len(graph)))
    u_list = graph[u_choice]
    v_choice = choice(range(1, len(u_list)))
    u = u_list[0]
    v = u_list[v_choice]
    #print(u, v)

    while v in u_list:
        graph[u_choice].remove(v)

    # merge (or "contract") u and v into a single vertex
    for i in range(len(graph)):
        if graph[i][0] == v:
            l_temp = graph.pop(i)[1:]
            #print(l_temp)
            break
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == v:
                graph[i][j] = u
    for i in range(len(graph)):
        if graph[i][0] == u:
            # remove self-loops before it becomes the same node
            while u in l_temp:
                l_temp.remove(u)
            graph[i] = graph[i] + l_temp
            break

    return graph


def kargerMinCut(graph):
    while(len(graph) > 2):
        graph = performCut(graph)
    #print(graph)
    if len(graph[0]) != len(graph[1]):
        print('bug: ' + str(len(graph[0])) + ' ' + str(len(graph[1])))
    return len(graph[0]) -1 
    
answers = []
for i in range(200):
    aaa = []
    length = 0
    with open('KargerMinCut.txt') as f:
        for line in f:
            length += 1 
            aaa.append(line)
    for i in range(len(aaa)):
        aaa[i] = aaa[i].split('\t')[:-1]
        aaa[i] = list(map(int, aaa[i]))
    ans = kargerMinCut(aaa)
    answers.append(ans)

print(min(answers))


