class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1

s = Solution()
a = [1, 7, 3, 6, 5, 6]
b = [1, 2, 3]

assert s.pivotIndex(a) == 3
assert s.pivotIndex(b) == -1
