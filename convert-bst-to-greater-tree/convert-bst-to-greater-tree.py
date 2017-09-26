# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def convertAndMax(root, sum):
            if root is None:
                return root, sum

            right, max = convertAndMax(root.right, sum)

            root.val = root.val + max

            if root.left:
                left, max = convertAndMax(root.left, root.val)
                return root, max

            return root, root.val

        converted, max = convertAndMax(root, 0)
        return converted
