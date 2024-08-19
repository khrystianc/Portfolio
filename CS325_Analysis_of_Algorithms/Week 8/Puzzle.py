def solve_puzzle(Board, Source, Destination):
    weight = 0
    no_edge = 0
    selected = []
    for i in Board:
        selected.append("")
    selected[0] = True
    travel = ""
    if len(Board) < 3:
        return "Board too small"
    for i in Board:
        if len(i) < 3:
            return "Board too small"
        if Source[1] > len(i) or Destination[1] > len(i):
            return "Input out of bounds"
    if Source[0] > len(Board) or Destination[0] > len(Board):
        return "Input out of bounds"
    if (Board[Source[0]][Source[1]]) or (Board[Destination[0]][Destination[1]]) == "#":
        print("None")
    while Source != Destination:
        for i in range(Source[0], Destination[0]):
            if selected[i]:
                for j in range(Source[1], Destination[1]):
                    if ((not selected[j]) and Board[i][j]):
                        if i < Source[0]:
                            travel.append("U")
                        if i > Source[0]:
                            travel.append("D")
                        if j < Source[1]:
                            travel.append("L")
                        if j > Source[1]:
                            travel.append("R")
                        Source[0] = i
                        Source[1] = j
        weight +=1
        selected[Source[1]] = True
        no_edge +=1
        if Source == Destination:
            print("Weight:" + weight)
            print(str(travel))

Board = [["","","","",""],
            ["","","#","",""],
            ["","","","",""],
            ["#","","#","#",""],
            ["","#","","",""]]

solve_puzzle(Board, (1,3), (3,3))

# Should return "Weight: 4, 'RDDL'"