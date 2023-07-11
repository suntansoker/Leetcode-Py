'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def findParent(node, par):
            parent[node] = par
            if node.left:
                findParent(node.left, node)
            if node.right:
                findParent(node.right, node)
            return

        findParent(root, None)
        q = [(0, target)]
        vis = set()
        vis.add(None)
        dist = 0
        while q:
            if dist == k:
                break
            l = len(q)
            for i in range(l):
                dis, node = q.pop(0)
                vis.add(node)
                if parent[node] not in vis:
                    q.append((dis+1, parent[node]))
                if node.left not in vis:
                    q.append((dis+1, node.left))
                if node.right not in vis:
                    q.append((dis+1, node.right))

            dist += 1

        ans = []
        while q:
            ans.append(q.pop(0)[1].val)

        return ans
