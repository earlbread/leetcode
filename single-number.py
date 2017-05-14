class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for i in nums:
            result ^= i
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 3, 2 ,2]

    print(s.singleNumber(nums))
