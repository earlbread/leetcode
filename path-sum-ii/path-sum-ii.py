# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        if root.val == sum and root.left is None and root.right is None:
            return [[root.val]]

        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)

        ret = []

        for l in left:
            ret.append([root.val]+l)

        for r in right:
            ret.append([root.val]+r)

        return ret
