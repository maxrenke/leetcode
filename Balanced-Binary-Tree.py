1class TreeNode:
2    def __init__(self, val=0, left=None, right=None):
3        self.val = val
4        self.left = left
5        self.right = right
6
7from typing import Optional
8
9class Solution:
10    def isBalanced(self, root: Optional[TreeNode]) -> bool:
11        
12        # Define helper function to return height and balance status of the tree.
13        def get_height_and_balance(node):
14            if not node:
15                return 0, True
16            
17            left_height, left_balanced = get_height_and_balance(node.left)
18            right_height, right_balanced = get_height_and_balance(node.right)
19
20            # If either subtree is unbalanced or height difference > 1,
21            # the whole tree will be considered as unbalanced.
22            if not left_balanced or not right_balanced or abs(left_height - right_height) > 1:
23                return 0, False
24
25            # Otherwise, the current node seems balanced and we can compute its height.
26            return max(left_height, right_height) + 1, True
27        
28        # Start helper function for root node
29        return get_height_and_balance(root)[1]