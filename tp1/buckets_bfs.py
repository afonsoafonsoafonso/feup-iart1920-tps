# Usage: python3 buckets_bfs C1 C2 N
import sys

c1 = int(sys.argv[1])
c2 = int(sys.argv[2])
n = int(sys.argv[3])

initialState = (0,0)
objectiveState = (n, 0)

queue = []
queue.append(initialState)

paths = {}
paths[initialState] = []

visited = {}

while queue:
    b1 = queue[0][0]
    b2 = queue[0][1]
    print("B1:" + str(b1) + " ; " + "B2:" + str(b2))

    if queue[0] == objectiveState:
        break;

    queue.pop(0)

    if (b1, b2) in visited.keys():
        continue
    else: visited[(b1, b2)] = True

    if b1 < c1:
        queue.append( (c1, b2) )
        visited[(c1, b2)] = True
        paths[(c1, b2)] = paths[(b1, b2)].append((b1, b2))

    if b2 < c2:
        queue.append( (b1, c2) )
        visited[(b1, c2)] = True
        paths[(b1, c2)] = paths[(b1, b2)].append((b1, b2))

    if b1 > 0:
        queue.append( (0, b2) )
        visited[(0, b2)] = True
        paths[(0, b2)] = paths[(b1, b2)].append((b1, b2))

    if b2 > 0:
        queue.append( (b1, 0) )
        visited[(b1, 0)] = True
        paths[(b1, 0)] = paths[(b1, b2)].append((b1, b2))

    if b1 > 0 and b2 < c2 and b1 > (c2 - b2):
        queue.append( (b1-(c2-b2), c2) )
        visited[(b1-(c2-b2), c2)] = True
        paths[(b1-(c2-b2), c2)] = paths[(b1, b2)].append((b1, b2))

    if b1 > 0 and b2 < c2 and b1 < (c2 - b2):
        queue.append( (0, b2+b1))
        visited[(0, b2+b1)] = True
        paths[(0, b2+b1)] = paths[(b1, b2)].append((b1, b2))

    if b2 > 0 and b1 < c1 and b2 > (c1 - b1):
        queue.append( (c1, b2-(c1-b1)) )
        visited[(c1, b2-(c1-b1))] = True
        paths[(c1, b2-(c1-b1))] = paths[(b1, b2)].append((b1, b2))

    if b2 > 0 and b1 < c1 and b2 < (c1 - b1):
        queue.append( (b1+b2, 0) )
        visited[(b1+b2, 0)] = True
        paths[(b1+b2, 0)] = paths[(b1, b2)].append((b1, b2))

# fim


    