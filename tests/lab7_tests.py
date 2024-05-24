import unittest
from Boyer_Moore import find_needle_in_haystack

class TestBoyerMoore(unittest.TestCase):
   def test_found_needle(self):
       needle = "дані"
       haystack = "метеодані"
       result = find_needle_in_haystack(needle, haystack)
       self.assertEqual(result, "needle is found at index 5")

   def test_not_found_needle(self):
       needle = "дані"
       haystack = "метео"
       result = find_needle_in_haystack(needle, haystack)
       self.assertEqual(result, "Nothing found")

   def test_empty_haystack(self):
       needle = "дані"
       haystack = ""
       result = find_needle_in_haystack(needle, haystack)
       self.assertEqual(result, "Nothing found")

   def test_empty_needle(self):
       needle = ""
       haystack = "метеодані"
       result = find_needle_in_haystack(needle, haystack)
       self.assertEqual(result, "Nothing found")

   def test_needle_equals_haystack(self):
       needle = "метеодані"
       haystack = "метеодані"
       result = find_needle_in_haystack(needle, haystack)
       self.assertEqual(result, "needle is found at index 1")

   def test_multiple_occurrences(self):
       needle = "ан"
       haystack = "даніданідані"
       result = find_needle_in_haystack(needle, haystack)
       self.assertEqual(result, "needle is found at index 2")  # First occurrence

if __name__ == "__main__":
   unittest.main()
