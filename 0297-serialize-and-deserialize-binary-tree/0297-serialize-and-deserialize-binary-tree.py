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
            return "None,"

        serialized = ''
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                serialized += str(node.val) + ','
                q.append(node.left)
                q.append(node.right)
            else:
                serialized += 'None,'

        return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree."""

        def remove_last_level_nones(arr):
            # Removes only the trailing None values from the last *complete* level
            # but keeps inner None values intact
            n = len(arr)
            if n == 0:
                return arr
            # trim trailing "None"s that come in a batch of 2^h size
            while arr and arr[-1] == 'None':
                arr.pop()
            return arr

        if not data or data == "None,":
            return None

        tree_vals = data.split(',')
        tree_vals.pop()  # remove last empty string
        tree_vals = remove_last_level_nones(tree_vals)

        # Build the tree using BFS reconstruction
        if not tree_vals or tree_vals[0] == 'None':
            return None

        root = TreeNode(int(tree_vals[0]))
        q = deque([root])
        i = 1

        while q and i < len(tree_vals):
            node = q.popleft()
            # left child
            if i < len(tree_vals) and tree_vals[i] != 'None':
                node.left = TreeNode(int(tree_vals[i]))
                q.append(node.left)
            i += 1

            # right child
            if i < len(tree_vals) and tree_vals[i] != 'None':
                node.right = TreeNode(int(tree_vals[i]))
                q.append(node.right)
            i += 1

        return root
