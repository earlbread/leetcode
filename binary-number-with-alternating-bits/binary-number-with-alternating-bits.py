class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bit = n % 2

        while n > 0:
            if bit != n % 2:
                return False
            bit = 1 if bit == 0 else 0
            n /= 2

        return True
