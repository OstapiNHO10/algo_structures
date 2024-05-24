from collections import deque

def bfs(maze, start, end):
   rows, cols = len(maze), len(maze[0])
   queue = deque([(start[0], start[1], 0)]) 
   visited = set()
   visited.add((start[0], start[1]))
   directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  
   while queue:
       x, y, steps = queue.popleft()
      
       if (x, y) == (end[0], end[1]):
           return steps
      
       for dx, dy in directions:
           nx, ny = x + dx, y + dy
           if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
               visited.add((nx, ny))
               queue.append((nx, ny, steps + 1))
  
   return -1