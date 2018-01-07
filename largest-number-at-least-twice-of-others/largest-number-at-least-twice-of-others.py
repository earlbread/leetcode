class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = 0
        for i in range(len(nums)):
            if nums[i] > nums[largest]:
                largest = i

        for i in range(len(nums)):
            if i == largest:
                continue

            if nums[i] * 2 > nums[largest]:
                return -1

        return largest
