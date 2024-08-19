def minEffort(puzzle):
    startPoint = (puzzle[0][0])
    pathlist = []
    m = 0
    n = 0
    counter = 0
    while startPoint != puzzle[m-1][n-1] or "visited":
        if (puzzle[m+1][n]-puzzle[m][n]) > (puzzle[m][n+1]-puzzle[m][n]):
            pathlist.append(startPoint)
            counter += (puzzle[m][n+1]-puzzle[m][n])
            nextPoint = puzzle[m][n+1]
            startPoint = "visited"
            startPoint = nextPoint
            n += 1
            continue
        if (puzzle[m+1][n]-puzzle[m][n]) < (puzzle[m][n+1]-puzzle[m][n]):
            pathlist.append(startPoint)
            counter += (puzzle[m+1][n]-puzzle[m][n])
            nextPoint = puzzle[m+1][n]
            startPoint = "visited"
            startPoint = nextPoint
            m += 1
            continue
        return (pathlist, counter)

print(minEffort([[1, 3, 5], [2, 8, 3], [3, 4, 5]]))