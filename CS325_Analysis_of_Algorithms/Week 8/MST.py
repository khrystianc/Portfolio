def prims(G): # G is a 2D array.
    INF = 9999999
    V = len(G) # number of vertices in graph
    weight_count = 0 # tracks the total weight of the tree
    selected = [] # for the algorithm to handle any amount of vertices
    for i in G:
        selected.append(0)
    # set number of edge to 0
    no_edge = 0
    # make first vertex true
    selected[0] = True
    print("Edge : Weight\n") #titles of what is returned in a table list like dijkstra
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):
                        # not in selected and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ":" + str(G[x][y])) # prints the edge and weight
        weight_count += (G[x][y])
        selected[y] = True
        no_edge += 1
    print("\nTotal weight=", weight_count) # prints the total weight

G = [[0, 9, 75, 0, 0],
         [9, 0, 95, 19, 42],
         [75, 95, 0, 51, 66],
         [0, 19, 51, 0, 31],
         [0, 42, 66, 31, 0]]

prims(G)