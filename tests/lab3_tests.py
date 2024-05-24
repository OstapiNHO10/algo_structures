import unittest
from post_order import postorder

class TestPostorder(unittest.TestCase):

 def test_empty_tree(self):
   self.assertEqual(postorder(None), [])

 def test_single_node(self):
   root = TreeNode(1)
   self.assertEqual(postorder(root), [1])

 def test_left_subtree(self):
   root = TreeNode(1)
   root.left = TreeNode(2)
   self.assertEqual(postorder(root), [2, 1])

 def test_right_subtree(self):
   root = TreeNode(1)
   root.right = TreeNode(2)
   self.assertEqual(postorder(root), [2, 1])

 def test_full_binary_tree(self):
   root = TreeNode(1)
   root.left = TreeNode(2)
   root.right = TreeNode(3)
   self.assertEqual(postorder(root), [2, 3, 1])

class TreeNode:
 def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Run tests
if __name__ == '__main__':
    unittest.main()