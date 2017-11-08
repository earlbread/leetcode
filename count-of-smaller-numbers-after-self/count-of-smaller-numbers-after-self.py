class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            result.append(count)

        return result
