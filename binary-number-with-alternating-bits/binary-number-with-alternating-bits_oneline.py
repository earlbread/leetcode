class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return ((n + (n >> 1) + 1) & (n + (n >> 1))) == 0
