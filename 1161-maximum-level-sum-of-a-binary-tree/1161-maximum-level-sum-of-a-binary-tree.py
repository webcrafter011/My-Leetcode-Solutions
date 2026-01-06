from collections import deque
# this is prebuilt queue data structure
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # this is like default function in which we have to write solutoin it is given already for every question this function runs when we submit answer then they cross check ohh, self the constructor object, yes root is the root node of the binary tree whcih is given to us so they have given us a binary tree for that binary tree we have to find this
        # I will start by reading problem statement 
        # then i will go to check examples 
        # what we have to find in this proboem is very important in every question
        # step 1 understand what is asked
        # so in this problem they are saying that we are given a binary tree 
        # a binary tree is a data structure consisting of one root node following two child nodes and every child has their two child nodes and so on 
        # in binary tree there are levels as you can see root node is at first level and root's child are at 2nd node 

        # Step 2. find what if asked and try to come up with solution
        # so in this problem we are asked to find sum of all the values of nodes at level x such that x should be smallest basically

        # read that sentence 3-4 times if you did not understand it 

        # maximum and maximum are same 
        # I am drawing my solutions on paper this is the best way to understand the problem allright guys?


        # because this is leetcode's problem of the day they normally these many prople wont be online for a problem 

        # so I am thinking of a standard BFS solution 
        # breath first search is a graph traversal algorithm which goes level wise if we have added elements to the queue 

        # so let me tell you binary tree or any kind of tree are also a graph 
        # graphs are like a superset and trees also come under graphs so we can use bfs to solve this problem 

        # first we will try to get sum of all the levels using bfs and we will return the maximum value after completing entire bfs

        if not root:
            return 0
        # if no root is given maximum sum isnt possible in that case return 0

        # so now i will start implementing bfs 

        # we will need one variable to return as an answer 
        maxi = root.val # instead we can keep maxi as root.val which is actually sum of the first level elements since first level only has root

        # we will need a queue to implement bfs 
        q = deque([root])
        # we can also keep a level variable to keep track of level we will update best level if we find better sum for a level
        level = 1 # initially 
        best_level = 1

        while q:
            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # if we found better sum for the level we update our global sum and best_level found so far 
            if curr_sum > maxi:
                maxi = curr_sum
                best_level = level

            level += 1

        
        return best_level
    # we are getting wrong answer oops i returned wrong variable 