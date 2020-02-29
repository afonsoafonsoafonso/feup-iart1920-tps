# Usage: python3 buckets_dfs C1 C2 N DEPTH_MAX
import sys

c1 = int(sys.argv[1])
c2 = int(sys.argv[2])
n = int(sys.argv[3])
depth_max = int(sys.argv[4])

initialState = ((0,0),0)
objectiveState = (n, 0)

queue = [initialState]
paths = {initialState[0]: []}

visited = {}

while queue:
    b1 = queue[0][0][0]
    b2 = queue[0][0][1]
    depth = queue[0][1]
    visited[(b1, b2)] = True

    if queue[0][0]==objectiveState:
        break

    queue.pop(0)

    #print("DEPTH: " + str(depth) + " ; B1: " + str(b1) + " ; B2: " + str(b2))
    #print("QUEUE:")
    #print(queue)

    if depth == depth_max:
        continue

    if b1 < c1 and (c1, b2) not in visited.keys():
        #print("Append!\n")
        queue.append( ((c1, b2),depth+1) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(c1, b2)] = path

    if b2 < c2 and (b1, c2) not in visited.keys():
        #print("Append!\n")
        queue.append( ((b1, c2), depth+1) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(b1, c2)] = path

    if b1 > 0 and (0, b2) not in visited.keys():
        #print("Append!\n")
        queue.append( ((0, b2), depth+1) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(0, b2)] = path

    if b2 > 0 and (b1, 0) not in visited.keys():
        #print("Append!\n")
        queue.append( ((b1, 0), depth+1) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(b1, 0)] = path

    if b1 > 0 and b2 < c2 and b1 >= (c2 - b2) and (b1-(c2-b2), c2) not in visited.keys():
        #print("Append!\n")
        queue.append( ((b1-(c2-b2), c2), depth+1) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(b1-(c2-b2), c2)] = path

    if b1 > 0 and b2 < c2 and b1 < (c2 - b2) and (0, b2+b1) not in visited.keys():
        #print("Append!\n")
        queue.append( ((0, b2+b1), depth+1))
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(0, b2+b1)] = path

    if b2 > 0 and b1 < c1 and b2 >= (c1 - b1) and (c1, b2-(c1-b1) ) not in visited.keys():
        #print("Append!\n")
        queue.append( ((c1, b2-(c1-b1)), depth+1) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(c1, b2-(c1-b1))] = path

    if b2 > 0 and b1 < c1 and b2 < (c1 - b1) and (b1+b2, 0) not in visited.keys():
        #print("Append!\n")
        queue.append( ((b1+b2, 0), depth+1) )
        path = paths[(b1, b2)].copy()
        path.append((b1, b2))
        paths[(b1+b2, 0)] = path

    queue.sort(key=lambda x: x[1], reverse=True)

print("FINAL QUEUE:")
print(queue)

# fim
if objectiveState in visited.keys():
    print("Path to solution: ")
    print(paths[objectiveState])
else: 
    print("No solution was found.")
