import heapq

# Ouvrir le fichier maze.mz
with open("maze.mz", "r") as f:
    maze = [list(line.strip()) for line in f]

# Trouver l'entrée et la sortie du labyrinthe
start = (0, 0)
end = (len(maze)-1, len(maze[0])-1)

# Initialiser le coût de chaque case à l'infini
costs = {(i, j): float('inf') for i in range(len(maze)) for j in range(len(maze[0]))}

# Le coût de l'entrée est de 0
costs[start] = 0

# Utiliser l'algorithme de Dijkstra pour trouver le chemin le plus court
heap = [(0, start)]
while heap:
    (cost, current) = heapq.heappop(heap)
    if current == end:
        break
    for next in [(current[0]+1, current[1]), (current[0]-1, current[1]), (current[0], current[1]+1), (current[0], current[1]-1)]:
        if next[0] < 0 or next[0] >= len(maze) or next[1] < 0 or next[1] >= len(maze[0]):
            continue
        new_cost = cost + 1
        if new_cost < costs[next] and maze[next[0]][next[1]] != "#":
            costs[next] = new_cost
            heapq.heappush(heap, (new_cost, next))

# Marquer le chemin dans le labyrinthe
x, y = end
while (x, y) != start:
    min_cost = float('inf')
    min_node = None
    for next in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if next[0] < 0 or next[0] >= len(maze) or next[1] < 0 or next[1] >= len(maze[0]):
            continue
        if costs[next] < min_cost:
            min_cost = costs[next]
            min_node = next
    x, y = min_node
    maze[x][y] = "X"

# Écrire le labyrinthe modifié dans un nouveau fichier
with open("maze-out.mz", "w") as f:
    for row in maze:
        f.write("".join(row) + "\n")

