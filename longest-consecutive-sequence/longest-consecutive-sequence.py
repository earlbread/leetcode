class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for n in nums:
            h[n] = 1

        longest = 0
        for n in nums:
            if (n - 1) not in h:
                i = n + 1
                while i in h:
                    i += 1
                longest = max(longest, i - n)

        return longest
