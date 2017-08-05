class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xmin = -2 ** 31
        xmax = 2 ** 31 - 1

        sign = 1
        if x < 0:
            sign = -1
            x *= -1

        result = 0

        while x != 0:
            result *= 10
            result += x % 10
            x /= 10

        result *= sign

        if result < xmin or result > xmax:
            return 0

        return result
