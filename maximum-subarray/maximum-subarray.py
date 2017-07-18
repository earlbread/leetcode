class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = nums[0]
        max_i = 0
        max_j = 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                s = sum(nums[i:j])
                if s > maximum:
                    maximum = s
                    max_i = i
                    max_j = j

        return sum(nums[max_i:max_j])
