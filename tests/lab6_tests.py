import unittest
from lab6 import max_experience

class TestCareer(unittest.TestCase):
   def test_case_1(self):
       L = 4
       levels = [
           [4],
           [3, 1],
           [2, 1, 5],
           [1, 3, 2, 1]
       ]
       self.assertEqual(max_experience(L, levels), 12)

   def test_case_2(self):
       L = 1
       levels = [
           [9999]
       ]
       self.assertEqual(max_experience(L, levels), 9999)

   def test_case_3(self):
       L = 5
       levels = [
           [0],
           [1, 1],
           [0, 0, 0],
           [1, 1, 1, 1],
           [0, 1, 0, 1, 0]
       ]
       self.assertEqual(max_experience(L, levels), 3)

   def test_case_4(self):
       L = 3
       levels = [
           [1],
           [2, 3],
           [4, 5, 6]
       ]
       self.assertEqual(max_experience(L, levels), 10)

if __name__ == "__main__":
   unittest.main()
