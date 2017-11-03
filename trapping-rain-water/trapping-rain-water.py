class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0

        lo = 0
        hi = len(height) - 1

        left_max = 0
        right_max = 0

        while lo < hi:
            if height[lo] < height[hi]:
                if height[lo] > left_max:
                    left_max = height[lo]
                else:
                    result += left_max - height[lo]
                lo += 1
            else:
                if height[hi] > right_max:
                    right_max = height[hi]
                else:
                    result += right_max - height[hi]
                hi -= 1

        return result
