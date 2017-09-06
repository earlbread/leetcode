class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def _permute(nums, begin, ret):
            if begin >= len(nums):
                ret.append(nums[:])
                return ret

            for i in range(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                _permute(nums, begin + 1, ret)
                nums[i], nums[begin] = nums[begin], nums[i]

            return ret

        return _permute(nums, 0, [])
