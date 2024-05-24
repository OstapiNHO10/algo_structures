import unittest
from simplify_busy_schedule import simplify_busy_schedule
class TestSimplifySchedule(unittest.TestCase):

   def test_empty_schedule(self):
       self.assertEqual(simplify_busy_schedule([]), [])

   def test_single_event(self):
       schedule = [(2, 4)]
       self.assertEqual(simplify_busy_schedule(schedule), schedule)

   def test_non_overlapping_events(self):
       schedule = [(1, 2), (4, 5), (7, 8)]
       simplified = schedule.copy()  # Очікуємо отримати копію початкового розкладу
       self.assertEqual(simplify_busy_schedule(schedule), simplified)

   def test_complex_schedule(self):
       schedule = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
       simplified = [(0, 1), (3, 8), (9, 12)]
       self.assertEqual(simplify_busy_schedule(schedule), simplified)

if __name__ == '__main__':
   unittest.main()