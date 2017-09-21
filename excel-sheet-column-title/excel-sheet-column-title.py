from collections import deque

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = deque()

        while n > 0:
            ret.appendleft(chr((n - 1) % 26 + ord('A')))
            n = (n - 1) // 26

        return ''.join(ret)
