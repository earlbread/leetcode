# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        secondMinimum = -1
        q = [root]

        while len(q) != 0:
            node = q.pop(0)

            if (node.val > root.val) and (secondMinimum == -1 or node.val < secondMinimum):
                secondMinimum = node.val

            if node.left:
                q.append(node.left)
                q.append(node.right)

        return secondMinimum

