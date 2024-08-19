def prims(G):
    s <- pick a source vertex from V

    for v in V: #v: current vertex; V: all the vertices in G
        dist[v] = infinity
        prev[v] = Empty

    #initalize source
    dist[v] = 0
    prev[v] = s

    #update neighbouring nodes of s
    for node in s.neighbours
        dist[v] = w(s,node)
        prev[v] = s

    while(len(visited)<len(V)):
        CurrentNode = unvisited vertex v with smallest dist[v]
        MST.add((prevNode, CurrentNode))
        for node in CurrentNode.neighbours:
            dist[node] = min(w(CurrentNode, node), dist[node])
            if dist[node] updated: prev[node] = CurrentNode
        visited.add(CurrentNode)
    return MST

def prims(G):
    Result = []
    visited = [] #pick one vertex from V

    while(len(visited)<V):
        find (a,b) where
            (a is in visited and b is not in visited) and (Edge(a,b) is min)
        Result.add((a,b))
        visited.add(b)
    
    return Result