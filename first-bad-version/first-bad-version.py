# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n

        bad_version = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if isBadVersion(mid):
                bad_version = mid
                hi = mid - 1
            else:
                lo = mid + 1


        return bad_version
