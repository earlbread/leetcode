# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder_(self, queue, result):
        if len(queue) == 0:
            return result

        current = []
        children = []

        for q in queue:
            current.append(q.val)

            if q.left is not None:
                children.append(q.left)
            if q.right is not None:
                children.append(q.right)

        result.append(current)

        return self.levelOrder_(children, result)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        result = []
        return self.levelOrder_(queue, result)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.levelOrder(root))
