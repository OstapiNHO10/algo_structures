import unittest
from mazequeue import bfs

class TestPathFinder(unittest.TestCase):

   def test_find_path(self):
       maze = [
           [1, 0, 0, 1],
           [1, 1, 0, 0],
           [0, 1, 1, 1],
           [1, 0, 1, 1]
       ]
       start = (0, 0)
       end = (3, 3)
       result = bfs(maze, start, end)
       self.assertEqual(result, 6) 

   def test_no_path(self):
       maze = [
           [1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]
       ]
       start = (0, 0)
       end = (3, 3)
       result = bfs(maze, start, end)
       self.assertEqual(result, -1) 

   def test_start_blocked(self):
       maze = [
           [0, 0, 0, 1],
           [1, 1, 0, 0],
           [0, 1, 1, 1],
           [1, 0, 1, 1]
       ]
       start = (0, 0)
       end = (3, 3)
       result = bfs(maze, start, end)
       self.assertEqual(result, -1) 

   def test_end_blocked(self):
       maze = [
           [1, 0, 0, 1],
           [1, 1, 0, 0],
           [0, 1, 1, 1],
           [1, 0, 1, 0]
       ]
       start = (0, 0)
       end = (3, 3)
       result = bfs(maze, start, end)
       self.assertEqual(result, -1)

   def test_single_cell_path(self):
       maze = [
           [1]
       ]
       start = (0, 0)
       end = (0, 0)
       result = bfs(maze, start, end)
       self.assertEqual(result, 0)

   def test_large_maze(self):
       maze = [
           [1, 0, 1, 1, 1],
           [1, 1, 1, 0, 1],
           [0, 1, 0, 1, 1],
           [1, 1, 1, 1, 0],
           [0, 0, 1, 1, 1]
       ]
       start = (0, 0)
       end = (4, 4)
       result = bfs(maze, start, end)
       self.assertEqual(result, 8)

if __name__ == '__main__':
   unittest.main()
