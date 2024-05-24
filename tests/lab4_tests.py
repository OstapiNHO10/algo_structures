import unittest
from binary_tree_priority_queue import BinaryTreePriorityQueue

class TestBinaryTreePriorityQueue(unittest.TestCase):

   def setUp(self):
       self.pq = BinaryTreePriorityQueue()
       self.pq.insert("apple", 5)
       self.pq.insert("banana", 3)
       self.pq.insert("cherry", 4)
       self.pq.insert("date", 7)
       self.pq.insert("elderberry", 2)

   def test_insert_and_inorder_traversal(self):
       expected = [("elderberry", 2), ("banana", 3), ("cherry", 4), ("apple", 5), ("date", 7)]
       self.assertEqual(self.pq.inorder_traversal(), expected)

   def test_peek(self):
       self.assertEqual(self.pq.peek(), "date")

   def test_delete_max(self):
       self.assertEqual(self.pq.delete_max(), "date")
       expected_after_delete = [("elderberry", 2), ("banana", 3), ("cherry", 4), ("apple", 5)]
       self.assertEqual(self.pq.inorder_traversal(), expected_after_delete)
       self.assertEqual(self.pq.peek(), "apple")

   def test_delete_max_on_empty_queue(self):
       empty_pq = BinaryTreePriorityQueue()
       self.assertIsNone(empty_pq.delete_max())

   def test_peek_on_empty_queue(self):
       empty_pq = BinaryTreePriorityQueue()
       self.assertIsNone(empty_pq.peek())

if __name__ == "__main__":
   unittest.main()
