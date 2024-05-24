class BinaryTree:
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
def postorder(root):
   res = []

   def dfs(node):
       if not node:
           return

       dfs(node.left)
       dfs(node.right)
  
       res.append(node.val)
   dfs(root)
   return res