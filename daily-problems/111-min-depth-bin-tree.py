'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # MAX = 10 ** 20
        # def findMinDepth(root):
        #     if not root:
        #         return MAX
        #     if not root.left and not root.right:
        #         return 1
        #     left = findMinDepth(root.left)
        #     right = findMinDepth(root.right)

        #     return 1+min(left, right)

        # l = findMinDepth(root.left)
        # r = findMinDepth(root.right)

        # if l == MAX and r == MAX:
        #     return 1
        # return 1+min(l, r)

        # SHORTER VERSION
        if not root:
            return 0
        if not root.left:
            return 1+self.minDepth(root.right)
        elif not root.right:
            return 1+self.minDepth(root.left)
        else:
            return 1+min(self.minDepth(root.left), self.minDepth(root.right))
