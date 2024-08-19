def solve_tsp(G):
    visited = [] # list of visited nodes
    y = 0    # holder values for graph traversal
    x = 0    # holder values for graph traversal
    cost = 0 # store the total cost

    while x not in visited:
        edges = G[x]  # the node placement that we update for traversing through
        min_cost = -1 # storage for the updating of the minimum cost in the node
        min_node = -1 # storage for smallest node
        visited.append(x)

        # find the smallest unvisited edge
        for (i, j) in enumerate(edges):
            if (min_cost == -1) and (i not in visited):
                min_cost = j
                min_node = i
            elif (min_cost != -1) and (j < min_cost) and (i not in visited):
                min_cost = j
                min_node = i
        if min_node != -1: # find the next edge to check
            x = min_node
        if min_cost != -1: # add to the total cost
            cost += min_cost

    # adding the cost of final node to starting point
    cost += G[x][y]
    print("Output: ", cost)

# example graph
G = [[0,1,3,7],[1,0,2,3],[3,2,0,1],[7,3,1,0]]
solve_tsp(G)