class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}

        for i in range(len(nums)):
            if nums[i] in complements:
                return [complements[nums[i]], i]
            else:
                complements[target - nums[i]] = i

        raise Exception('Something is wrong!')


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    print(s.twoSum(nums, target))
