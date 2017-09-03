# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return root

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        if L <= root.val <= R:
            return root

        if root.left is None:
            return root.right

        return root.left
