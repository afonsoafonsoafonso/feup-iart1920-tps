# n-puzzle-astar puzzle_n
# h1: no of out of places pieces
# h2: sum of manhattan distance to correct position
import time

# 3x3
initialMatrix = [[1, 6, 2],[5, 7, 3],[0, 4, 8]]
final_positions = [(2,2),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]
objectiveState = [[1,2,3],[4,5,6],[7,8,0]]

# 4x4
#initialMatrix = [[5,1,3,4],[2,0,7,8],[10,6,11,12],[9,13,14,15]]
#final_positions = [(3,3),(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2)]
#objectiveMatrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]


nrow = len(initialMatrix)
ncol = len(initialMatrix[0])

initialState = initialMatrix


queue = [initialState]
#paths = {initialState: []}

visited = []

start = time.time()
while queue:
    #time.sleep(3)
    currState = queue[0]
    zeroLoc = [(index, row.index(0)) for index, row in enumerate(currState) if 0 in row][0]
    #print(zeroLoc)
    #print(currState)
    #print(currState.h)

    if currState==objectiveState:
        break

    visited.append(currState)

    queue.pop(0)
    # move 0 para cima
    # -> 0 não está na primeira row
    #print(visited)
    if zeroLoc[0]!=0:
        newState = [row[:] for row in currState]
        newState[zeroLoc[0]][zeroLoc[1]] = newState[zeroLoc[0]-1][zeroLoc[1]]
        newState[zeroLoc[0]-1][zeroLoc[1]] = 0
        #print(newState not in visited)
        #print(newState)
        #print(visited)
        if newState not in visited:
            queue.append(newState)
    # move 0 para baixo
    # -> 0 não está na última row
    if zeroLoc[0]!=nrow-1:
        newState = [row[:] for row in currState]
        newState[zeroLoc[0]][zeroLoc[1]] = newState[zeroLoc[0]+1][zeroLoc[1]]
        newState[zeroLoc[0]+1][zeroLoc[1]] = 0
        #print(newState not in visited)
        #print(newState)
        #print(visited)
        if newState not in visited:
            queue.append(newState)
    # move 0 para direita
    # -> 0 não está na última col
    if zeroLoc[1]!=ncol-1:
        newState = [row[:] for row in currState]
        newState[zeroLoc[0]][zeroLoc[1]] = newState[zeroLoc[0]][zeroLoc[1]+1]
        newState[zeroLoc[0]][zeroLoc[1]+1] = 0
        #print(newState not in visited)
        #print(newState)
        #print(visited)
        if newState not in visited:
            queue.append(newState)
    # move 0 para esquerda
    # -> 0 não está na primeira col
    if zeroLoc[1]!=0:
        newState = [row[:] for row in currState]
        newState[zeroLoc[0]][zeroLoc[1]] = newState[zeroLoc[0]][zeroLoc[1]-1]
        newState[zeroLoc[0]][zeroLoc[1]-1] = 0
        #print(newState not in visited)
        #print(newState)
        #print(visited)
        if newState not in visited:
            queue.append(newState)

end = time.time()
print(end - start)

print("END")



