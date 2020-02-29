# Usage: python3 buckets_bfs C1 C2 N
import sys

c1 = int(sys.argv[1])
c2 = int(sys.argv[2])
n = int(sys.argv[3])

initialState = (0,0)
objectiveState = (n, 0)

queue = [initialState]
paths = {initialState: []}

visited = {}

while queue and queue[0]!=objectiveState:
    b1 = queue[0][0]
    b2 = queue[0][1]

    queue.pop(0)

    if b1 < c1 and (c1, b2) not in visited.keys():
        queue.append( (c1, b2) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(c1, b2)] = path

    if b2 < c2 and (b1, c2) not in visited.keys():
        queue.append( (b1, c2) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(b1, c2)] = path

    if b1 > 0 and (0, b2) not in visited.keys():
        queue.append( (0, b2) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(0, b2)] = path

    if b2 > 0 and (b1, 0) not in visited.keys():
        queue.append( (b1, 0) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(b1, 0)] = path

    if b1 > 0 and b2 < c2 and b1 >= (c2 - b2) and (b1-(c2-b2), c2) not in visited.keys():
        queue.append( (b1-(c2-b2), c2) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(b1-(c2-b2), c2)] = path

    if b1 > 0 and b2 < c2 and b1 < (c2 - b2) and (0, b2+b1) not in visited.keys():
        queue.append( (0, b2+b1))
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(0, b2+b1)] = path

    if b2 > 0 and b1 < c1 and b2 >= (c1 - b1) and (c1, b2-(c1-b1) ) not in visited.keys():
        queue.append( (c1, b2-(c1-b1)) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(c1, b2-(c1-b1))] = path

    if b2 > 0 and b1 < c1 and b2 < (c1 - b1) and (b1+b2, 0) not in visited.keys():
        queue.append( (b1+b2, 0) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(b1+b2, 0)] = path

    visited[(b1, b2)] = True

# fim
if objectiveState in visited.keys():
    print("Path to solution: ")
    print(paths[objectiveState])
else: 
    print("No solution was found.")


    