# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSumAndTilt(self, root):
        if root is None:
            return (0, 0)

        left_sum, left_tilt = self.findSumAndTilt(root.left)
        right_sum, right_tilt = self.findSumAndTilt(root.right)

        root_sum = left_sum + right_sum + root.val
        root_tilt = left_tilt + right_tilt + abs(left_sum - right_sum)

        return (root_sum, root_tilt)

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findSumAndTilt(root)[1]

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.findTilt(root))
