class Node:
   def __init__(self, value, priority):
       self.value = value
       self.priority = priority
       self.left = None
       self.right = None

class BinaryTreePriorityQueue:
   def __init__(self):
       self.root = None

   def insert(self, value, priority):
       new_node = Node(value, priority)
       if self.root is None:
           self.root = new_node
       else:
           self._insert(self.root, new_node)

   def _insert(self, current, new_node):
       if new_node.priority < current.priority:
           if current.left is None:
               current.left = new_node
           else:
               self._insert(current.left, new_node)
       else:
           if current.right is None:
               current.right = new_node
           else:
               self._insert(current.right, new_node)

   def delete_max(self):
       if self.root is None:  
           return None
       else:
           self.root, max_node = self._delete_max(self.root)
           return max_node.value

   def _delete_max(self, node):
       if node.right is None:
           return node.left, node
       else:
           node.right, max_node = self._delete_max(node.right)
       return node, max_node

   def peek(self):
       if self.root is None:
           return None
       else:
           max_node = self._find_max(self.root)
       return max_node.value

   def _find_max(self, node):
       current = node
       while current.right is not None:
           current = current.right
       return current

   def inorder_traversal(self):
       elements = []
       self._inorder_traversal(self.root, elements)
       return elements

   def _inorder_traversal(self, node, elements):
       if node:
           self._inorder_traversal(node.left, elements)
           elements.append((node.value, node.priority))
           self._inorder_traversal(node.right, elements)
