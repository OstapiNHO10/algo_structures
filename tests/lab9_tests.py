import unittest
from electricity import calculate_max_wire_length

class TestCalculateMaxWireLength(unittest.TestCase):
   def test_case_1(self):
       w = 2
       heights = [3, 3, 3]
       result = calculate_max_wire_length(w, heights)
       self.assertEqual(result, 2.83)

   def test_case_2(self):
       w = 100
       heights = [1, 1, 1, 1]
       result = calculate_max_wire_length(w, heights)
       self.assertEqual(result, 300.00)

   def test_case_3(self):
       w = 4
       heights = [100, 2, 100, 2, 100]
       result = calculate_max_wire_length(w, heights)
       self.assertEqual(result, 396.32)

   def test_case_4(self):
       w = 4
       heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
       result = calculate_max_wire_length(w, heights)
       self.assertEqual(result, 2738.18)

if __name__ == "__main__":
   unittest.main()
