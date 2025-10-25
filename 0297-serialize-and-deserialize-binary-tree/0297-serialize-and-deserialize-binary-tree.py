# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string using Level-Order Traversal.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        # Use deque for efficient popleft
        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            
            if node:
                # Append the value as a string
                result.append(str(node.val))
                # Add children (including None) to the queue
                queue.append(node.left)
                queue.append(node.right)
            else:
                # Append the placeholder 'None'
                result.append('None')
        
        # We need to trim trailing 'None' values that represent children 
        # of already-processed 'None' nodes, or the trailing 'None's 
        # that were pushed but not needed.
        while result and result[-1] == 'None':
            result.pop()

        # Join the list into a comma-separated string
        return ','.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
            
        # Split the string and convert elements to a list of strings/placeholders
        nodes_str = data.split(',')
        
        # The first element is the root
        root_val = nodes_str[0]
        root = TreeNode(int(root_val))
        
        # Use a queue to keep track of parent nodes waiting for their children
        queue = deque([root])
        # Start reading the serialized data from the second element (index 1)
        i = 1

        while queue and i < len(nodes_str):
            parent = queue.popleft()
            
            # --- Left Child ---
            if i < len(nodes_str):
                left_val_str = nodes_str[i]
                if left_val_str != 'None':
                    left_node = TreeNode(int(left_val_str))
                    parent.left = left_node
                    queue.append(left_node) # Add the new child to the queue
                i += 1
            
            # --- Right Child ---
            if i < len(nodes_str):
                right_val_str = nodes_str[i]
                if right_val_str != 'None':
                    right_node = TreeNode(int(right_val_str))
                    parent.right = right_node
                    queue.append(right_node) # Add the new child to the queue
                i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# # Example usage:
# # tree_root = TreeNode(1)
# # tree_root.left = TreeNode(2)
# # tree_root.right = TreeNode(3)
# # tree_root.right.left = TreeNode(4)
# # tree_root.right.right = TreeNode(5)
# # serialized_data = ser.serialize(tree_root) # Expected: '1,2,3,None,None,4,5'
# # ans = deser.deserialize(serialized_data)
# # print(ser.serialize(ans)) # Check: Should be '1,2,3,None,None,4,5'