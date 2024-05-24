import unittest
from src.main import kruskal_minimum_spanning_tree

class TestKruskalMinimumSpanningTree(unittest.TestCase):
   def test_basic_case(self):
       wells = [
           ('K1', 'K2', 1),
           ('K2', 'K3', 2),
           ('K1', 'K3', 2)
       ]
       result = kruskal_minimum_spanning_tree(wells)
       self.assertEqual(result, 3)

   def test_disconnected_case(self):
       wells = [
           ('K1', 'K2', 1),
           ('K3', 'K4', 2)
       ]
       result = kruskal_minimum_spanning_tree(wells)
       self.assertEqual(result, -1)

   def test_large_case(self):
       wells = [
           ('K1', 'K2', 1),
           ('K2', 'K3', 2),
           ('K3', 'K4', 3),
           ('K4', 'K5', 4),
           ('K5', 'K1', 5)
       ]
       result = kruskal_minimum_spanning_tree(wells)
       self.assertEqual(result, 10)

if __name__ == "__main__":
   unittest.main()
