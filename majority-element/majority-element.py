from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        return max(d.items(), key=lambda a: a[1])[0]
