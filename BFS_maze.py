from collections import deque

def is_valid_move(maze, visited, x, y):
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1 and not visited[x][y]:
        return True
    return False

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start, [])])  

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path + [(x, y)]

        visited[x][y] = True

        for direction in range(4):
            new_x, new_y = x + dx[direction], y + dy[direction]
            if is_valid_move(maze, visited, new_x, new_y):
                queue.append(((new_x, new_y), path + [(x, y)]))

    return []

maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0]
]

start = (0, 1)
end = (5, 4)

path = bfs(maze, start, end)
print(path)
