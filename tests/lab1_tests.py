import unittest
from two_sum import two_sum

class TestTwoSumSorted(unittest.TestCase):

 def test_sorted_valid_pair(self):
   self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 2))

 def test_sorted_multiple_solutions(self):
   self.assertEqual(two_sum([2, 3, 7, 11, 15], 9), (0, 1))  # First pair

 def test_sorted_target_not_found(self):
   self.assertEqual(two_sum([1, 2, 3, 4, 5], 10), None)

# Run tests
if __name__ == '__main__':
 unittest.main()