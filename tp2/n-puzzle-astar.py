# n-puzzle-astar puzzle_n
# h1: no of out of places pieces
# h2: sum of manhattan distance to correct position
import time

class State:
    def __init__(self, matrix, hs):
        self.matrix = matrix
        self.h1 = hs[0]
        self.h2 = hs[1]
        self.h = hs[0] + hs[1]

    def __str__(self):
        return self.matrix

def calculate_heuristics(matrix, final_positions):
    total_offset = 0
    out_of_place = 0
    for rown, row in enumerate(matrix): # for index, item in items
        for coln, piece in enumerate(row):
            #print(piece)
            a=rown
            b=coln
            c=final_positions[piece][0]
            d=final_positions[piece][1]
            #print("Correct position=" + str((c,d)))
            #print("Manhattan position=" + str(manhattan_pos))
            if (a,b) != (c,d):
                out_of_place += 1
                total_offset += abs(a-c) + abs(b-d)
    
    return (out_of_place, total_offset) # (h1, h2)
# 3x3
#initialMatrix = [[1, 6, 2],[5, 7, 3],[0, 4, 8]]
#final_positions = [(2,2),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]
#objectiveState = State([[1,2,3],[4,5,6],[7,8,0]], (0, 0))

# 4x4
initialMatrix = [[5,1,3,4],[2,0,7,8],[10,6,11,12],[9,13,14,15]]
final_positions = [(3,3),(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2)]
objectiveState = State([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]], (0, 0))


nrow = len(initialMatrix)
ncol = len(initialMatrix[0])

h1, h2 = calculate_heuristics(initialMatrix, final_positions)
initialState = State(initialMatrix, (h1, h2))

queue = [initialState]
paths = {initialState: []}

visited = []

start = time.time()
while queue:
    #time.sleep(3)
    currState = queue[0]
    currMatrix = currState.matrix
    zeroLoc = [(index, row.index(0)) for index, row in enumerate(currState.matrix) if 0 in row][0]
    #print(zeroLoc)
    #print(currMatrix)
    #print(currState.h)

    if queue[0].h==0:
        break

    visited.append(currMatrix)

    queue.pop(0)
    # move 0 para cima
    # -> 0 não está na primeira row
    #print(visited)
    if zeroLoc[0]!=0:
        newMatrix = [row[:] for row in currMatrix]
        newMatrix[zeroLoc[0]][zeroLoc[1]] = newMatrix[zeroLoc[0]-1][zeroLoc[1]]
        newMatrix[zeroLoc[0]-1][zeroLoc[1]] = 0
        newState = State(newMatrix, calculate_heuristics(newMatrix, final_positions))
        #print(newMatrix not in visited)
        #print(newMatrix)
        #print(visited)
        if newMatrix not in visited:
            queue.append(newState)
    # move 0 para baixo
    # -> 0 não está na última row
    if zeroLoc[0]!=nrow-1:
        newMatrix = [row[:] for row in currMatrix]
        newMatrix[zeroLoc[0]][zeroLoc[1]] = newMatrix[zeroLoc[0]+1][zeroLoc[1]]
        newMatrix[zeroLoc[0]+1][zeroLoc[1]] = 0
        #print(newMatrix not in visited)
        #print(newMatrix)
        #print(visited)
        newState = State(newMatrix, calculate_heuristics(newMatrix, final_positions))
        if newMatrix not in visited:
            queue.append(newState)
    # move 0 para direita
    # -> 0 não está na última col
    if zeroLoc[1]!=ncol-1:
        newMatrix = [row[:] for row in currMatrix]
        newMatrix[zeroLoc[0]][zeroLoc[1]] = newMatrix[zeroLoc[0]][zeroLoc[1]+1]
        newMatrix[zeroLoc[0]][zeroLoc[1]+1] = 0
        newState = State(newMatrix, calculate_heuristics(newMatrix, final_positions))
        #print(newMatrix not in visited)
        #print(newMatrix)
        #print(visited)
        if newMatrix not in visited:
            queue.append(newState)
    # move 0 para esquerda
    # -> 0 não está na primeira col
    if zeroLoc[1]!=0:
        newMatrix = [row[:] for row in currMatrix]
        newMatrix[zeroLoc[0]][zeroLoc[1]] = newMatrix[zeroLoc[0]][zeroLoc[1]-1]
        newMatrix[zeroLoc[0]][zeroLoc[1]-1] = 0
        newState = State(newMatrix, calculate_heuristics(newMatrix, final_positions))
        #print(newMatrix not in visited)
        #print(newMatrix)
        #print(visited)
        if newMatrix not in visited:
            queue.append(newState)

    #print("\n")
    #for elem in queue:
    #    print(elem.h)
    #time.sleep(1.5)
    queue.sort(key=lambda x: x.h, reverse=False)
    #for elem in queue:
    #    print(elem.h)
    #print("\n")
end = time.time()
print(end - start)

print("END")



