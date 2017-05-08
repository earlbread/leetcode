class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = 1
        num_len = 1
        count = 9

        while n > num_len * count:
            n -= num_len * count
            num_len += 1
            count *= 10
            number *= 10

        number += (n - 1) // num_len

        return int(str(number)[(n - 1) % num_len])

if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(10))
    print(s.findNthDigit(21))
    print(s.findNthDigit(100))
