from collections import deque
import math

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return "#"  # Handle empty tree

        ser = ''
        q = deque([root])

        while q:
            node = q.popleft()

            if node is None:  # Check for None 
                ser += '#,'
                continue

            # Append the value to the string (the fix!)
            ser += str(node.val) + ','
            
            # Add children to the queue. 
            # Crucially, add 'None' markers for null children.
            q.append(node.left if node.left else None)
            q.append(node.right if node.right else None)
                    
        # Optional: Remove the trailing comma
        return ser.rstrip(',')            
                

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data or data == '#':
            return None

        i = 1
        vals = data.split(',')

        root = TreeNode(vals[0])
        q = deque([root])

        while i < len(vals):
            node = q.popleft()

            if vals[i] != '#':
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            if i < len(vals) and vals[i] != '#':
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        
        return root